n=1260
cnt = 0

coin = [500, 100, 50, 10]

for coins in coin :
   cnt +=n//coins
   n%=coins

print(cnt)