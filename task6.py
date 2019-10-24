stroka_1 = int(input())
stroka_2 = map(int, input().split())
stroka_3 = int(input())
stroka_4 = map(int, input().split())
x = set(stroka_2)
y = set(stroka_4)
a = x - y
b = y - x
rezult = a.union(b)
rezult = sorted(rezult)
print('\n'.join(map(str, rezult)))
