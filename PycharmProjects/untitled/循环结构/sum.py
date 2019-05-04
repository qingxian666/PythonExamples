"""
用for循环实现1~100求和

"""

sum = 0
for x in range(101):
    sum += x
print(sum)

"""
range(101)可以产生一个0到100的整数序列。
range(1, 100)可以产生一个1到99的整数序列。
range(1, 100, 2)可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量。
"""

"""
用for循环实现1~100之间的偶数求和

"""

sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)