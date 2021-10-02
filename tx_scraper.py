from typing import Dict
import urllib.request, json

def address_scraper(
    crypto_addr,
) -> Dict:
    """
    Extracts the wallet from the BlockCypher API
    """
    if crypto_addr[:2] == '0x':
        url = "https://api.blockcypher.com/v1/eth/main/addrs/" +crypto_addr
        
        
    else:
        url = "https://api.blockcypher.com/v1/btc/main/addrs/" +crypto_addr
        
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


#Testing
data = address_scraper("0xc711df3edca3cccc375c18273780aa7dcd72f6e7")
print(basic_extractor(data))



def tx_extractor (
    data: Dict,
) -> list:

    """
    Returns list of transactions
    tx_data format:
    in/out: Whether transaction was sent or received
    """

    all_tx = []
    
    tx_arr = data["txrefs"]
    for tx in tx_arr:
        tx_data = {}
        if tx["tx_input_n"] == "0":
            tx_data["mode"] = "in"
        else:
             tx_data["mode"] = "out"
        tx_data['hash'] = tx["tx_hash"]
        tx_data['value'] = tx['value']
        url = "https://api.blockcypher.com/v1/eth/main/txs/" + tx_data["hash"]
        url = "https://api.blockcypher.com/v1/bth/main/txs/" + tx_data["hash"]


        all_tx.append(tx_data)




    
