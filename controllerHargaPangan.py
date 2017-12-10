#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import cgi
import cgitb
import urllib
from lxml import html
import requests
import pycurl
import json
from io import BytesIO

class hargaPangan:
    def getHargaPanganAll(self):
        data = ""
        browser = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
        browser.get("https://ews.kemendag.go.id/")
        html_source = browser.page_source
        try:
            tree = html.fromstring(html_source)
            tdx = tree.xpath('//div[@id="ctl00_contentMain_upMaps"]/div[@class="col-lg-12 sp2kplistpasarblock"]/div[@class="container"]/div[@class="row"]/div[@class="col-lg-3 tglharganasional"]/div[@id="nasionalitem"]/div/table/tbody/tr/td/text()')
            browser.quit()
            # print(tdx)
            for j in range(0, len(tdx)):
                if (tdx[j] == 'Kg') or (tdx[j] == 'Lt') or (tdx[j] == 'Gr') or (tdx[j] == 'Bks'):
                    data = data + "Komoditas " + tdx[j - 3] + " Harga saat ini Rp. " + tdx[j - 1] + " /" + tdx[j] + ","
            return data
        except TimeoutException:
            return 'Loading took too much time!'

    def getSalahSatuHargaPangan(Self, namaPangan):
        data = ""
        browser = webdriver.PhantomJS(
            executable_path='/usr/local/bin/phantomjs')
        browser.get("https://ews.kemendag.go.id/")
        html_source = browser.page_source
        try:
            tree = html.fromstring(html_source)
            tdx = tree.xpath(
                '//div[@id="ctl00_contentMain_upMaps"]/div[@class="col-lg-12 sp2kplistpasarblock"]/div[@class="container"]/div[@class="row"]/div[@class="col-lg-3 tglharganasional"]/div[@id="nasionalitem"]/div/table/tbody/tr/td/text()')
            browser.quit()
            # print(tdx)
            for j in range(0, len(tdx)):
                if (tdx[j] == 'Kg') or (tdx[j] == 'Lt') or (tdx[j] == 'Gr') or (tdx[j] == 'Bks'):
                    if(namaPangan == tdx[j - 3]):
                        data = data + "Komoditas " + \
                            tdx[j - 3] + " Harga saat ini Rp. " + \
                            tdx[j - 1] + " /" + tdx[j] + "\n"
            return data
        except TimeoutException:
            return 'Loading took too much time!'

    def getToken(self):
        token_url = 'https://api.pometera.id/smsnotif/token'
        data = 'grant_type=client_credentials'
        dataReturn = BytesIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, token_url)
        c.setopt(pycurl.HTTPHEADER, [
            'X-Pometera-Api-Key: b925096d-d86f-4d29-b8ee-a39f49d66bd8', 'Content-Type: application/x-www-form-urlencoded'])
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.POSTFIELDS, data)
        c.setopt(c.WRITEFUNCTION, dataReturn.write)
        c.perform()
        foo = json.loads(dataReturn.getvalue())
        return foo['access_token']
        
    def sendToNumber(self, numberHandPhone, isiText, token):
        notification_sms_url = 'https://api.pometera.id/smsnotif/messages'
        dataMSISDN = 'msisdn='+numberHandPhone
        dataCONTENT = 'content='+isiText
        dataReturn = BytesIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, notification_sms_url)
        c.setopt(pycurl.HTTPHEADER, [
            'X-Pometera-Api-Key: b925096d-d86f-4d29-b8ee-a39f49d66bd8', 'Accept: application/json', 'Content-Type: application/x-www-form-urlencoded', 'Authorization: Bearer '+token])
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.POSTFIELDS, dataMSISDN + '\n' + dataCONTENT)
        # c.setopt(pycurl.POSTFIELDS, dataCONTENT)
        c.setopt(c.WRITEFUNCTION, dataReturn.write)
        c.perform()
        foo = json.loads(dataReturn.getvalue())
        # if foo['status'] == 'FAILED':
        #     return foo['message']
        # else:
        return foo['status']
        # return numberHandPhone + ' ' + isiText + ' ' + token 
