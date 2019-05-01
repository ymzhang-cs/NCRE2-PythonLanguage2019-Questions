'''
设n是一任意自然数，如果n的各位数字反向排列所得自然数与n相等，则n被成为回文数。从键盘输入一个5位数字，请编写程序判断这个数字是不是回文数
'''
try:
    num = eval(input("请输入一个五位数字："))
except NameError:
    print("这不是一个五位数字。")
except:
    print("未知错误")
numStr = str(num)
if len(numStr) != 5:
    print("这不是一个五位数字！")
else:
    if numStr[::-1] == numStr:
        print("这是一个回文数")
    else:
        print("这不是个回文数")