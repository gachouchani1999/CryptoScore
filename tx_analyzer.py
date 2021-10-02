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

data = tx_scraper.address_scraper('bc1quctskkzeh0kfd93hrzns0jwg3gj35fvneqspr43c4wfxddwnx2qq5yeutp')
tx_list = tx_scraper.tx_extractor(data)
tx_lst3 = tx_scraper.depth3_list(data,tx_list)
g = create_Graph(tx_lst3)
print(g)



    
    
