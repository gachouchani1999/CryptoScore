from typing import Dict
import urllib.request, json

def tx_scraper(
    crypto_addr,
) -> Dict:
    if crypto_addr[:2] == '0x':
        url = "https://api.blockcypher.com/v1/eth/main/addrs/" +crypto_addr
        
        
    else:
        url = "https://api.blockcypher.com/v1/btc/main/addrs/" +crypto_addr
        
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())  
    return data[:1000]

print(tx_scraper("0x00000000219ab540356cbb839cbe05303d7705fa"))

