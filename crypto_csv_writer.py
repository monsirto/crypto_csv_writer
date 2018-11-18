#! /usr/bin/python3
# https://www.roboshout.com
# Scrape coinmarketcap.com's historical cryptocurrency datasets.
# Write date, open, high, low, close, volume, & market capacity
# to .csv in current directory. ex: bitcoin20181120.csv
# Data for a given currency will be written to the .csv file
# from April 28, 2013 to the current date
# 2018 James Loye Colley
# usage: python3 -c bitcoin
#
import requests
import argparse
from datetime import datetime
from sys import exit
import re
import csv


class CryptoCSV:
    def __init__(self, currency_type):
        self.today = datetime.now().strftime("%Y%m%d")
        self.currency = currency_type
        self.matches = ''
        self.__build_url()

    def __build_url(self):
        self.url = "https://coinmarketcap.com/currencies/"
        self.url += self.currency
        self.url += "/historical-data/?start=20130428&end="
        self.url += self.today

    def __search_regex(self):
        req = requests.get(self.url)
        reg_str = "<td.*\w+.*</td>"
        self.matches = re.findall(reg_str, req.text)

    def __get_data(self):
        csv_row = []
        for td_tag in self.matches:
            regex = ">(.*)<"
            match = re.search(regex, td_tag)
            if match:
                if not match.group(1)[:3].isalpha():
                    csv_row.append(match.group(1))
                else:
                    copy = csv_row[:]
                    csv_row = [match.group(1)]
                    yield copy

    def create_csv(self):
        self.__search_regex()
        meta_data = [
            "date", "open", "high", "low",
            "close", "volume", "mkt_cap"
        ]
        file_name = self.currency + self.today + ".csv"
        with open(file_name, "w") as csv_file:
            writer = csv.writer(csv_file, delimiter='\t')
            writer.writerow(meta_data)
            for line in self.__get_data():
                writer.writerow(line)


if __name__ == "__main__":
    valid_currenies = [
        "bitcoin", "litecoin", "ripple", "ethereum",
        "bitcoin-cash", "reddcoin", "stellar", "eos",
        "cardano", "monero", "tron", "iota", "dash",
        "factom", "nem", "neo", "ethereum-classic",
        "tezos", "zcash", "bitcoin-gold", "ark", "vechain",
        "ontology", "dogecoin", "decred", "qtum", "lisk",
        "bytecoin", "bitcoin-diamond", "bytecoin", "icon",
        "bitshares", "nano", "digibyte", "siacoin", "steem",
        "bytom", "waves", "metaverse", "verge", "stratis",
        "electroneum", "komodo", "cryptonex", "ardor",
        "wanchain", "monacoin", "moac", "pivx", "horizen",
        "ravencoin", "gxchain", "huobi-token"
    ]
    message = 'Enter a currency type'
    parser = argparse.ArgumentParser(description='-c currency name argument')
    parser.add_argument('-c', '--currency', required=True, help=message)
    currency_arg = vars(parser.parse_args())
    if currency_arg['currency'] not in valid_currenies:
        print("Please enter a valid cryptocurrency...")
        exit()
    CryptoCSV(currency_arg['currency']).create_csv()
