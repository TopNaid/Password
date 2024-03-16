from gen import generate_password\

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
    pasca = generate_password()
    print(f"kindly enter a strong password or pick the suggestion below \n{pasca}")

