# CryptoScore
## Inspiration
In a future where cryptocurrency is inevitable, it still lacks on main component: trust. Trust that banks took decades to build with their customers, that could be taken away in a second. In a world of anonymity, where no one wants to be known, it is harder to trust than ever. The main question lies: to make cryptocurrency used officially around the world, how can we make people trust each other? How can we trust that the person behind the Bitcoin address is not here to scam us? How can we trust that both sides of the transaction will be satisfied? 
Humans have shown to be sometimes too irrational to have a decision in that matter. This is where CryptoScore comes into the story. CryptoScore aims to build trust among addresses rather than people and let updated algorithms decide whether an address is reliable or not based on machine learning algorithms that analyze its transactions on the blockchain.
## What it does
CryptoScore takes as an input an address and returns a score over 100 that represents how much the address is reliable to have a transaction with. CryptoScore is made up of 6 parts: An address analyzer, a transaction analyzer, a directed cyclic graph, a criteria creator, the algorithm trainer and finally the machine learning algorithm. 
## How we built it
To discuss how we built it we need to explain each part in details:
## Address Analyzer
The Address Analyzer function was built using the BlockCypher API that allows the function to receive a JSON file that the function can analyze to scrape the address, the transactions list, the balance and how many transactions they are. 
## Transaction Analyzer 
The transaction analyzer function takes as an input the data extracted from the address analyzer function and returns the transactions in a list that takes the most important data that we need for analysis, including sender and receiver, value of transaction.
The transaction list is then put into another function that expands to find the transactions of the wallets the initial wallet interacted with. This creates a list of transactions of depth 2.
This function then iterates one more time to find the list of transactions for the addresses that the addresses from the depth 2 function iterates with.
This creates a list of transactions of depth 3 which is enough to find cycles in transactions and erratic behaviors from multiple wallets.
#Directed Weighted Graph
We then wrote a function that takes as input the list of depth 3 of transactions and creates a weighted directed graph using DFS algorithms. This graph allows to search for cycles in transactions, repeated transactions, number of sender addresses in pump and dump schemes and also in extortion schemes. 
# Criteria Creator
Then the directed graph is fed to a function that searches for different criteria from the graph and returns an array with the different criteria to feed the ML model.
## Machine Learning Training
This array is then fed to a machine Learning algorithm using Scikit-learn KNN classification model, and we save this model into a file that is then called when the algorithm is called in the Frontend.
## Machine Learning Algorithm
The main algorithm that is used in the website that returns a score for a certain wallet based on the previous training done for the algorithm.
## Challenges we ran into
The main challenge we ran into is that the BlockCypher API had a very slow request rate which made training the algorithm tiresome, around 4 hours while working on other stuff, and the connection in Lebanon (where 2 team members reside) was very slow that led for the API to lead to 404s.
## Accomplishments that we're proud of
We are very proud of the algorithms we built that had a very good running time for their complexity since we used O(n log n) algorithms such as merge sort, DFS for graph traveling and others that we came up with.
## What we learned
We learned that sometimes using APIs have its limitations and that outside of the scope of the hackathon, with a longer deadline we should build or purchase higher limits to be able to have all the data we need in the least amount of time to increase user experience.
Also we have learnt that sometimes if the average runtime for an algorithm is good does not mean we need to use it if our data is a best case scenario, we can just use the best case.
## What's next for CryptoScore
The next step is to create deep learning algorithms using Neural Networks and PyTorch for the algorithms to run a graph of depth 5 to 10 instead of a depth 3 which allows the algorithm to find more fraudulent activity.
## Limits
Due to the limits of the API BlockCypher if you run the code and an error occurs then the API reached a maximum limit of requests (which is a very low limit) then go visit BlockCypher to get an API and replace it in tx_scraper.py to test the code yourselves. In a production environment, we would pay for way increased limits to use.
