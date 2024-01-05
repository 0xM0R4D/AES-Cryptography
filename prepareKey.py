# this file prepare key input 
# convert from ascii format to hex format
# convert txtStr to hexStr 

from helpers import txtStrToHex 


res= input("Enter your key: ")
print("Your key in hex format: ", txtStrToHex(res))
