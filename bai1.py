"""
Created on Sun Sep 29 20:11:51 2024

@author: NGUYEN THANH HUY
"""

def tich_tong(*args, **kwargs):
    a = sum(args)
    b = 1
    for i in args:
        b *= i
    return a, b
c, d = tich_tong(1, 2, 3, 4, 5)
print("tổng:", c)
print("tích:", d)