import pandas as pd
import pathlib
import os
import yfinance as yf

ticker_info = ""
balance_sheet = ""
cash_flow = ""
earnings = ""

def data_call(ticker_name):
    #ticker_name = 'AAPL'
    ticker_data = yf.Ticker(ticker_name)
    global ticker_info, balance_sheet, cash_flow, earnings
    ticker_info = ticker_data.info
    balance_sheet = ticker_data.balancesheet
    cash_flow = ticker_data.cashflow
    earnings = ticker_data.earnings

    print(balance_sheet,cash_flow) #, ticker_data.recommendations)
    return ticker_data

def store_txt():
    #Create a text file and store Bussiness summary
    with open('Bussiness_info.txt', 'w') as f:
        f.write('Create a new text file! \n')
        #Bussiness info stored in a one line and not able to read
        #line by line. Adding \n after each fullpoint .
        modified_text = ticker_info['longBusinessSummary'].replace('Inc.', 'Inc').replace('.','.\n')
        f.write(modified_text)
    with open ('Bussiness_info.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
        #print(lines)

def balance_sheet_to_csv():
    #global balance_sheet
    balance_sheet.to_csv('balance.csv')



if __name__ == "__main__":
    data_call('AAPL')
    #store_txt()
    #balance_sheet_to_csv()