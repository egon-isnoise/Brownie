
from brownie import SimpleStorage, accounts, config

def read_contract():
    simple_storage = SimpleStorage[-1]
    # uses -1 so we always take the last contract deployed (it's like array.length() -1)
    # address and ABI are already known from brownie
    print(simple_storage.retrieve())

def main():
    read_contract()