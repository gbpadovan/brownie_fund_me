from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]                    # compiled contract
    account = get_account()
    # price = fund_me.getPrice()
    entrance_fee = fund_me.getEntranceFee() # calls function getEntranceFee() from FundMe.sol
    print(f"Entrance fee (in WEI): {entrance_fee}")
    print(f"Funding")
    # calls function fund() from FundMe.sol
    # pass {'value':entrance_fee} as a web3.py transaction
    fund_me.fund({'from':account, 'value':entrance_fee}) 
    return


def withdraw():
    fund_me = FundMe[-1]                    # compiled contract
    account = get_account()
    fund_me.withdraw({'from':account,})     # calls function withdraw() from FundMe.sol
    return


def main():
    fund()
    withdraw()
    return