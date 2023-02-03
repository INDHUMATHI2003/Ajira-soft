def add_computer(name):
    c_list=[]
    c_list.append(name)
    return "Successfully added {}".format(name[-2:])
computer_name=input(" ")
if computer_name=="ADD":
    print("invalid command syntax")
else:
 print(add_computer(computer_name))

