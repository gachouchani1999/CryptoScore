import pandas as pd
import random
import json
import tx_scraper
import tx_analyzer
from csv import writer
  

  






with open('Fraud.txt') as f:
  bad_addrs = json.load(f)

sample_bad_addrs = [random.choice(bad_addrs) for i in range(100)]

with open('legends.txt') as f:
    pos_addrs = f.readlines()
    for pos_addr in pos_addrs:
        pos_addr = pos_addr[2:]
    

sample_pos_addrs = [random.choice(pos_addrs) for i in range(100)]


def prepare_training_negative(addrs :list):
    """Uses random negative addresses to get arrays to feed to Classifier ML Algorithm"""
    practice_list = []
    for addr in addrs:
        try:
            data = tx_scraper.address_scraper(addr)
        except:
            pass
        basic_data = tx_scraper.basic_extractor(data)
        try:
            tx_list = tx_scraper.tx_extractor(data)
        except:
            pass
        tx_lst2 = tx_scraper.depth2_list(data,tx_list)
        tx_lst3 = tx_scraper.depth3_list(data,tx_lst2)

        g = tx_analyzer.create_Graph(tx_lst3)
        practice = tx_analyzer.analysis_criteria(g,tx_lst3,basic_data)
        practice.append(0)
        if practice != [0,0,0,0,0,0,0,0,0]:
            with open('training.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(practice)
                f_object.close()
    
    
    
prepare_training_negative(sample_bad_addrs[:10])

def prepare_training_positive(addrs :list):
    """Uses random addresses to get arrays to feed to Classifier ML Algorithm"""
    practice_list = []
    for addr in addrs:
        try:
            data = tx_scraper.address_scraper(addr)
        except:
            pass
        basic_data = tx_scraper.basic_extractor(data)
        try:
            tx_list = tx_scraper.tx_extractor(data)
        except:
            pass
        tx_lst2 = tx_scraper.depth2_list(data,tx_list)
        tx_lst3 = tx_scraper.depth3_list(data,tx_lst2)

        g = tx_analyzer.create_Graph(tx_lst3)
        practice = tx_analyzer.analysis_criteria(g,tx_lst3,basic_data)
        practice.append(1)
        if practice != [0,0,0,0,0,0,0,0,1]:
            with open('training.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(practice)
                f_object.close()
    
    
    
prepare_training_positive(sample_pos_addrs[:10])