BTC Top 100

This program is a Python script that retrieves the top 100 Bitcoin addresses associated with a specific address.



This program requires the requests library, which can be installed with 

$ pip install requests


To use the program, run the following command in your terminal:

$ python3 btc_top_100.py

The program will prompt you to enter the address for which you want to retrieve the top 100 associated addresses. Once you have entered the address, the program will retrieve the list of transactions associated with the address, extract the addresses associated with each transaction, count the number of transactions associated with each address, sort the addresses by the number of transactions, and return the top 100 addresses. The addresses and their associated transaction count will be printed to the terminal.
