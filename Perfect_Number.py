total = 0
num = int(input("Enter the number: "))

for i in range(1,num):
    if num % i == 0:
        total += i
        if total == num:
            print('Perfect Number ! : ',total) 
    else:
        continue













