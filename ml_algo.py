import pandas as pd
import random
import json
import tx_scraper
import tx_analyzer





with open('Fraud.txt') as f:
  bad_addrs = json.load(f)

sample_bad_addrs = [random.choice(bad_addrs) for i in range(1000)]


def prepare_training(addrs :list):
    """Uses random addresses to get arrays to feed to Classifier ML Algorithm"""
    practice_list = []
    for addr in addrs:
        data = tx_scraper.address_scraper(addr)
        basic_data = tx_scraper.basic_extractor(data)
        data = tx_scraper.address_scraper('bc1qejavv9dtk63ywt8t99tx6nm4cn9xszge7tagn2')
        tx_list = tx_scraper.tx_extractor(data)
        tx_lst2 = tx_scraper.depth2_list(data,tx_list)
        tx_lst3 = tx_scraper.depth3_list(data,tx_lst2)
        g = tx_analyzer.create_Graph(tx_lst3)
        practice = tx_analyzer.analysis_criteria(g,tx_lst3,basic_data)
        practice_list.append(practice)
    df = pd.DataFrame(practice_list)
    
    df.to_csv('practice.csv')
    
prepare_training(sample_bad_addrs)