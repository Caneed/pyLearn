# 键值对形式存储

d={
  'y':1,
  'x':2,
  'aaa':3,
  'bbb':4
}

print(d['y']) #1

# 判断是否存在键
print('z' in d) #false
print(d.get('z')) #none
print(d.get('y')) #1

# 删除键
print(d.pop('x')) #2
print(d) #{'y':1,'aaa':3,'bbb':4}
# 或者使用del来删除
del d['aaa']
print(d) #{'y':1,'bbb':4}


# # 清空字典
# d.clear()
# print(d) #{}
# del d
# print(d) #报错