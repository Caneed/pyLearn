# list=['apple','samsung','huawei','xiaomi','vivo','oppo']

# ------------------------基本操作----------------------------------------
# print(list[1:3]) #['samsung', 'huawei']
# print(list[::-1]) #['oppo', 'vivo', 'xiaomi', 'huawei', 'samsung', 'apple']

# # list超过索引会报错

# # for循环遍历

# for i in list:
#   print(i)
# #   apple
# # samsung
# # huawei
# # xiaomi
# # vivo
# # oppo

# # 获取列表长度
# print(len(list)) #6

# ----------------------------增删改查----------------------------------------------

# list=['apple','samsung','huawei','xiaomi','vivo','oppo']


# # --------------------增--------------------------------
# print(list.append('阿里郎')) #none
# print(list) #['apple', 'samsung', 'huawei', 'xiaomi', 'vivo', 'oppo', '阿里郎']
# # 返回none，向队尾添加元素

# print(list.insert(0,'黑莓')) #none
# print(list) #['黑莓', 'apple', 'samsung', 'huawei', 'xiaomi', 'vivo', 'oppo', '阿里郎']
# # 指定索引位置插入

# print(list.extend(['IQOO','Google'])) #none
# print(list) #['黑莓', 'apple', 'samsung', 'huawei', 'xiaomi', 'vivo', 'oppo', '阿里郎', 'IQOO', 'Google'] 
# # 合并两个列表（批量添加）

# ----------------------------删除--------------------------------------

# print(list.pop()) #Google
# print(list) #['黑莓', 'apple', 'samsung', 'huawei', 'xiaomi', 'vivo', 'oppo', '阿里郎', 'IQOO']
# # 返回被删除的元素，从队尾删除元素

# print(list.pop(2)) #samsung
# # 可以添加索引

# print(list.remove('apple')) #none
# # 直接删除指定元素

# ---------------------------------修改&查询-------------------------------------

# list=['apple','samsung','huawei','xiaomi','vivo','oppo']

# list[3]='dami'
# print(list) #['apple', 'samsung', 'huawei', 'dami', 'vivo', 'oppo']
# 直接用索引进行修改和查询

# ----------------------------------------------------------------------------

# list=['apple','samsung','huawei','xiaomi','vivo','oppo']

# # for item in list:
# #   if item=='apple':
# #     item='APPLE'

# # print(list) #['apple', 'samsung', 'huawei', 'xiaomi', 'vivo', 'oppo']
# # # for循环遍历列表时无法拿到索引

# for i in range(len(list)):
#   item = list[i]
#   if item=='apple':
#     list[i]='APPLE'

# print(list) #['APPLE', 'samsung', 'huawei', 'xiaomi', 'vivo', 'oppo']

# ---------------------------------------排序-------------------------------------------

# list=[1,2,4,5,6,47,4,6342,524,5,2,542,542]

# print(list.sort())
# print(list)
# # [1, 2, 2, 4, 4, 5, 5, 6, 47, 524, 542, 542, 6342]
# print(list.sort(reverse=True))
# print(list)
# # [6342, 542, 542, 524, 47, 6, 5, 5, 4, 4, 2, 2, 1]
# # 升序，降序

# ---------------------------------------嵌套-------------------------------------------

# list=[1,2,34,4,[1,21,321,321,[321321421]]]

# print(list[4][4])
# # [321321421]


# --------------------------------------列表的稳妥删除-----------------------------
# 用一个临时列表来记录源列表
# 仅用于循环删除的时候

list=['apple','samsung','huawei','xiaomi','vivo','oppo']
temp=[]

for i in list:
  if i=='apple':
    temp.append(i) #记录要删除的元素

for item in temp:
  list.remove(item)