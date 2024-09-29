# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 20:54:08 2024


@author: NGUYEN THANH HUY
"""
a=int(input("Nhập cạnh hình vuông="))
b=int(input("Nhập chiều dài hình chữ nhật="))
c=int(input("Nhập chiều rộng hình chữ nhâtj ="))
d=int(input("Nhập bán kính hình tròn="))
print("=========")
import math

def tinh_dien_tich(*s, **z): #s là args, z là kwargs
    hinh = z.get('hinh', None)
    if hinh == 'hinh_vuong':
        canh = s[0]
        return canh ** 2
    elif hinh == 'hinh_chu_nhat':
        dai, rong = s
        return dai * rong
    elif hinh == 'hinh_tron':
        r = s[0]
        return math.pi * r ** 2
    else:
        return "Hình không hợp lệ"
dien_tich = tinh_dien_tich(a, hinh='hinh_vuong')
print("Diện tích hình vuông:", dien_tich)

dien_tich = tinh_dien_tich(b, c, hinh='hinh_chu_nhat')
print("Diện tích hình chữ nhật:", dien_tich)
dien_tich = tinh_dien_tich(d, hinh='hinh_tron')
print("Diện tích hình tròn:", round(dien_tich,2))