from typing import Dict
import urllib.request, json
import time
def address_scraper(
    crypto_addr,
) -> Dict:
    """
    Extracts the wallet from the BlockCypher API
    """
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




def depth3_list(
    data: Dict,
    all_tx: list,
) -> list:
    """
    Takes as argument the list of transactions from tx_extractor function and returns it recursively with depth 3
    """
    final_tx = []
    final_tx.append(all_tx)
    for tx in all_tx:
        if tx['sender'] != data['address']:
            print('done 1')
            new_data = address_scraper(tx['sender'])
            new_txs = tx_extractor(new_data)
            for tx in new_txs:
                final_tx.append(tx)
        if tx['receiver'] != data['address']:
            print('done2')
            new_data = address_scraper(tx['receiver'])
            new_txs = tx_extractor(new_data)
            for tx in new_txs:
                final_tx.append(tx)
    return final_tx

data = address_scraper("bc1qa5wkgaew2dkv56kfvj49j0av5nml45x9ek9hz6")
tx_lst = tx_extractor(data)
tx_lst3 = depth3_list(data,tx_lst)
