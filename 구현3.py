a=input()

col = int(a[1])                 #행
raw = ord(a[0])-ord('a')+1      #열(a,b,c,d---를 숫자로 변환)

night = [col, raw]

move_type=[(2, 1), (2, -1), (1, 2), (-1, 2), (-2,-1),(-2,1), (-1,-2), (1, -2)]
cnt = 0

for moves in move_type  :
    if (1<=col + moves[0]<= 8) and (1<=raw + moves[1] <=8)  :
        cnt+=1

print(cnt)

