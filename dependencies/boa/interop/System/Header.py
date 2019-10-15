

class Header:

    def getmyhash(self):
        return GetHash(self)

    @property
    def Index(self):
        return GetIndex(self)

    @property
    def Hash(self):
        """

        :return:
        """
        return GetHash(self)

    @property
    def Timestamp(self):
        """

        :return:
        """
        return GetTimestamp(self)

    @property
    def Version(self):
        """

        :return:
        """
        return GetVersion(self)

    @property
    def PrevHash(self):
        """

        :return:
        """
        return GetPrevHash(self)

    @property
    def MerkleRoot(self):
        """

        :return:
        """
        return GetMerkleRoot(self)

    @property
    def ConsensusData(self):
        """

        :return:
        """
        return GetConsensusData(self)

    @property
    def NextConsensus(self):
        """

        :return:
        """
        return GetNextConsensus(self)


def GetIndex(header):
    """

    Returns the height/index of a header

    """
    pass


def GetHash(header):
    """

    gets the hash of the header

    """
    pass

def GetPrevHash(header):
    """

    gets the hash of the previous header in the blockchain

    """
    pass

def GetTimestamp(header):
    """

    gets the timestamp of when the header was created

    """
    pass
