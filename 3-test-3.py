'''
程序读入一个表示星期几的数字（1-7），输出所对应的星期字符串名称。例如：输入3，返回“星期三”
'''
day = {1:19968, 2:20108, 3:19977, 4:22235, 5:20116, 6:20845, 7:26085}
dayInput = eval(input("请输入一个1-7的数字："))
try:
    print("星期" + chr(day[dayInput]))
except KeyError:
    print("您输入的不是1-7之间的数字！")
except:
    print("未知错误！")