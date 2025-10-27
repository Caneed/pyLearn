# -------------字符串修改-------------------------------------------------
#strip

# s=" 你好胖 " 
# print(s)
# print(s.strip()) #去掉空格

# # split("需要使用什么去切割") 返回一个列表
# s1="1,2,3,4,5,6,7,8,9"
# print(s1.split(",")) #['1', '2', '3', '4', '5', '6', '7', '8', '9']

# # replace()

# s2="你好 我 是 你 跌 "

# print(s2.replace(" ",",")) #你好,我,是,你,跌,
# # 将指定的字符换成另外的字符

# ------字符串索引----------------------------------------------------

# s="你好我是你爸爸"
# print(s.find("你爸爸")) #4 返回它的索引值
# print(s.find("周杰伦")) #-1 未找到
# print(s.index("你爸爸")) #4 也是索引
# print(s.index("周杰伦")) #ValueError: substring not found 报错 
# find与index主要返回的是索引
# ---------------------字符串判断------------------------------------------

# s="我是你爸爸"
# print("你爸爸" in s) #true
# print("周杰伦" in s) #false
#  in 做判断 
# print(s.startswith("我")) #true
# print(s.startswith("你爸爸")) #false
# 相应的还有endswith()

# s="100"
# print(s.isdigit()) #判断是否为整数组成

# ----------------------------字符串其它操作-----------------------------------

# s="我是你爸爸"
# list=['apple','huawei','xiaomi']
# print(len(s)) #返回长度 5
# print("-".join(list)) #apple-huawei-xiaomi 拼接列表
