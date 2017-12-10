#!/usr/bin/python

import cgi
import cgitb
import urllib
from lxml import html
from controllerHargaPangan import hargaPangan

cgitb.enable()
print("Content-type:text/html; charset=UTF-8")
print("\n")
form = cgi.FieldStorage()

nomorHape = form.getvalue('nomor_hape')
jenisPangan = form.getvalue('nama_pangan')

hargaPangan = hargaPangan()
if (jenisPangan == 'Semua'):
    # print("haha")
    # print(nomorHape)
    # print(jenisPangan)
    print(hargaPangan.sendToNumber(nomorHape, hargaPangan.getHargaPanganAll(), hargaPangan.getToken()))
    # print(hargaPangan.getToken())
    # print(hargaPangan.sendToNumber(nomorHape, 'hehehehehehe', hargaPangan.getToken()))

else:
    # print("hihi")
    # print(nomorHape)
    # print(jenisPangan)
    # print(hargaPangan.sendToNumber(nomorHape, hargaPangan.getSalahSatuHargaPangan(jenisPangan)))
    # print('nothing')
    # print(hargaPangan.getSalahSatuHargaPangan(jenisPangan))
    print(hargaPangan.sendToNumber(nomorHape, hargaPangan.getSalahSatuHargaPangan(jenisPangan), hargaPangan.getToken()))