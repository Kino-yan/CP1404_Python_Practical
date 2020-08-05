
name_file=open('name.txt', 'w')
name=str(input("Please enter your name: "))
print("Your name is "+name, file=name_file)
name_file.close


number_file1=open('numbers.txt','w')
number=['17','42','400']
print("{}".format(number[0]), file=number_file1)
print("{}".format(number[1]), file=number_file1)
print("{}".format(number[2]), file=number_file1)
number_file1.close()

number_file2=open('numbers.txt','r')
result=0
num1=int(number_file2.readline())
num2=int(number_file2.readline())
result=num1+num2
print("{} + {} = {}".format(num1,num2,result))
number_file2.close()


number_file3=open('numbers.txt','r')
all_lines = number_file3.readlines()
print(all_lines)
number_file3.close()


