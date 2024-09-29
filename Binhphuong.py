# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:59:43 2024

@author: NGUYEN THANH HUY
"""
a=int(input("Nhập số = "))
def binhphuong(n):
    if n > 0:
        return n ** 2
    else:
        return "Vui lòng nhập một số dương"
ket_qua = binhphuong(a)
print(ket_qua)
