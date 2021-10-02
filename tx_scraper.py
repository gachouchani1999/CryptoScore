from typing import Dict
import urllib.request, json
import time
def address_scraper(
    crypto_addr,
) -> Dict:
    """
    Extracts the wallet from the BlockCypher API
    """
<<<<<<< HEAD
    url = "https://api.blockcypher.com/v1/btc/main/addrs/" +crypto_addr + '/full?limit=10&token=ff7b5a8efc0345a0b3a056d2f869128c'
=======
    url = "https://api.blockcypher.com/v1/btc/main/addrs/" +crypto_addr + '/full?limit=10&token=dd7ab7e82c07483a897166fb3510396a'
>>>>>>> 87a112fae331c387cdca067f2c2313edf7cfa221
        
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




def depth2_list(
    data: Dict,
    all_tx: list,
) -> list:
    """
    Takes as argument the list of transactions from tx_extractor function and returns it recursively with depth 3
    """
    
    final_tx = []
    surpassed = []
    for tx in all_tx:
        final_tx.append(tx)

    for tx in all_tx:
        if tx['sender'] != data['address'] and tx['sender'] not in surpassed :
            print(tx['sender'])
            surpassed.append(tx['sender'])
            new_data = address_scraper(tx['sender'])
            try:
                new_txs = tx_extractor(new_data)
            except:
                pass
            for tx in new_txs:
                final_tx.append(tx)
        if tx['receiver'] != data['address'] and tx['receiver'] not in surpassed:
            print(tx['receiver'])
            surpassed.append(tx['receiver'])
            new_data = address_scraper(tx['receiver'])
            try:
                new_txs = tx_extractor(new_data)
            except:
                pass
            for tx in new_txs:
                final_tx.append(tx)
    return final_tx


def depth3_list(
    data: Dict,
    all_tx: list,

) -> list:
    """
    Takes as argument the list of transactions from tx_extractor function and returns it recursively with depth 3
    """
    
    final_tx = []
    surpassed = []
    for tx in all_tx:
        final_tx.append(tx)

    for tx in all_tx:
        if tx['sender'] != data['address'] and tx['sender'] not in surpassed :
            print(tx['sender'])
            surpassed.append(tx['sender'])
            new_data = address_scraper(tx['sender'])
            try:
                new_txs = tx_extractor(new_data)
            except:
                pass
            for tx in new_txs:
                final_tx.append(tx)
        if tx['receiver'] != data['address'] and tx['receiver'] not in surpassed:
            print(tx['receiver'])
            surpassed.append(tx['receiver'])
            new_data = address_scraper(tx['receiver'])
            
            for tx in new_txs:
                final_tx.append(tx)
    return final_tx
    

