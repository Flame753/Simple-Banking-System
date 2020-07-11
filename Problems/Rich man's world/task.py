deposit = int(input())
year = 0
while deposit < 700000:
    deposit *= 1.071
    year += 1
print(year)
