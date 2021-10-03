import pandas as pd
import random
import json
import tx_scraper
import tx_analyzer

  

  







with open('Fraud.txt') as f:
  bad_addrs = json.load(f)

sample_bad_addrs = [random.choice(bad_addrs) for i in range(100)]

with open('legends.txt') as f:
    pos_addrs = f.readlines()
    for i,pos_addr in enumerate(pos_addrs):
        pos_addr = pos_addr[pos_addr.find('\t')+1:pos_addr.find('\n')]
        pos_addr = pos_addr[:pos_addr.find('\t')+1]
        pos_addrs[i] = pos_addr


    

sample_pos_addrs = [random.choice(pos_addrs) for i in range(100)]


def prepare_training_negative(addrs :list):
    """Uses random negative addresses to get arrays to feed to Classifier ML Algorithm"""
    with open('training.csv', 'a+') as f:
        for addr in addrs:
            print("I am in 1")
            data = tx_scraper.address_scraper(addr)
            basic_data = tx_scraper.basic_extractor(data)
            try:
                tx_list = tx_scraper.tx_extractor(data)
            except:
                continue
            tx_lst2 = tx_scraper.depth2_list(data,tx_list)
            tx_lst3 = tx_scraper.depth3_list(data,tx_lst2)

            g = tx_analyzer.create_Graph(tx_lst3)
            practice = tx_analyzer.analysis_criteria(g,tx_lst3,basic_data)
            practice.append(0)
            print("I am in 2!")
            if practice != [0,0,0,0,0,0,0,0,0]:
                
                    for line in f:
                        f.write(practice)
            print("I am h")
    
    
prepare_training_negative(sample_bad_addrs)


def prepare_training_positive(addrs :list):
    """Uses random addresses to get arrays to feed to Classifier ML Algorithm"""
    practice_list = []
    for addr in addrs:
        data = tx_scraper.address_scraper(addr)

        basic_data = tx_scraper.basic_extractor(data)
        try:
            tx_list = tx_scraper.tx_extractor(data)
        except:
            continue
        tx_lst2 = tx_scraper.depth2_list(data,tx_list)
        tx_lst3 = tx_scraper.depth3_list(data,tx_lst2)

        g = tx_analyzer.create_Graph(tx_lst3)
        practice = tx_analyzer.analysis_criteria(g,tx_lst3,basic_data)
        practice.append(1)
        print("I am here")
        if practice not in [0,0,0,0,0,0,0,0,1]:
            with open('training.csv', 'a') as f:
                for line in f:
                    f.write(practice)
                
                
    
    
    
prepare_training_positive(sample_pos_addrs[:10])