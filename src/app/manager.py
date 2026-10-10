from src.app.errors import AccountNotFound
from src.app.models import Account, Transaction
from src.app.storage import load_accounts, save_accounts, save_transaction
from src.app.utils import generate_id


class BankManager:
    def __init__(self):
        self.__accounts = load_accounts()

    def create(self, name: str):
        acc = Account(generate_id(), name)
        self.__accounts.append(acc)

        save_accounts(self.__accounts)
        return acc

    def find_account(self, acc_id: str):
        for acc in self.__accounts:
            if acc._id == acc_id:
                return acc

        raise AccountNotFound(f"{acc_id} is invalid.")

    def deposit(self, acc_id: str, amount: float):
        acc = self.find_account(acc_id)
        new_balance = acc.deposit(amount)

        txn = Transaction("deposit", amount, acc._id)

        save_transaction(txn)
        save_accounts(self.__accounts)

        return new_balance

    def withdraw(self, acc_id: str, amount: float):
        acc = self.find_account(acc_id)
        new_balance = acc.withdraw(amount)

        txn = Transaction("withdraw", amount, acc._id)

        save_transaction(txn)
        save_accounts(self.__accounts)

        return new_balance

    def transfer(self, src_id: str, trg_id: str, amount: float):
        src = self.find_account(src_id)
        trg = self.find_account(trg_id)

        new_balance = src.withdraw(amount)
        trg.deposit(amount)

        txn = Transaction("transfer", amount, src._id, trg._id)

        save_transaction(txn)
        save_accounts(self.__accounts)

        return new_balance

    def show_balance(self, acc_id: str):
        acc = self.find_account(acc_id)
        return acc.balance

    def list_accounts(self):
        return self.__accounts
