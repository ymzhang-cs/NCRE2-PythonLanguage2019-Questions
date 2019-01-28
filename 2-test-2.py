'''
获得用户输入的一段文字，将这段文字进行垂直输出
'''
string = input("Please input a string:")
i = len(string) - 1
s = 0
while i >= s:
    print(string[s],end="\n")
    s = s + 1
