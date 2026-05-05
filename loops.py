# continue - move to the next iteration
# break - break out of the loop

nums = [1,2,3,4,5]
for i in nums:
    if i == 3:
        # print('Found!')
        continue
    # print(i)

# for num in nums:
#     for letter in 'abc':
        # print(num, letter)

# for i in range(1,11):
#     print(i)

x = 0
#while x<10:
while True:
    if x==5:
        break
    print(x)
    x += 1