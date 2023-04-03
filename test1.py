b=0
a=[11,2,3,4,5,6,7,8,9]
# # for b in range (len(a)):
# #     print([a[b:b+3]])
# while b<len(a):
#   # print(a[b:b+3])
#   for i in (a[b:b+3]) :
#     print(a[b:b+3:1], end=' ')
#     # print('\n')
#   b+=3

# a:list[int] = range(1,7)
# def printlist(start:int, end:int):
#   for i in range(start, end+1)
#     if i != end:
#       print(a[i], end=' ,')
#     else:
#       print(a[i])
# printlist(0,2)
# printlist(3,5)

while b < len(a):
  print("")
  for i in (a[b:b+3]):
    print(i, end=', ')
  b = b + 3