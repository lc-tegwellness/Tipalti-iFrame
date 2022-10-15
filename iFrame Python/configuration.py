# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:07:07 2022

@author: pratik.khatwani
@author: pratik.khatwani
"""

#Private key found on APHUB. Administration -> Apps -> API Key
PayerName ="YOUR-PAYER-NAME"
api_key = "YOUR-API-KEY"

#Sandbox URLs
paymentsetup_url = "https://ui2.sandbox.tipalti.com/payeedashboard/home?"
paymenthistory_url = "https://ui2.sandbox.tipalti.com/PayeeDashboard/PaymentsHistory?"
invoicehistory_url = "https://ui2.sandbox.tipalti.com/PayeeDashboard/Invoices?"

#Production URLs
#paymentsetup_url = "ui2.tipalti.com/payeedashboard/home?"
#paymenthistory_url = "ui2.tipalti.com/PayeeDashboard/PaymentsHistory?"
#invoicehistory_url = "ui2.tipalti.com/PayeeDashboard/Invoices?"

htmlstart = """<!DOCTYPE html>
    <html>
    <head>
    </head>
    <style type="text/css">
        html {
            overflow: auto;
        }
         
        html,
        body,
        div,
        iframe {
            margin: 0px;
            padding: 0px;
            height: 130%;
            margin-bottom: 0.01em;
            border: none;
        }
         
        iframe {
            display: block;
            width: 100%;
            border: none;
            overflow-y: auto;
            overflow-x: hidden;
        }
    </style>

    <body>

    <iframe src="
    """

htmlend="""
            " frameborder="0"
            marginheight="0"
            marginwidth="0"
            width="100%"
            height="100%"
            scrolling="yes"


    ></iframe>

    </body>
    </html>"""
