num=11
dec=0
base=1
while num>0:
    rem=num%10
    dec=dec+rem*base
    num=num//10
    base=base*2
print(dec)