import time
def intnabin(n):
    start_time = time.time()
    b = ''
    while n > 0:
        n = n/2
        # print(n)
        if n%1 == 0:
            b+=str('0')
        else:
            b+=str('1')
        n = int(n)
    print("Here is a result:")    
    print(b[::-1])
    print(f"Time of process: {time.time() - start_time}")

print("Enter integer number:")
liczba = int(input())
intnabin(liczba)
#example int 78 give bin 1001110 