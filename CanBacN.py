z=int(input("căn bậc = "))
m=int(input("Số = "))
def can_bac_n(x, n):
    
    if n == 0:
        raise ValueError("Căn bậc 0 không xác định.")
    if n < 0 and x >= 0:
        raise ValueError("Không thể tính căn bậc âm của số dương.")
    return x ** (1/n)

a = can_bac_n(m, z)
print(f"căn bậc {z} của {m}= {a}")  
