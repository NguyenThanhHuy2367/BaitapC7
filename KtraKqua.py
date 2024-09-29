# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 22:03:33 2024

@author: NGUYEN THANH HUY
"""
a = int(input("Nhập một số: "))
def kiem_tra_so(n):
    if a < 0 and a % 2 != 0:
        return -1
    elif a > 0 and a % 2 == 0:
        return 1
    else:
        return 0
b = kiem_tra_so(a)
print("Kết quả:", b)