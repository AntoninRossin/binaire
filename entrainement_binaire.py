def bin_to_dec(x):
    n = 0
    for i in range(len(x)):
        n += int(x[-i-1])*2**i
    return n

test = "100111001"
print(bin_to_dec(test))

def dec_to_bin(x):
    n = ""
    while x >0:
        n = str(x%2) + n
        x = x//2
    return n
print(dec_to_bin(bin_to_dec(test)))

"""

6: 110
3: 011


"""

def replace(x,y,id):
    liste = list()
    for i in range(len(x)):
        liste.append(x[i])
    liste[id] = y
    result = str()
    for i in range(len(liste)):
        result += liste[i]
    return result

def union(x,y):
    a = len(x)
    b = len(y)
    if a<b:
        x,y = y,x
    a = len(x)
    b = len(y)
    result = x
    for i in range(1,b+1):
        if x[-i] == "1" or y[-i] == "1":
            result = replace(result, "1", a-i)
        else:
            result = replace(result, "0", a-i)
    return result

print(union("110","011"))

def et(x,y):
    a = len(x)
    b = len(y)
    if a<b:
        x,y = y,x
    a = len(x)
    b = len(y)
    result = x
    for i in range(1,b+1):
        if x[-i] == "1" and y[-i] == "1":
            result = replace(result,"1",a-i)
        else:
            result = replace(result,"0",a-i)
    if a-b > 0:
        result = "0" * (a-b) + result[a-b:]
    return result
print(et("110","011"))

def xor(x,y):
    a = len(x)
    b = len(y)
    if a<b:
        x,y = y,x
    a = len(x)
    b = len(y)
    result = x
    for i in range(1,b+1):
        if x[-i] == "0" and y[-i] == "1" or x[-i] == "1" and y[-i] == "0":
            result = replace(result,"1",a-i)
        else:
            result = replace(result,"0",a-i)
    return result
print(xor("110","011"))

def decale(x,n):
    result = x
    if n >0:
        result = result + "0" * n
    elif n<0:
        result = result[:n]
    return result
