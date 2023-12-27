n=[5, 3, 4, 6, 2]
p=sorted(n)
mi=p[0]
n.remove(p[-1])
for i in n:
    if i==mi:
        n.remove(i)
print(sum(n)//len(n))
#
