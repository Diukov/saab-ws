import unittest
from day1._4debugging.exercise3_deadlock import BankAccount, transfer
import threading

class TestBankTransfer(unittest.TestCase):
    def test_transfers(self):
        account_a = BankAccount(1000)
        account_b = BankAccount(1000)

        t1 = threading.Thread(target=transfer, args=(account_a, account_b, 100))
        t2 = threading.Thread(target=transfer, args=(account_b, account_a, 200))

        t1.start()
        t2.start()
        t1.join()
        t2.join()

        self.assertEqual(account_a.balance, 1100)
        self.assertEqual(account_b.balance, 900)

if __name__ == '__main__':
    unittest.main()
