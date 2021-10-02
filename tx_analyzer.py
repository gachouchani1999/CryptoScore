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

data = tx_scraper.address_scraper('1Di7HSRy3T8YbczYv4Q8Pr2VbppgZf3iUY')
tx_list = tx_scraper.tx_extractor(data)

tx_lst2 = tx_scraper.depth2_list(data,tx_list)
tx_lst3 = tx_scraper.depth3_list(data,tx_lst2)

g = create_Graph(tx_lst3)
print(g)



    
    
