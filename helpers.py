# from keyGen import applyXoring


# xor function take 2 hex strings return 1 hex string    **take 2 words return 1 word  *** this func. used also in keyGen
def applyXoring(hexStr1 , hexStr2):
    # convert hex strings to binary *convert hex string to decimal firstly by int(hexDigit,16)
    binStr1 = ''.join(format(int(hexDigit,16),'04b') for hexDigit in hexStr1)  # 04b for bin in 4 bits
    binStr2 = ''.join(format(int(hexDigit,16),'04b') for hexDigit in hexStr2)
    
    #apply xor operation 
    binStrRes =[]
    iterationLen = len(binStr1)      # length of any of them 
    for i in range(iterationLen):
        if (binStr1[i]=='0' and binStr2[i] == '0') or (binStr1[i]=='1' and binStr2[i] == '1'): 
            binStrRes.append('0')
        else: 
            binStrRes.append('1')
    binStrRes = ''.join(binStrRes)

    # converting ret binary string to hex string 
    hexString = ''.join(format(int(binStrRes[i:i+4], 2), 'X') for i in range(0, len(binStrRes), 4))

    return hexString 



#### some additions for decryption part 

# look up in L table func. 
def lookUpLTable(elem):    # 1 elem: ch1,ch2         //exactly:dig1,dig2
    # tmp make first elem:00 instead ++
    L_matrix = [
    ["00", "00", "19", "01", "32", "02", "1A", "C6", "4B", "C7", "1B", "68", "33", "EE", "DF", "03"],
    ["64", "04", "E0", "0E", "34", "8D", "81", "EF", "4C", "71", "08", "C8", "F8", "69", "1C", "C1"],
    ["7D", "C2", "1D", "B5", "F9", "B9", "27", "6A", "4D", "E4", "A6", "72", "9A", "C9", "09", "78"],
    ["65", "2F", "8A", "05", "21", "0F", "E1", "24", "12", "F0", "82", "45", "35", "93", "DA", "8E"],
    ["96", "8F", "DB", "BD", "36", "D0", "CE", "94", "13", "5C", "D2", "F1", "40", "46", "83", "38"],
    ["66", "DD", "FD", "30", "BF", "06", "8B", "62", "B3", "25", "E2", "98", "22", "88", "91", "10"],
    ["7E", "6E", "48", "C3", "A3", "B6", "1E", "42", "3A", "6B", "28", "54", "FA", "85", "3D", "BA"],
    ["2B", "79", "0A", "15", "9B", "9F", "5E", "CA", "4E", "D4", "AC", "E5", "F3", "73", "A7", "57"],
    ["AF", "58", "A8", "50", "F4", "EA", "D6", "74", "4F", "AE", "E9", "D5", "E7", "E6", "AD", "E8"],
    ["2C", "D7", "75", "7A", "EB", "16", "0B", "F5", "59", "CB", "5F", "B0", "9C", "A9", "51", "A0"],
    ["7F", "0C", "F6", "6F", "17", "C4", "49", "EC", "D8", "43", "1F", "2D", "A4", "76", "7B", "B7"],
    ["CC", "BB", "3E", "5A", "FB", "60", "B1", "86", "3B", "52", "A1", "6C", "AA", "55", "29", "9D"],
    ["97", "B2", "87", "90", "61", "BE", "DC", "FC", "BC", "95", "CF", "CD", "37", "3F", "5B", "D1"],
    ["53", "39", "84", "3C", "41", "A2", "6D", "47", "14", "2A", "9E", "5D", "56", "F2", "D3", "AB"],
    ["44", "11", "92", "D9", "23", "20", "2E", "89", "B4", "7C", "B8", "26", "77", "99", "E3", "A5"],
    ["67", "4A", "ED", "DE", "C5", "31", "FE", "18", "0D", "63", "8C", "80", "C0", "F7", "70", "07"]
]
    # dig1=elem[0]
    ch1=elem[0]
    rowIdx= int(ch1,16)  # hex char to decimal
    ch2 = elem[1]
    colIdx = int(ch2,16)
    elemRes= L_matrix[rowIdx][colIdx]
    return elemRes
    

# look up in E table func. // 35
def lookUpETable(elem):    # 1 elem: ch1,ch2         //exactly:dig1,dig2
    E_matrix = [
    ["01", "03", "05", "0F", "11", "33", "55", "FF", "1A", "2E", "72", "96", "A1", "F8", "13", "35"],
    ["5F", "E1", "38", "48", "D8", "73", "95", "A4", "F7", "02", "06", "0A", "1E", "22", "66", "AA"],
    ["E5", "34", "5C", "E4", "37", "59", "EB", "26", "6A", "BE", "D9", "70", "90", "AB", "E6", "31"],
    ["53", "F5", "04", "0C", "14", "3C", "44", "CC", "4F", "D1", "68", "B8", "D3", "6E", "B2", "CD"],
    ["4C", "D4", "67", "A9", "E0", "3B", "4D", "D7", "62", "A6", "F1", "08", "18", "28", "78", "88"],
    ["83", "9E", "B9", "D0", "6B", "BD", "DC", "7F", "81", "98", "B3", "CE", "49", "DB", "76", "9A"],
    ["B5", "C4", "57", "F9", "10", "30", "50", "F0", "0B", "1D", "27", "69", "BB", "D6", "61", "A3"],
    ["FE", "19", "2B", "7D", "87", "92", "AD", "EC", "2F", "71", "93", "AE", "E9", "20", "60", "A0"],
    ["FB", "16", "3A", "4E", "D2", "6D", "B7", "C2", "5D", "E7", "32", "56", "FA", "15", "3F", "41"],
    ["C3", "5E", "E2", "3D", "47", "C9", "40", "C0", "5B", "ED", "2C", "74", "9C", "BF", "DA", "75"],
    ["9F", "BA", "D5", "64", "AC", "EF", "2A", "7E", "82", "9D", "BC", "DF", "7A", "8E", "89", "80"],
    ["9B", "B6", "C1", "58", "E8", "23", "65", "AF", "EA", "25", "6F", "B1", "C8", "43", "C5", "54"],
    ["FC", "1F", "21", "63", "A5", "F4", "07", "09", "1B", "2D", "77", "99", "B0", "CB", "46", "CA"],
    ["45", "CF", "4A", "DE", "79", "8B", "86", "91", "A8", "E3", "3E", "42", "C6", "51", "F3", "0E"],
    ["12", "36", "5A", "EE", "29", "7B", "8D", "8C", "8F", "8A", "85", "94", "A7", "F2", "0D", "17"],
    ["39", "4B", "DD", "7C", "84", "97", "A2", "FD", "1C", "24", "6C", "B4", "C7", "52", "F6", "01"]
]
    # dig1=elem[0]
    ch1=elem[0]
    rowIdx= int(ch1,16)  # hex char to decimal
    ch2 = elem[1]
    colIdx = int(ch2,16)
    elemRes= E_matrix[rowIdx][colIdx]
    return elemRes    


# do addition operation on 2 hex strings(2 elements) and return 1 element 
def add2HexElem_mixCol(elem1, elem2):
    # convert hexadecimal elements to integers(decimal) for addition
    int_elem1 = int(elem1, 16)
    int_elem2 = int(elem2, 16)
    # print("elem1 as decimal: ",int_elem1,"elem2 as decimal: ", int_elem2 )    
    result = int_elem1 + int_elem2   # Perform addition    
    # if hexResult > "ff": hexResult-="ff" (result > 255)
    if result > 255:
        result -= 255
    
    # convert back to hexa string format
    resElem = hex(result)[2:]      # remove '0x' prefix        
    resElem = resElem.zfill(2) # add prefix zero if necessary to maintain two-digit format  // 03
    
    return resElem  # return 1 element 


def multiply2Elems_mixCol(elem1,elem2): # ab  x   3d  
    # if elem1=0 or elem2=0  ==>  res=0
    if elem1=="00" or elem1=="00": # if zero, therefore res of mult. is zero. so no lookUp tables
        elemRes = "00"
        return elemRes
    LTableRes1 = lookUpLTable(elem1)
    LTableRes2 = lookUpLTable(elem2)
    additionRes = add2HexElem_mixCol(LTableRes1,LTableRes2)
    ETableRes = lookUpETable(additionRes)
    return ETableRes 


# func: convert hexString to binString  a  =>10   ==>1010
def hexStrToBinStr(hexStrIn): 
    binString = ''.join(format(int(hexDigit, 16), '04b') for hexDigit in hexStrIn)
    return binString

# func: convert bin string to hex string     10001101
def binStrToHexStr(binStrIn):
    hexStr = ''.join(format(int(binStrIn[i:i+4], 2), 'X') for i in range(0, len(binStrIn), 4))
    return hexStr


# func: xoring two bin strings and return one bin string
def xorBinStrings(binStr1,binStr2):    #    // take any length and used in general 
    ret = [] 
    itrLen = len(binStr1)
    for i in range(itrLen):
        if (binStr1[i]=='0' and binStr2[i] == '0') or (binStr1[i]=='1' and binStr2[i] == '1'): 
            ret.append('0')
        else: 
            ret.append('1')
    ret = ''.join(ret)
    # ret = str(ret)
    return ret 

# GF function is called in mix column function *ex:GF(word1,word2)=2HexDigits_str
# take 1 col.(word) of wordsList and 1 raw(word) of state mtrx then retun 1 element(e.g. '3D')
def GF(lWord, cWord):
    # ex: res = lWord[0]*cWord[0]+....+ lWord[3]*cWord[3]//* is multiplyFunc and +is xor
    # multiplication operations
    # global multiply2Elems_mixCol
    multRes1 = multiply2Elems_mixCol(lWord[0:2],cWord[0:2]) # element = 2 hex digits.ex:'F5'
    multRes2 = multiply2Elems_mixCol(lWord[2:4],cWord[2:4]) # result: 1 element
    multRes3 = multiply2Elems_mixCol(lWord[4:6],cWord[4:6])
    multRes4 = multiply2Elems_mixCol(lWord[6:8],cWord[6:8]) 
    #above returned hex elements. *must converting to bin before calling xorBinStrings func. 
    # xoring operations
    xorRes1 = xorBinStrings(hexStrToBinStr(multRes1),hexStrToBinStr(multRes2))  # result is bin string
    xorRes2 = xorBinStrings(hexStrToBinStr(multRes3),hexStrToBinStr(multRes4))  # result is bin string
    xorRes3 = xorBinStrings(xorRes1,xorRes2)  # here bin string 
    # convert bin string to hex string     
    # res = ''.join(format(int(xorRes3[i:i+4], 2), 'X') for i in range(0, len(xorRes3), 4))
    res = binStrToHexStr(xorRes3)
    return res  # 1 element as hex string, ex: '62'


def mixColumns(wordsListIn, mixColMatrixIn):
    # cMatrix = ["02030101", "01020301","01010203", "03010102"]  #cMatrx in wordslist form 
    
    resWordsList = ["","","",""] # initialize wordsList with 4 empty words

    for i in range(4):
        lWord = wordsListIn[i] # access word of wordsListIn (accessColumn)
        for j in range(4):
            cWord = mixColMatrixIn[j]  # access word of cMatrix (accessRaw)
            GFRes = GF(lWord,cWord) # apply GF with col,rows
            # resWordsList[j]+=GFRes 
            # test to solve bug. :  ===> ok, really solved bug. ==> continue testing 
            resWordsList[i]+=GFRes 
    
    return resWordsList
                          ####   new edition: take 32 hex instead 16 chars 
def blockToState(txtHex): # take 32 hex digits  return 32 hex in wordsList format
 
    # put hex digits as words list form 
    wordsListRes=[]
    for i in range(0,len(txtHex),8):  # every 8 digits = 1 word
        getWord = txtHex[i:i+8]
        wordsListRes.append(getWord)
    
    return wordsListRes # return words list 


# add round key func. : take wordsList, keys, keyNum(*zeroBased) and return wordsList
def addRoundKey(wordsListIn, keys,keyNum):
    resWordsList =[]
    for i in range(4):
        getWord= applyXoring(wordsListIn[i],keys[keyNum][i])#Xor(1wordOfWordsLists,1wordOfKey)
        resWordsList.append(getWord)                             

    return resWordsList        


# apply shift rows func.  take wordsList return wordsList 
def applyShiftRows(wordsListIn,invOption):
    
    # convert wordslist to rows 
    rows = ["","","",""]
    rows[0] = wordsListIn[0][0:2]+wordsListIn[1][0:2]+wordsListIn[2][0:2]+wordsListIn[3][0:2]
    rows[1] = wordsListIn[0][2:4]+wordsListIn[1][2:4]+wordsListIn[2][2:4]+wordsListIn[3][2:4]
    rows[2] = wordsListIn[0][4:6]+wordsListIn[1][4:6]+wordsListIn[2][4:6]+wordsListIn[3][4:6]
    rows[3] = wordsListIn[0][6:8]+wordsListIn[1][6:8]+wordsListIn[2][6:8]+wordsListIn[3][6:8]
    # apply left shifting 
    if invOption==0:
    # if invOption==0 or invOption==1:
        rows[1] = rows[1][2:8]+ rows[1][0:2]
        rows[2] = rows[2][4:8]+ rows[2][0:4]
        rows[3] = rows[3][6:8]+ rows[3][0:6]
    else: # case invOption==1 
                 # apply right shifting 
        rows[1] = rows[1][6:8]+ rows[1][0:6]
        rows[2] = rows[2][4:8]+ rows[2][0:4]
        rows[3] = rows[3][2:8]+ rows[3][0:2]

    # converting rows to wordsList 
    resWordsList = ["","","",""]
    resWordsList[0] = rows[0][0:2]+rows[1][0:2]+rows[2][0:2]+rows[3][0:2]
    resWordsList[1] = rows[0][2:4]+rows[1][2:4]+rows[2][2:4]+rows[3][2:4]
    resWordsList[2] = rows[0][4:6]+rows[1][4:6]+rows[2][4:6]+rows[3][4:6]
    resWordsList[3] = rows[0][6:8]+rows[1][6:8]+rows[2][6:8]+rows[3][6:8]

    return resWordsList # return words list 

# testWordsList = ["ABCD0120","01234567","EF123BCD","123EFBCD"]
# testWord = "ABCD0120"


# convert wordsList to oneHex string 
def wordsListToHexStr(wordsListIn):
    hexStrRes = ""
    for word in wordsListIn: # loop on 4 words 
        for digit in word:   # loop on one word to access their digits        
            hexStrRes+=digit
    return hexStrRes

# convert hexStr to txtStr  // hex to bytes then to txt 
def hexStrToTxt(hexStrIn):
    byteData = bytes.fromhex(hexStrIn)    #hex to bytes
    # convert the byte data to a text string
    textString = byteData.decode('latin-1')  # UTF-8 encoding, can be different

    return textString

# convert txtStr to hexStr 
def txtStrToHex(txtStrIn):
    txtStrIn = str(txtStrIn)  
    txtBytes = txtStrIn.encode('latin-1')
    hexStr = txtBytes.hex()
    return hexStr
