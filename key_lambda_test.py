"""
在排序的时候，接使用sorted方法，返回一个列表就是排序好的
"""
a = [4, 2, 6, 1, 8, 3, 6, 3]
b = ["d", "a", "x", "w", "v", "c"]
print(sorted(a))
print(sorted(b))
print(sorted(a, reverse=True))
print(sorted(b, reverse=True))

"""
x[0]表示元组里的第一个元素，x[1]当然就是第二个元素；  
"""
a = [("d", 4), ("a", 1), ("c", 9), ("b", 5), ("e", 2), ]
print(sorted(a, key=lambda x: x[0]))
print(sorted(a, key=lambda x: x[1]))
print(sorted(a, key=lambda x: x[0], reverse=True))
print(sorted(a, key=lambda x: x[1], reverse=True))
