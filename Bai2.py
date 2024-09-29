# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:06:12 2024

@author: NGUYEN THANH HUY
"""
a=int(input("Nhập cạnh hình vuông="))
b=int(input("Nhập chiều dài hình chữ nhật="))
c=int(input("Nhập chiều rộng hình chữ nhật   ="))
d=int(input("Nhập bán kính hình tròn="))
print("=========")
def tinh_chu_vi(*args, **kwargs):
    if 'hinh' in kwargs:
        hinh = kwargs['hinh']
        if hinh == 'hinh_vuong':
            return 4 * args[0]
        elif hinh == 'hinh_chu_nhat':
            return 2 * (args[0] + args[1])
        elif hinh == 'hinh_tron':
            return 2 * 3.14 * args[0]
    return None
chu_vi_hinh_vuong = tinh_chu_vi(a, hinh='hinh_vuong')
print(f"Chu vi hình vuông: {chu_vi_hinh_vuong}")
chu_vi_hinh_chu_nhat = tinh_chu_vi(b, c, hinh='hinh_chu_nhat')
print(f"Chu vi hình chữ nhật: {chu_vi_hinh_chu_nhat}")
chu_vi_hinh_tron = tinh_chu_vi(d, hinh='hinh_tron')
print(f"Chu vi hình tròn: {chu_vi_hinh_tron}")