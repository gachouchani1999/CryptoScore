from typing import Dict

import json
import tx_scraper
import exchange_wallets
from merge_sort import merge_sort

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

#Testing purposes
'''data = tx_scraper.address_scraper('bc1qejavv9dtk63ywt8t99tx6nm4cn9xszge7tagn2')
tx_list = tx_scraper.tx_extractor(data)

tx_lst2 = tx_scraper.depth2_list(data,tx_list)
tx_lst3 = tx_scraper.depth3_list(data,tx_lst2)
basic_data = tx_scraper.basic_extractor(data)
g = create_Graph(tx_lst3)'''


def analysis_criteria(
    g: Dict,
    all_txs: list,
    basic_data : list,
) -> list:
    """
    This function takes as input the directed cyclic graph and creates an array of values that will be fed for the ML algorithm to train.
    Array Values:
    [0]: 1 if there is sender in fraudulent wallets/ 0 if not
    [1]: number of senders in trusted wallets
    [2]: Returns number of senders in graph
    [3]: Returns average number of recievers for each sender in graph
    [4]: Average weight of transactions between senders and receivers
    [5]: Is there a cycle in blockchain transactions? 1 if YES / 0 if NO
    [6]: Is there a sum of values sent in the blockchain that sum up to another value?
    [7]: Total amount sent/ Total amount received
    """
    analysis_arr = [0,0,0,0,0,0,0,0] #7 criteria
    with open('Fraud.txt') as f:
        fraudulent_wallets = json.load(f)
    for sender in g:
        if sender in fraudulent_wallets:
            analysis_arr[0] = 1

        if sender in exchange_wallets.most_trusted_wallet:
            analysis_arr[1] += 1
        

    analysis_arr[2] = len(g)

    total_receivers = 0
    for dic in g.values():
        total_receivers += len(dic)

    try:
        analysis_arr[3] = (total_receivers/analysis_arr[2])
    except:
        analysis_arr[3] = 0

    total_weights = 0
    for receiver in g.values():
        for value in receiver.values():
            total_weights += value
    try:   
        analysis_arr[4] = (total_weights/analysis_arr[3])
    except:
        analysis_arr[4] =0

    for sender in g: 
        for receiver in g.values():
            if sender in receiver:
                analysis_arr[5] = 1
    
    values = [tx["value"] for tx in all_txs]
    merge_sort(values)
    sum = 0
    #Could Probably enhance function 
    for value in values:
        sum += value
        if sum == values[len(values)-1]:
            analysis_arr[6] = 1
        elif sum == values[len(values)-2]:
            analysis_arr[6] = 1
    try:
        analysis_arr[7] = basic_data[1]/basic_data[0]
    except:
        analysis_arr[7] = 0

    return analysis_arr


