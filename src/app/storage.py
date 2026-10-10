import json
import os

from src.app.models import Account, Transaction
from src.config import ACC_DATA, TXN_DATA

# implement locking into save functions


def ensure_files():
    """Ensure data/accounts.json and data/transactions.json is present in the working directory"""

    os.makedirs("data", exist_ok=True)

    for i in (ACC_DATA, TXN_DATA):
        if not os.path.exists(i):
            with open(i, "x") as file:
                json.dump([], file, indent=4)


def load_accounts() -> list[Account]:
    """Load every account details from data/accounts.json into a python supported data type."""

    with open(ACC_DATA, "r") as f:
        result = list(json.load(f))

    return [Account.from_dict(data) for data in result]


def save_accounts(accounts: list[Account]):
    """Save account details into data/accounts.json"""

    with open(ACC_DATA, "w") as f:
        json.dump([a.to_dict() for a in accounts], f, indent=4)


def save_transaction(txn: Transaction):
    """Save transaction details into data/transactions.json"""

    # get all the txns from the json file into a list
    with open(TXN_DATA, "r") as f:
        data = list(json.load(f))

    # add new txn to the list of all txns
    data.append(txn.to_dict())

    with open(TXN_DATA, "w") as f:
        json.dump(data, f, indent=4)
