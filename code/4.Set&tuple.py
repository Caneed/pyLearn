# --------------------------tuple:不可变的列表---------------------------------------

# t=('apple','samsung','huawei')
# print(t) #('apple', 'samsung', 'huawei')
# # t[0]='oppo'
# # 改变元组时会报错

# -------------------------------Set----------------------------------------------

# s={1,2,3,'huawei',4,5,'apple'}
# print(s)
# # {1, 2, 3, 4, 5, 'huawei', 'apple'}
# # set是无序的，set不可放入列表

# s1=set()
# s1.add('apple')
# s1.add('samsung')
# s1.add('vivo')
# s1.add('oppo')
# print(s1)
# # {'oppo', 'vivo', 'samsung', 'apple'}
# # 删除最多使用的就是remove
# s1.remove('apple')
# print(s1) #{'oppo', 'vivo', 'samsung'}
# # 想修改只能先删除再添加

# # 修改
# for item in s1:
#   print(item)
# # oppo
# # vivo
# # samsung

# ----------------------------------------交集，并集，差集--------------------------------

# s1={'apple','samsung','huawei','vivo'}
# s2={'apple','banana','grapes'}

# # 交集
# print(s1 & s2)
# print(s1.intersection(s2))
# # {'apple'}
# # {'apple'}


# # 并集
# print(s1|s2) #{'banana', 'samsung', 'grapes', 'huawei', 'apple', 'vivo'}
# print(s1.union(s2))  #{'banana', 'samsung', 'grapes', 'huawei', 'apple', 'vivo'}

# # 差集
# print(s1-s2)
# print(s1.difference(s2))
# # {'vivo', 'huawei', 'samsung'}
# # {'vivo', 'huawei', 'samsung'}

# print(s2-s1)
# print(s2.difference(s1))
# # {'banana', 'grapes'}
# # {'banana', 'grapes'}

# -----------------------------去重-------------------------------------------

s={'apple','samsung','vivo'}
s.add('apple')
print(s) #{'vivo', 'apple', 'samsung'}
# 集合中不允许有一样的元素
# 使用set来为list去重

lst=[111,111,111,111,3,4,5,6,6,7,13,43,14,123,414,312]
print(set(lst)) #{3, 4, 5, 6, 7, 43, 13, 14, 111, 312, 123, 414}
print(list(set(lst))) #[3, 4, 5, 6, 7, 43, 13, 14, 111, 312, 123, 414]

# 去重之后无序了