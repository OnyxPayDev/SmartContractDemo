#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

from punica.common.define import DEFAULT_CONFIG

from punica.exception.punica_exception import PunicaException, PunicaError


def handle_network_config(config_dir_path: str, network: str = '', is_print: bool = True) -> str:
    try:
        print(config_dir_path)
        config_file_path = os.path.join(config_dir_path, 'punica-config.json')
        with open(config_file_path, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        raise PunicaException(PunicaError.config_file_not_found)
    try:
        network_dict = config['networks']
        default_net = config['defaultNet']
    except KeyError:
        raise PunicaException(PunicaError.config_file_error)
    if network == '':
        if default_net == '':
            network = list(network_dict.keys())[0]
        else:
            default_network = network_dict.get(default_net, '')
            if default_network == '':
                raise PunicaException(PunicaError.other_error('there is not the network: ' + default_net))
            else:
                network = default_net
    try:
        rpc_address = ''.join([network_dict[network]['host'], ':', str(network_dict[network]['port'])])
    except KeyError:
        raise PunicaException(PunicaError.config_file_error)
    if is_print:
        print('Using network \'{}\'.\n'.format(network))
    return rpc_address


def handle_deploy_config(project_dir_path: str, config: str = ''):
    try:
        if config != '':
            config_path = os.path.join(project_dir_path, config)
            if os.path.exists(config_path):
                if not os.path.isfile(config_path):
                    raise PunicaError.other_error(config_path, ' is not file')
            else:
                config_path = os.path.join(project_dir_path, 'contracts', config)
                if not os.path.exists(config_path):
                    raise PunicaError.other_error(config_path, ' not exist')
        else:
            config_path = os.path.join(project_dir_path, 'contracts', DEFAULT_CONFIG)
        if not os.path.exists(config_path):
            print(config_path, ' not exist')
            os._exit(0)
        with open(config_path, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        raise PunicaException(PunicaError.config_file_not_found)
    try:
        wallet_file = config['defaultWallet']
        deploy_information = config['deployConfig']
        password_information = config['password']
    except KeyError:
        raise PunicaException(PunicaError.config_file_error)
    if not isinstance(deploy_information, dict):
        raise PunicaException(PunicaError.config_file_error)
    return wallet_file, deploy_information, password_information


def handle_invoke_config(project_dir_path: str, config: str):
    try:
        if config != '':
            config_path = os.path.join(project_dir_path, config)
            if not os.path.exists(config_path):
                if os.path.dirname(config) != '':
                    raise PunicaException(PunicaError.other_error(config + ' not found'))
                else:
                    config_path = os.path.join(project_dir_path, 'contracts', config)
                    if not os.path.exists(config_path):
                        raise PunicaException(PunicaError.other_error(config_path + ' not exist'))
        else:
            config_path = os.path.join(project_dir_path, 'contracts', DEFAULT_CONFIG)
        if not os.path.exists(config_path):
            raise PunicaException(PunicaError.other_error(config_path + ' not found'))
        with open(config_path, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        raise PunicaException(PunicaError.config_file_not_found)
    try:
        wallet_file = config['defaultWallet']
        invoke_config = config['invokeConfig']
        password_config = config['password']
    except KeyError:
        raise PunicaException(PunicaError.other_error('the config file lack invokeConfig or password'))
    if not isinstance(invoke_config, dict):
        raise PunicaException(PunicaError.config_file_error)
    return wallet_file, invoke_config, password_config
