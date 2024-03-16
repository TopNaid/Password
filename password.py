print("WELCOME TO TOP BANK")
print("Please enter your password! ")

password = input("Password: ")
x = ["&","?","^","/",".","[","]","+",")","(","*","%","#","@",">","'","!","_","-","$",",",":","|",";","=","<","}","{"]
# Note: the condition for the user to have a strong password is that their password must include any
#  of the special character above.
for y in x:
    if y in password:
     print("Strong Password")
     break
else: 
    print("kindly enter a strong password or pick from the suggestions below\n1. thgf76hf'*$\n2. fggf888*&%:\n3. f7ffg^()fg!")

