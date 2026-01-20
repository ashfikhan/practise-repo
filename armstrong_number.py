num = int(input())
temp = num
n = len(str(num))
sum =0

while temp > 0:
    digit = temp % 10
    sum += digit**n

    temp //= 10

if sum == num:
    print("armstong")

else:
   print("not a armstrong")
