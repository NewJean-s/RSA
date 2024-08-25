def gcd(n1,n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1

def get_public_key(theta):
    e = 2
    while e < theta and gcd(e,theta) != 1:
        e += 1
    return e

def get_private_key(e, theta):
    k = 1
    while (e * k) % theta != 1 or k == e:
        k += 1
    return k

p = 13
q = 29
#README.md의 조건에 따라서 p,q는 변경 가능

n = p * q
theta = (p-1)*(q-1)
e = get_public_key(theta)
d = get_private_key(e, theta)

print(f"공개 키 : {e}\n")
print(f"비공개 키 : {d}\n")

while True:
  select = int(input("암호화(0) 또는 복호화(1)\n> "))
  
  if select == 0:
    pwd = input("암호화 할 문자열을 입력\n> ")
    arr = []
    result = ""

    for i in pwd:
      M = ord(i)
      C = (M**e) % n
      arr.append(str(C))

    print(f"\n결과 : {arr}\n")
  else:
    pwd = input("복호화 할 문자열을 입력\n> ")
    arr = []
    result = ""

    for i in pwd:
      arr.append(ord(i))

    for i in arr:
      result += chr((i**d)%n)

    print(f"\n결과 : {result}\n")
