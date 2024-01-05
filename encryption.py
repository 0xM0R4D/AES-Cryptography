from keyGen import  generateKeys, applySubBtes
from helpers import *

# apply subBytes4Enc  // call subBytesFunc of keyGen 4 times
# take wordsList return wordsList 
def applySubBytes4Enc(wordsListIn):
    
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
    wordsListRes = []
    for word in wordsListIn:
        subBytedWord = applySubBtes(word, subBytesMtrx)
        wordsListRes.append(subBytedWord)
    return wordsListRes


# func encrypt 16 chars and return 16 chars (latin format **or txt format)
def encrypt16Chars(txt16Chars, keys):

    # block to state step 
    # convert text chars to hex firstly 
    txtHex = txtStrToHex(txt16Chars)
    blockStateRes = blockToState(txtHex)
    # testing block to state again 
    print("block to state: ",blockStateRes)
    # add ininitial round key 
    initRoundKeyRes = addRoundKey(blockStateRes,keys,0)
    # testing init round res 
    print ("state of round 0: ", initRoundKeyRes)
    # loop 10 times:1.applySubBytes 2.ShiftRows 3.MixColumnCasei!=10 4.addRoundKey
    addRounKeyRes = initRoundKeyRes
    # print("roundKeyRes: ",addRounKeyRes)
    # initialize mixColumnMatrix
    cMatrix = ["02030101", "01020301","01010203", "03010102"]  #cMatrx in wordslist form 
    shiftRows_invOption = 0 
    for i in range(1,11):  # start from 1 end at 10 (<11)       
        subBytesRes  = applySubBytes4Enc(addRounKeyRes)
        shiftLeftRes = applyShiftRows(subBytesRes,shiftRows_invOption)
        mixColumnRes = ["","","",""]  # initialize mixCol result
        if i !=10:
            mixColumnRes = mixColumns(shiftLeftRes,cMatrix)
        else:     # case i =10 => no mix columns 
            mixColumnRes = shiftLeftRes
            
        addRounKeyRes= addRoundKey(mixColumnRes,keys,i)
        # testing 
        # if i==10:
        #     print(f"subBytesRes at round {i}:  ",subBytesRes )
        #     print(f"shiftLeftRes at round{i}:  ",shiftLeftRes ) 
        #     print(f"mixColumnRes at round{i}:  ",mixColumnRes) 
        #     print(f"addRounKeyRes at round{i}: ",addRounKeyRes)
        print(f"subBytesRes at round {i}:  ",subBytesRes )
        print(f"shiftLeftRes at round{i}:  ",shiftLeftRes ) 
        print(f"mixColumnRes at round{i}:  ",mixColumnRes) 
        print(f"addRounKeyRes at round{i}: ",addRounKeyRes)

    encryptedWordsList= addRounKeyRes
    # print("encrypted wordsList: ", encryptedWordsList)
    # convert wordsList to oneHexStr
    oneHexStr = wordsListToHexStr(encryptedWordsList)
    # print("encrypted hex str: ", oneHexStr)
    # convert hex str to txt 
    encryptedTxtStr = hexStrToTxt(oneHexStr)
    # print("encrypted txt str: ", encryptedTxtStr)     
         
    return encryptedTxtStr


# Enter your key(32 digits) in hex digits format: 706f77657266756c7a656e61726d6f72   # test by this
# testKeys = [['706f7765', '7266756c', '7a656e61', '726d6f72'], ['4DC73725', '3FA14249', '45C42C28', '37A9435A'],
#          ['9CDD89BF', 'A37CCBF6', 'E6B8E7DE', 'D111A484'], ['1A94D681', 'B9E81D77', '5F50FAA9', '8E415E2D'],
#            ['91CC0E98', '282413EF', '7774E946', 'F935B76B'], ['17657101', '3F4162EE', '48358BA8', 'B1003CC3'],
#              ['548E5FC9', '6BCF3D27', '23FAB68F', '92FA8A4C'],
#            ['39F07686', '523F4BA1', '71C5FD2E', 'E33F7762'], ['CC05DC97', '9E3A9736', 'EFFF6A18', '0CC01D7A'],
#            ['6DA10669', 'F39B915F', '1C64FB47', '10A4E63D'], ['122F21A3', 'E1B4B0FC', 'FDD04BBB', 'ED74AD86']]



# encrypt all plain text 
def encryptPlaintext():
        # get keys 
    keys = generateKeys()

    # read from file    
    plaintext = ""
    with open('plaintext.txt', 'r') as inputfile:
        lines = inputfile.readlines()
        for line in lines:
            plaintext+= line.strip()
    
    # handle different sizes of plaintext data as input
    if (len(plaintext) % 16 !=0):  # if len % 16!=0 :  add extra special chars
        rem = len(plaintext)%16 
        end = 16 - rem 
        extra =""

        for i in range(end):
            # extra+= "$"   #®       // a®®®®®®
            extra+= "®"   
        plaintext = plaintext + extra

    with open('ciphertxt.txt', 'w') as file:
        plaintext_len =len(plaintext)
        for i in range(0,plaintext_len,16):
            txt_16Chars_plaintxt  = plaintext[i:i+16]
            txt_16Chars_ciphertxt = encrypt16Chars(txt_16Chars_plaintxt,keys)
            file.write(txt_16Chars_ciphertxt)
    
    print("\nCongratulations!!\nEncrypting data is done successfully!!")




