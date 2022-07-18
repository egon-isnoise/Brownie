
from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account, deploy_mocks

def deploy_fund_me():
    account = get_account()
    
    if network.show_active() != "development":
        eth_price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"];
        matic_price_feed_address = config["networks"][network.show_active()]["matic_usd_price_feed"];
        xtz_price_feed_address = config["networks"][network.show_active()]["xtz_usd_price_feed"];
        
    else:
        deploy_mocks()
        eth_price_feed_address = MockV3Aggregator[-1].address
        matic_price_feed_address = MockV3Aggregator[-1].address
        xtz_price_feed_address = MockV3Aggregator[-1].address
        
        
        
    fund_me = FundMe.deploy(
        eth_price_feed_address, 
        matic_price_feed_address,
        xtz_price_feed_address,
        {"from": account}, 
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    
    print(f"Contract deployed to {fund_me.address}")

def main():
    deploy_fund_me()