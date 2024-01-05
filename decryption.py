from keyGen import applySubBtes, generateKeys
from helpers import *


def applySubBytes4Dec(wordsListIn):
    
    invSubBytesMtrx = [
    ["52", "09", "6A", "D5", "30", "36", "A5", "38", "BF", "40", "A3", "9E", "81", "F3", "D7", "FB"],
    ["7C", "E3", "39", "82", "9B", "2F", "FF", "87", "34", "8E", "43", "44", "C4", "DE", "E9", "CB"],
    ["54", "7B", "94", "32", "A6", "C2", "23", "3D", "EE", "4C", "95", "0B", "42", "FA", "C3", "4E"],
    ["08", "2E", "A1", "66", "28", "D9", "24", "B2", "76", "5B", "A2", "49", "6D", "8B", "D1", "25"],
    ["72", "F8", "F6", "64", "86", "68", "98", "16", "D4", "A4", "5C", "CC", "5D", "65", "B6", "92"],
    ["6C", "70", "48", "50", "FD", "ED", "B9", "DA", "5E", "15", "46", "57", "A7", "8D", "9D", "84"],
    ["90", "D8", "AB", "00", "8C", "BC", "D3", "0A", "F7", "E4", "58", "05", "B8", "B3", "45", "06"],
    ["D0", "2C", "1E", "8F", "CA", "3F", "0F", "02", "C1", "AF", "BD", "03", "01", "13", "8A", "6B"],
    ["3A", "91", "11", "41", "4F", "67", "DC", "EA", "97", "F2", "CF", "CE", "F0", "B4", "E6", "73"],
    ["96", "AC", "74", "22", "E7", "AD", "35", "85", "E2", "F9", "37", "E8", "1C", "75", "DF", "6E"],
    ["47", "F1", "1A", "71", "1D", "29", "C5", "89", "6F", "B7", "62", "0E", "AA", "18", "BE", "1B"],
    ["FC", "56", "3E", "4B", "C6", "D2", "79", "20", "9A", "DB", "C0", "FE", "78", "CD", "5A", "F4"],
    ["1F", "DD", "A8", "33", "88", "07", "C7", "31", "B1", "12", "10", "59", "27", "80", "EC", "5F"],
    ["60", "51", "7F", "A9", "19", "B5", "4A", "0D", "2D", "E5", "7A", "9F", "93", "C9", "9C", "EF"],
    ["A0", "E0", "3B", "4D", "AE", "2A", "F5", "B0", "C8", "EB", "BB", "3C", "83", "53", "99", "61"],
    ["17", "2B", "04", "7E", "BA", "77", "D6", "26", "E1", "69", "14", "63", "55", "21", "0C", "7D"]
]

    wordsListRes = []
    for word in wordsListIn:
        subBytedWord = applySubBtes(word, invSubBytesMtrx)
        wordsListRes.append(subBytedWord)
    return wordsListRes


# take *32 hex* (16 chars) and return 16 txt chars **newEdition: take txt chars instead hex
# def decrypt16Chars(hex32Digits): 
def decrypt16Chars(txt16Chars, keys): 
 
    # converting txt to hex 
    hex32Digits = txtStrToHex(txt16Chars)
    
    # block to state 
    blockToStateRes = blockToState(hex32Digits)
    # test block to state again 
    # print("block to state: ",blockToState)

    #setting inverse option for shift left and use invMixColumn matrix
    shiftInvOption = 1 
    invMixColumnMtrx = ["0E0B0D09","090E0B0D","0D090E0B","0B0D090E"]
    # loop 10 times from 10 to 1 and do: 1.addRoundKey[i] 2.mixColumnCase i!=10  3. shiftRows 4.subBytes 
    tmpWordsListInput = blockToStateRes
    for i in range(10, 0, -1):
        addRoundKeyRes = addRoundKey(tmpWordsListInput,keys,i)
        if i!=10: # apply inv mix columns 
            invMixColRes = mixColumns(addRoundKeyRes, invMixColumnMtrx)
        else: # ignore inv mix columns 
            invMixColRes = addRoundKeyRes
        invShiftRowsRes = applyShiftRows(invMixColRes,shiftInvOption)
        invSubBytesRes  = applySubBytes4Dec(invShiftRowsRes)
        tmpWordsListInput = invSubBytesRes

    addRoundKeyRes = addRoundKey(tmpWordsListInput,keys,0) # apply final round and now, res: wordsList
    # convert wordsList to hex str
    hexRes = wordsListToHexStr(addRoundKeyRes)    
    # print("decrypted as hex: ", hexRes)
    txtRes = hexStrToTxt(hexRes)
    # print("decrypted as txt: ", txtRes)

    return txtRes


# decrypt all cipher  
def decryptCiphertext():
    # get keys 
    keys = generateKeys()
    # read from file    
    ciphertext = ""
    with open('ciphertxt.txt', 'r') as inputfile:
        lines = inputfile.readlines()
        for line in lines:
            ciphertext+= line.strip()

    
    with open('plaintext.txt', 'w') as file:
        ciphertext_len =len(ciphertext)
        for i in range(0,ciphertext_len,16):
            txt_16Chars_ciphertxt  = ciphertext[i:i+16]
            txt_16Chars_plaintxt = decrypt16Chars(txt_16Chars_ciphertxt,keys)
            for ch in txt_16Chars_plaintxt:
                if ch=="®":
                    continue
                file.write(ch)
    print("\nCongratulations!!\nDecrypting ciphertext is done successfully!!")
                

