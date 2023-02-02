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

def getPaymentSetupURL(idap,ts,hashkey,para_str):
    paymentsetup = """{url}payer={payer}&idap={idap}&ts={ts2}{para_str}&hashkey={hashkey}""".format(url=str(configuration.paymentsetup_url), idap = str(idap), payer = str(payer), ts2=str(ts), hashkey = str(hashkey), para_str = str(para_str))
    return paymentsetup

def getPaymentHistoryURL(idap,ts,hashkey,para_str):
    paymenthistory = """{url}payer={payer}&idap={idap}&ts={ts2}{para_str}&hashkey={hashkey}""".format(url = str(configuration.paymenthistory_url), idap = str(idap), payer = str(payer), ts2=str(ts), hashkey = str(hashkey), para_str = str(para_str))
    return paymenthistory

def getInvoiceHistoryURL(idap,ts,hashkey,para_str):
    invoiceshistory = """{url}payer={payer}&idap={idap}&ts={ts2}{para_str}&hashkey={hashkey}""".format(url = str(configuration.invoicehistory_url), idap = str(idap), payer = str(payer), ts2=str(ts), hashkey = str(hashkey), para_str = str(para_str))
    return invoiceshistory

def iframe(idap, payer, ts, hashkey, selection,para_str):
    error=0
    paymentsetup = getPaymentSetupURL(idap, ts, hashkey, para_str)
    paymenthistory = getPaymentHistoryURL(idap, ts, hashkey, para_str)
    invoiceshistory = getInvoiceHistoryURL(idap, ts, hashkey, para_str)
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
    selection = input("""
                      1. Payment Setup (Parameters allowed)
                      2. Payments History
                      3. Invoices History 
                      
                      Please select a type: Enter 1 or 2 or 3
                      """)
    
    parameters = ["1.First Name","2.Last Name","3.Company Name","4.Email","5.Payer Entity","6.Payee Type","7.Payee Erp Currency"]
    para =""
    first=""
    last=""
    company=""
    email=""
    preferredPayerEntity=""
    payeeErpCurrency=""
    payeeType=""
    para_str = ""
    valid=1
    if selection == '1':
        sel_parameters = input("\n Do you wish to add any parameters?\n 1.Yes\t 2.No\n")
        if sel_parameters == '1':
            print("\n", parameters)
            para = input("Please enter your parameter choices.\n Example. For First Name, Last Name and Email, enter 124\n")
            for i in range(len(para)):
                if para[i]>'7': 
                    print("invalid selection")
                    valid=0
                    break
            if valid==1:
                for i in range(len(para)):
                    if para[i]=='1':
                        first = input("\n Enter First Name \n")
                        para_str = para_str+"&first="+first
                    elif para[i]=='2':
                        last = input ("\n Enter Last Name \n")
                        para_str = para_str+"&last="+last
                    elif para[i]=='3':
                        company = input ("\n Enter Company Name \n")
                        para_str = para_str+"&company="+company
                    elif para[i]=='4':
                        email = input ("\n Enter Email \n")
                        para_str = para_str+"&email="+email
                    elif para[i]=='5':
                        preferredPayerEntity = input ("\n Enter Entity \n")
                        para_str = para_str+"&preferredPayerEntity="+preferredPayerEntity
                    elif para[i]=='6':
                        payeeType = input ("\n Enter Individual or Company \n")
                        para_str = para_str+"&payeeType="+payeeType
                    elif para[i]=='7':
                        payeeErpCurrency = input ("\n Enter ERP Currency \n")
                        para_str = para_str+"&payeeErpCurrency="+payeeErpCurrency
                    else:
                        print("invalid selection")
    
    #payer = input('Please type in payer name: ')
    if selection=='1':
        para_str = para_str.replace(' ','%20')
        msgiframe = 'payer=' + payer+ '&idap=' + idap +'&ts=' + str(ts) + para_str
    else:
        msgiframe = 'payer=' + payer+ '&idap=' + idap +'&ts=' + str(ts)
    hashkey = keymaker(msgiframe, api_key)
    iframe(idap, payer, ts, hashkey, selection, para_str)

if __name__ == "__main__":
    main()
