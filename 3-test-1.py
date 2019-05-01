'''
获取用户输入的一个整数，输出该整数百位及以上的数字
'''
a = int(input("请输入一个三位或以上的整数："))
aOutput = str(a)[0:-2]
print(aOutput)
