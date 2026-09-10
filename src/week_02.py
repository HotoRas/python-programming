print("Hello python") # Hello python

print("*"*10) # **********

print("??"*20) # ????????????????????????????????????????

print('I love Korea')
print('I'+' '+'love'+' '+'Korea')
print(" ".join(['I','love','Korea']))
print('I','love','Korea')
# I love Korea

tmp=['I','love','Korea','but','hate','Japan']
print(" ".join(tmp)) # I love Korea but hate Japan

print(list(range(1,5))) # [1, 2, 3, 4]

print(list(range(1,101))) # [1, 2, 3, 4, 5, 6, ..., 99, 100]

print(list(range(1,100,2))) # [1, 3, 5, 7, 9, ..., 95, 97]

print(len(list(range(3,100,3)))) # 33

print(list(range(99,10,-2))) # [99, 97, 95, ..., 13, 11]

tmp2=list(range(99,0,-3))
print(tmp2) # [99, 96, 93, 90, ..., 6, 3]
print(len(tmp2)) # 33

st1='http://www.ebs.co.kr//example.lec'
print(st1.split('/')) # ["http:", "", "www.ebs.co.kr", "", "example.lec"]
st2=st1.split('//')
print(st2) # ["http:", "www.ebs.co.kr", "example.lec"]
print("//".join(st2)) # http://www.ebs.co.kr//example.lec
print("\\\\".join(st2)) # http:\\www.ebs.co.kr\\example.lec

print(list("Korea")) # ["K", "o", "r", "e", "a"]
print("".join(list("Korea"))) # Korea

def add_hyphen(__input, __sep="-"):
    return __sep.join(list(__input))

#############################################################
st3='ABcc@DDff@ggHI'
#print("".join("".join(st3.split("@@@")).split("???")).lower())
st4=st3.split("@")
print(" ".join(list(map(lambda x: x.lower(),st4))))

def rem_and_join(__input, __to_remove="@", __sep="-"):
    tmp=__input.split(__to_remove)
    tmp1=list(map(lambda x: x.lower(), tmp))
    return add_hyphen(tmp1, __sep)

box=list(range(1,21))
print(box[-1]) # 20
print(box[:5]) # [1, 2, 3, 4, 5]
print(box[-5:]) # [16, 17, 18, 19, 20]
print(box[0: :2]) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(box[2: :3]) # [3, 6, 9, ..., 18]

print(box[0])
# 1
print(box[0:1])
# [1]

print(box[-1]) # 20
print(box[-1:]) # [20]

def str_reverse_up(__in):
    return "".join(list(__in)[::-1]).upper()

def str_reverse_lw(__in):
    return "".join(list(__in)[::-1]).lower()

# 1부터 1000까지, 3이 들어가는 수의 개수

counter=0
for _member in range(1,1001):
    counter += str(_member).count("3")

print(counter) # 300

def count_number(_start, _end, find=3):
    count=0
    for i in range(_start, _end+1):
        count += str(i).count(str(find))
    return count

print(count_number(100,1000,7)) # 280
print(count_number(10,10**5,7)) # 49999
