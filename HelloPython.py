msg = "Hello world"
print(msg)
def hi(name):
    if not len(str(name))>0:
        print('이름이 없어요!~')
        
    print('Hi I\'m '+ str(name))

temp_list = [3,12,5,"345",12.8,12]
for target_list in temp_list:
    print("this val : "+ str(target_list))
hi()




