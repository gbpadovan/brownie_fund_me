from brownie import network, config, FundMe, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS, FORKED_LOCAL_ENVIRONMENTS


def deploy_fund_me():
    """Deploys contract FundMe.sol into a blockchain.
    The FundMe.sol contract has 1 constructor parameters:

    <_priceFeed> address
    ----------------solidity code----------------------
    constructor(address _priceFeed) public {
        priceFeed = AggregatorV3Interface(_priceFeed);
        owner = msg.sender;
    }
    ----------------------------------------------------
    """
    account = get_account()
    # pass the price feed address to our fundme contract

    # if we are on a persistent network like goerli, use associated address
    # otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        contructor_param =  config['networks'][network.show_active()][
            'eth_usd_price_feed'                                         # _priceFeed
        ]                                                               
    else:
        deploy_mocks()
        contructor_param = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        contructor_param,    # add _priceFeed into our FundMe.deploy() function 
        {'from':account}, 
        publish_source=config['networks'][network.show_active()].get('verify')
    )
    print(f"Contract deployed at: {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
    return
