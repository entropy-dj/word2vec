a = [1, 4, 3, 5, 2]
b = ['c', 'a', 'd', 'b', 'e']
"""
第一种排序，变成list，里面全是元组
"""
data1 = [(x, y) for x, y in zip(a, b)]
# 按照第一个排序
result = sorted(data1, key= lambda x:x[0])
print(result)
"""
第二种排序，用zip
"""
data2 = zip(a, b)
result = sorted(data2)  # 看zip第一个元素是谁(当前是a)
print(result)