Principal = int(input())
Year = int(input())
bank = []
for i in range(2):
    sumAmt = 0
    for i in range(int(input())):

        eachYr,r = input().split()
        part1 = pow((1+float(r)),int(eachYr)*12)
        emiAmt = (Principal*float(r))/(1-1/part1)
        sumAmt += emiAmt

    bank.append(sumAmt)
print(bank)
if bank[0]<bank[1]:
    print("Bank A")
else:
    print("Bank B")