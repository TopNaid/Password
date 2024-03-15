print("WELCOME TO TOP BANK")
print("Please enter your password! ")

password = input("Password: ")
x = ["&","?","^","/",".","[]","+",")","()","*","%","#","@",">","'","!","_","-"]
for y in x:
    if y in password:
     print("Strong Password")
     break
else: 
    print("kindly enter a strong password or pick from the below suggestions\n1.thgf76hf'*$\n2.fggf888*&%:\n3. f7ffg^()fg!")

