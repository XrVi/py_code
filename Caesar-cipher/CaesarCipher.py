str = input("Input the ciphertext: ")
for k in range(1, 26):
    result = ""
    for i in str:
        if ord(i) < 65 or 97 > ord(i) > 90 or ord(i) > 122:
            result += i
            continue
        elif (90 >= ord(i) >= 65 and ord(i)+k >= 91) or (122 >= ord(i) >= 97 and ord(i)+k >= 123):
            result += chr(ord(i) + k - 26)
        else:
            result += chr(ord(i) + k)
    print(result)
