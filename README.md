# Tipalti-iFrame
Python to generate the Tipalti iFrame
## Installation
#
#### For [Python 3.8.8](https://www.python.org/)


## Dependencies

* Python
* [requests](https://pypi.org/project/requests/)

## Getting Started (configuration.py)
  ```python
  #Private key found on APHUB. Administration -> Apps -> API Key
  PayerName ="YOUR-PAYER-NAME"
  api_key = "YOUR_PRIVATE_APIKEY"

  #Sandbox URLs
  paymentsetup_url = "https://ui2.sandbox.tipalti.com/payeedashboard/home?"
  paymenthistory_url = "https://ui2.sandbox.tipalti.com/PayeeDashboard/PaymentsHistory?"
  invoicehistory_url = "https://ui2.sandbox.tipalti.com/PayeeDashboard/Invoices?"

  #Production URLs
  #paymentsetup_url = "ui2.tipalti.com/payeedashboard/home?"
  #paymenthistory_url = "ui2.tipalti.com/PayeeDashboard/PaymentsHistory?"
  #invoicehistory_url = "ui2.tipalti.com/PayeeDashboard/Invoices?"
  ```

## Documentation for iFrame

* iFrame Authentication: https://support.tipalti.com/Content/Topics/Development/iFrames/IframeAuthentication.htm
* Using iFrame URLs: https://support.tipalti.com/Content/Topics/Development/iFrames/UseTipaltiIframeUrls.htm
* iFrame Error Codes: https://support.tipalti.com/Content/Topics/Development/iFrames/IframeErrorCodes.htm

## Using the BAT file
* Ensure Python is installed
* Update the directory inside the bat file
  * 1. Update the Python Path where it is installed
  * 2. Update the Python path where the file resides on your machine
  
