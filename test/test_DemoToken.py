import unittest
import DemoTokenWrapper
import SdkUtils

owner = "ATwo3VeAj4JnDY2uP1aKWS4p5LhyFHJeiE"
alice = "AGgWM5cmmmRUH9iwZaigYk4n4NKpkD2kEC"
ownerAccount = SdkUtils.GetSdk().wallet_manager.get_account(owner, '123')

class TestDemoToken(unittest.TestCase):
    def test_mint(self):
        balance = DemoTokenWrapper.Balance(owner)
        self.assertEqual(balance, 0) # Initial balance is zero

        result = DemoTokenWrapper.Init() # Initialize contract
        self.assertEqual(result, True)
        
        balance = DemoTokenWrapper.Balance(owner)
        self.assertEqual(balance, 10000000000000000) # Balance is equal to total supply

    def test_transfer_tokens(self):
        transfer_amount = 100000
        owner_balance_before = DemoTokenWrapper.Balance(owner)
        alice_balance_before = DemoTokenWrapper.Balance(alice) # Check initial balances

        DemoTokenWrapper.Transfer(owner, alice, transfer_amount, ownerAccount) # Transfer some coins

        owner_balance_after = DemoTokenWrapper.Balance(owner)
        alice_balance_after = DemoTokenWrapper.Balance(alice)
        self.assertEqual(owner_balance_after, owner_balance_before - transfer_amount)
        self.assertEqual(alice_balance_after, alice_balance_before + transfer_amount) # Check balances after transfer


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDemoToken('test_mint'))
    suite.addTest(TestDemoToken('test_transfer_tokens'))
    return suite

if __name__ == '__main__':
    unittest.main()
