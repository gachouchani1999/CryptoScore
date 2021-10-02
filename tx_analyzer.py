from typing import Dict
import tx_scraper

def create_Graph(
    lst: list, #Hash - Value - Sender - Receiver
) -> Dict:
    """
    Creates a weighted directed graph from a list of transactions
    """
    Graph = {}
    for tx in (lst):
        if tx['sender'] in Graph:
            if tx["receiver"] in Graph[tx['sender']]:
                Graph[tx["sender"]][tx["receiver"]] +=1
            else:
                Graph[tx["sender"]][tx["receiver"]] = 1
        else:
            Graph[tx["sender"]] = {tx["receiver"]: 1}
    return Graph

data = tx_scraper.address_scraper('0xbe0eb53f46cd790cd13851d5eff43d12404d33e8')
tx_list = tx_scraper.tx_extractor(data)
g = create_Graph(tx_list)
print(g)



    
    
