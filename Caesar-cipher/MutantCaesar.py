str = input("Set the encryption password: ")
result = ""
k = input("Set the staring value: ")
k = int(k)
for i in str:
    result += chr(ord(i)+k)
    k += 1
print(result)
