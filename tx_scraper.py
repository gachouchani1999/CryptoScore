from typing import Dict
import urllib.request, json
import time
def address_scraper(
    crypto_addr,
) -> Dict:
    """
    Extracts the wallet from the BlockCypher API
    """
    if crypto_addr[:2] == '0x':
        url = "https://api.blockcypher.com/v1/eth/main/addrs/" +crypto_addr + '/full?limit=50'
        
        
    else:
        url = "https://api.blockcypher.com/v1/btc/main/addrs/" +crypto_addr + '/full?limit=50'
        
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())  
    return data



def basic_extractor(
    data: Dict,
) -> list: 
    """
    Returns list of the total_recieved token, the total sent token and the number of transactions the wallet participated in.
    """
    return [data["total_received"],data["total_sent"],data["n_tx"]]






def tx_extractor (
    data: Dict,
) -> list:

    """
    Returns list of transactions
    tx_data format:
    
    """

    all_tx = []
    
    tx_arr = data["txs"]
    for tx in tx_arr:
        tx_data = {}
        tx_data['hash'] = tx["hash"]
        tx_data['value'] = tx['total']
        tx_data['sender'] = tx["inputs"][0]["addresses"][0]
        tx_data['receiver'] = tx["outputs"][0]["addresses"][0]
        all_tx.append(tx_data)
        
    return all_tx




