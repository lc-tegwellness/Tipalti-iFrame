"""
Created on Wed Jul 20 15:27:03 2022

@author: zachary.tanverakul//pratik.khatwani
"""

import hmac
import hashlib
import time
import configuration
payer = configuration.PayerName
api_key = configuration.api_key

def keymaker(msgiframe, secretkey):

    hashkey = hmac.new(bytes(secretkey, 'latin-1'), msg=bytes(msgiframe,'latin-1' ) , digestmod=hashlib.sha256).hexdigest()
    return hashkey

def getPaymentSetupURL(idap,ts,hashkey):
    paymentsetup = """{url}idap={idap}&payer={payer}&ts={ts2}&hashkey={hashkey}""".format(url=str(configuration.paymentsetup_url), idap = str(idap), payer = str(payer), ts2=str(ts), hashkey = str(hashkey))
    return paymentsetup

def getPaymentHistoryURL(idap,ts,hashkey):
    paymenthistory = """{url}idap={idap}&payer={payer}&ts={ts2}&hashkey={hashkey}""".format(url = str(configuration.paymenthistory_url), idap = str(idap), payer = str(payer), ts2=str(ts), hashkey = str(hashkey))
    return paymenthistory

def getInvoiceHistoryURL(idap,ts,hashkey):
    invoiceshistory = """{url}idap={idap}&payer={payer}&ts={ts2}&hashkey={hashkey}""".format(url = str(configuration.invoicehistory_url), idap = str(idap), payer = str(payer), ts2=str(ts), hashkey = str(hashkey))
    return invoiceshistory

def iframe(idap, payer, ts, hashkey, selection):
    error=0
    paymentsetup = getPaymentSetupURL(idap, ts, hashkey)
    paymenthistory = getPaymentHistoryURL(idap, ts, hashkey)
    invoiceshistory = getInvoiceHistoryURL(idap, ts, hashkey)
    #print(paymentsetup)
    #print(paymenthistory)
    #print(invoiceshistory)
    message = configuration.htmlstart
    end_message = configuration.htmlend
    if selection=='1':
        f = open('Setup_Demo.html','w+')
        f.write(message)
        f.write(paymentsetup)
        f.write(end_message)
        f2 = open('URL_paymentsetup.txt','w+')
        f2.write(paymentsetup)
        f2.close()
        print("URL for iFrame: ", paymentsetup)
    elif selection=='2':
        f = open('PaymentHistory_Demo.html','w+')
        f.write(message)
        f.write(paymenthistory)
        f.write(end_message)
        f2 = open('URL_Paymenthistory.txt','w+')
        f2.write(paymenthistory)
        f2.close()
        print("URL for iFrame: ", paymenthistory)
    elif selection=='3':
        f = open('InvoiceHistory_Demo.html','w+')
        f.write(message)
        f.write(invoiceshistory)
        f.write(end_message)
        f2 = open('URL_InvoiceHistory.txt','w+')
        f2.write(invoiceshistory)
        f2.close()
        print("URL for iFrame: ", invoiceshistory)
    else:
        f = open('error.txt','w+')
        f.write("Wrong selection, please select one of the options")
        error=1
    f.close()
    

def main():

    ts = int(time.time())

    idap = input('Please type in idap: ')

    #payer = input('Please type in payer name: ')
    selection = input("""
                      1. Payment Setup
                      2. Payments History
                      3. Invoices History 
                      
                      Please select a type: Enter 1 or 2 or 3
                      """)
    msgiframe = 'idap=' + idap + '&payer=' + payer +'&ts=' + str(ts)
    hashkey = keymaker(msgiframe, api_key)
    iframe(idap, payer, ts, hashkey, selection)

if __name__ == "__main__":
    main()
