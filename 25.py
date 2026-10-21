x, y, n=map(int, input().split())
a=(x*100+y)*n
R=a//100
K=a%100
print(R,"руб.",K, "коп.")