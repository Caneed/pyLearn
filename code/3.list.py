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

# ----------------------------------------------------------------------------------

