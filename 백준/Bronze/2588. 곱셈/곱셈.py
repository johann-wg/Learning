num1 = int(input())
num2 = input()

for i in num2[::-1]:
    print(int(i) * num1)
print(num1 * int(num2))