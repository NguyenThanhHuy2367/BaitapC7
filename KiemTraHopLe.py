# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 22:06:15 2024

@author: NGUYEN THANH HUY
"""

def kiemtra():
    while True:
        a = float(input("Nhập giá trị (trong khoảng [-89, 90]): "))
        if -89 <= a <= 90:
            print("hợp lệ:", a)
            break
        else:
            print(" không hợp lệ, vui lòng nhập lại.")
kiemtra()