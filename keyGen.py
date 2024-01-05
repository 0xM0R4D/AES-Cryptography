from helpers import applyXoring # xor function take 2 hex strings return 1 hex string

# validate user input is hex or no 
def isHex(inputString):
    try:
        int(inputString, 16)
        return True
    except ValueError:
        return False

# take input as hex key and send res.(1 key) to generate keys func. 
def setKeyRet(): # set and return key 
    key =""
    key = input("Enter your key(32 digits) in hex digits format: ")
    while True:
        if len(key)==32 and isHex(key):
            break
        elif key!=32:
            key =input("Error!!\nyour key length not equal 32.\nPlz, enter key its length equal 32: ")
        else : 
            key =input("Error!!\nyour key contain non-hex digits.\nPlz, enter key in hex foramt(their all digits are hexa): ")
    return key 


# Rcon function 
def applyRcon(roundNum):
                # 1             2                3            4            5        6                
    rconList = ['01000000','02000000','04000000','08000000','10000000','20000000'
                ,'40000000','80000000','1B000000','36000000']   # 7 8 9 10 
    ret = rconList[roundNum -1]  
    return ret 

# subBytes func. **also used in enc, dec processes 
def applySubBtes(wordIn, subBytesMtrxIn):# take 1 word, subBytesMatrix and  return 1 word

    wordRes = ""
# af 33 se 78  
    for i in range(0,8,2):        
        ch1=wordIn[i]    # af  
        rowIdx= int(ch1,16)  # hex char to decimal
        ch2 = wordIn[i+1]
        colIdx = int(ch2,16)
        elemRes= subBytesMtrxIn[rowIdx][colIdx]   # fuc("ab") = "dd"
        wordRes += elemRes
    
    return wordRes


# k[i].w[j] = k[i-1].w[i]  xor  k[i].w[j-1]  case j!=0 
# k[i].w[0] = k[i-1].w[0]  xor   subBytes(shiftLeft2HexDigits(k[i].w[3]))  xor rcon[i]  
## create key rounds 
def createKeys(initKey):  # take initial key and return list of 11 keys

    # subBytesMtrx for passing to applySubBytes func. when calling 
    subBytesMtrx = [
    ['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'],
    ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'],
    ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'],
    ['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'],
    ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'],
    ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'],
    ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'],
    ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'],
    ['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'],
    ['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'],
    ['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'],
    ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'],
    ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'],
    ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'],
    ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'],
    ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']
]   
    # seperate key to words     # 1234458909879878979798797
    w0 = initKey[0:8]
    w1 = initKey[8:16]
    w2 = initKey[16:24]
    w3 = initKey[24:32]
    tmpKey= [w0,w1,w2,w3]    
    
    # keys is list contain strings list(words list)   *init key+ i need create 10 keys. 
    keys = []
    keys.append(tmpKey) # add initial key to keys list
    # print round 0 of keys  *keys[0]
    # print("keys round 0: ", keys[0])
    # create 10 keys 
    # append one key(empty) first then re-setting it inside inner loop 
    for i in range (1,11):
        tmpKey = ['','','','']  # empty key initialize empty words 
        keys.append(tmpKey)
        # for each key 
        for j in range(4):
            if j == 0:
                rconRes = applyRcon(i)            ### continue here after pseudo code 
                accessedW3 = keys[i-1][3]
                shiftLeftRes= accessedW3[2:]+accessedW3[:2]
                subBytesRes = applySubBtes(shiftLeftRes,subBytesMtrx)
                res1 = applyXoring(subBytesRes,rconRes)
                res2 = applyXoring(keys[i-1][0],res1)
                keys[i][0]= res2
            else:
                res = applyXoring(keys[i-1][j],keys[i][j-1])
                keys[i][j]= res
    
        # print(f"keys round {i}: ", keys[i])

    print(" generating keys is finished\n")           
    return keys


# generate keys function
def generateKeys():
    inputKey =  setKeyRet()  
    # inputKey = "5468617473206D79204B756E67204675"
    keysList = createKeys(inputKey) # take init key return 11 keys 
    return keysList
