import yaml
from yaml.loader import SafeLoader

from web3 import Web3

def load_addresses():
    return load_yaml_config('config/addresses.yaml')

def load_configs():
    return load_yaml_config('config/configs.yaml')

def load_yaml_config(path):
    with open(path) as f:
        data = yaml.load(f, Loader=SafeLoader)
        return data

if __name__ == "__main__":
    addresses = load_addresses()
    configs = load_configs()

    w3 = Web3(Web3.HTTPProvider(configs['infura_url']))

    # Get balance from my wallet address
    balance_wei = w3.eth.get_balance(addresses['ethereum'][0])
    balance = w3.fromWei(balance_wei, 'ether')

    # transaction_hash = '0xf2dc320ca36d8685c1fbde2a8b75583f89fd5468428e95a63d2834f5564edde5'

    print(balance)
