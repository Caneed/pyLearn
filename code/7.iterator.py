# iter
import sys

lis=[1,2,3,4,5]
it=iter(lis)
# print(next(it)) #1
# print(next(it)) #2
# print(next(it)) #3
# print(next(it)) #4
# print(next(it)) #5
# print(next(it)) #StopIteration

## for 遍历iter
# for i in it:
#   print(i) #1 2 3 4 5

# 使用while遍历
while True:
  try:
    print(next(it))
  except StopIteration:
    sys.exit()

# 1 2 3 4 5

