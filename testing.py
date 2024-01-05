# # from encryption import binStrToHexStr
# # class Word:
# #     # construcor of class *init method
# #     def __init__(self):
# #         self.elements = [0, 0, 0, 0]  # initializing with zeros

# #     # set word function
# #     def setWord(self, word_list):
# #         self.elements = word_list
        
# #     # get word function
# #     def getWord(self):
# #         return self.elements
# from WordClass import Word

# # Example usage:
# word_obj = Word()

# # Setting a word
# new_word = ['a','b','c','ee']
# word_obj.setWord(new_word)

# # Getting the word
# retrieved_word = word_obj.getWord()
# # print("Retrieved Word:", type(retrieved_word[0]))
# # print("Retrieved Word:", retrieved_word)


# def is_hex(input_string):
#     try:
#         int(input_string, 16)
#         return True
#     except ValueError:
#         return False

# # Example usage:
# user_input = "2B7E151"

# # if is_hex(user_input):
# #     print("Valid hexadecimal input!")
# # else:
# #     print("Not a valid hexadecimal input.")

# # convert hex to decimal 
# hex_string = 'A1B4'
# decimal_list = [int(x, 16) for x in hex_string]
# # print(decimal_list)


# hex_string = 'A1B4'
# # Convert each hex digit to binary (4 bits) and concatenate them
# binary_string = ''.join(format(int(digit, 16), '04b') for digit in hex_string)

# # print(binary_string)


# binary_string = '1010000110110100'

# # Split the binary string into groups of 4 bits and convert each group to binary then convert to  its hexadecimal representation
# # X refer to hex format and their uppercase letters, 
# hex_string = ''.join(format(int(binary_string[i:i+4], 2), 'X') for i in range(0, len(binary_string), 4))


# # print(hex_string)
# # print(binStrToHexStr(binary_string))
# # print(binary_string)
# def binStrToHexStr(binStrIn):
#     hexStr = ''.join(format(int(binStrIn[i:i+4], 2), 'X') for i in range(0, len(binStrIn), 4))
#     return hexStr
# # print("bin string by function: ",binStrToHexStr(binary_string))


# # xor of des 
# # def xoring(Ri,kj):    #  j = i+1    // take any length and used in general 
# #     ret = [] 
# #     itrLen = len(Ri)
# #     for i in range(itrLen):
# #         if (Ri[i]=='0' and kj[i] == '0') or (Ri[i]=='1' and kj[i] == '1'): 
# #             ret.append('0')
# #         else: 
# #             ret.append('1')
# #     ret = ''.join(ret)
# #     return ret 


# # convert txt to hex 
# # Text to be converted to hexadecimal
# text = "powerfulzenarmor"

# # Encoding text to bytes using UTF-8 encoding
# bytes_text = text.encode('utf-8')

# # Converting bytes to hexadecimal representation
# hex_text = bytes_text.hex()

# # print("Hexadecimal representation:", hex_text)
# # 706f77657266756c7a656e61726d6f72


# # convert lowercase to upper case 
# # text = "AB1cdd2"
# text = "wwwsunnyvalleyio"
# # # Checking if the text contains lowercase alphabetic characters
# # if any(char.islower() for char in text if char.isalpha()):
# #     # Converting text to uppercase for alphabetic characters
# #     text = ''.join(char.upper() if char.isalpha() else char for char in text)

# # print("Text (potentially converted to uppercase):", text)
# txtRes = ""
# for i in range(len(text)):
#     if text[i].isalpha() and text[i].islower():
#         txtRes += text[i].upper()
#     else: 
#         txtRes +=text[i]
# text = txtRes
# # print(text)        


# def hex_to_text(hex_string):
#     # Remove any spaces and convert the hex string to bytes
#     # hex_string = hex_string.replace(' ', '')
#     byte_data = bytes.fromhex(hex_string)

#     # Convert the byte data to a text string
#     text_string = byte_data.decode('utf-8')  # Assuming UTF-8 encoding, can be different

#     return text_string

# # Example hex string
# hex_str = "48656c6c6f20576f726c64"  # Hex representation of "Hello World"

# # Convert hex string to text string
# text_str = hex_to_text(hex_str)
# # print(text_str)





# # def hex_to_text(hex_string):
# #     # Convert hex string to bytes
# #     byte_data = bytes.fromhex(hex_string)
    
# #     try:
# #         # Decode bytes to text
# #         text_string = byte_data.decode('utf-8')
# #         return text_string
# #     except UnicodeDecodeError:
# #         print("Unable to decode the provided hex string.")
# #         return None

# # # Example usage:
# # hex_string = "9C577E696AC75C4F85EA59AD3A0C6E8A"  # Replace this with your hex string
# # resulting_text = hex_to_text(hex_string)

# # if resulting_text:
# #     print("Resulting text:", resulting_text)

# # ex:  elem:'A6'
# def lookUpLTable(elem):    # 1 elem: ch1,ch2         //exactly:dig1,dig2
#     L_matrix = [
#     ["++", "00", "19", "01", "32", "02", "1A", "C6", "4B", "C7", "1B", "68", "33", "EE", "DF", "03"],
#     ["64", "04", "E0", "0E", "34", "8D", "81", "EF", "4C", "71", "08", "C8", "F8", "69", "1C", "C1"],
#     ["7D", "C2", "1D", "B5", "F9", "B9", "27", "6A", "4D", "E4", "A6", "72", "9A", "C9", "09", "78"],
#     ["65", "2F", "8A", "05", "21", "0F", "E1", "24", "12", "F0", "82", "45", "35", "93", "DA", "8E"],
#     ["96", "8F", "DB", "BD", "36", "D0", "CE", "94", "13", "5C", "D2", "F1", "40", "46", "83", "38"],
#     ["66", "DD", "FD", "30", "BF", "06", "8B", "62", "B3", "25", "E2", "98", "22", "88", "91", "10"],
#     ["7E", "6E", "48", "C3", "A3", "B6", "1E", "42", "3A", "6B", "28", "54", "FA", "85", "3D", "BA"],
#     ["2B", "79", "0A", "15", "9B", "9F", "5E", "CA", "4E", "D4", "AC", "E5", "F3", "73", "A7", "57"],
#     ["AF", "58", "A8", "50", "F4", "EA", "D6", "74", "4F", "AE", "E9", "D5", "E7", "E6", "AD", "E8"],
#     ["2C", "D7", "75", "7A", "EB", "16", "0B", "F5", "59", "CB", "5F", "B0", "9C", "A9", "51", "A0"],
#     ["7F", "0C", "F6", "6F", "17", "C4", "49", "EC", "D8", "43", "1F", "2D", "A4", "76", "7B", "B7"],
#     ["CC", "BB", "3E", "5A", "FB", "60", "B1", "86", "3B", "52", "A1", "6C", "AA", "55", "29", "9D"],
#     ["97", "B2", "87", "90", "61", "BE", "DC", "FC", "BC", "95", "CF", "CD", "37", "3F", "5B", "D1"],
#     ["53", "39", "84", "3C", "41", "A2", "6D", "47", "14", "2A", "9E", "5D", "56", "F2", "D3", "AB"],
#     ["44", "11", "92", "D9", "23", "20", "2E", "89", "B4", "7C", "B8", "26", "77", "99", "E3", "A5"],
#     ["67", "4A", "ED", "DE", "C5", "31", "FE", "18", "0D", "63", "8C", "80", "C0", "F7", "70", "07"]
# ]
#     # dig1=elem[0]
#     ch1=elem[0]
#     rowIdx= int(ch1,16)  # hex char to decimal
#     ch2 = elem[1]
#     colIdx = int(ch2,16)
#     elemRes= L_matrix[rowIdx][colIdx]
#     return elemRes
    

#     # for i in range(0,8,2):
        
#     #     ch1=wordIn[i]
#     #     rowIdx= int(ch1,16)  # hex char to decimal
#     #     ch2 = wordIn[i+1]
#     #     colIdx = int(ch2,16)
#     #     elemRes= subBytesMtrx[rowIdx][colIdx]
#     #     wordRes += elemRes
    
#     # return wordRes

# # look up in E table func. 
# def lookUpETable(elem):    # 1 elem: ch1,ch2         //exactly:dig1,dig2
#     E_matrix = [
#     ["01", "03", "05", "0F", "11", "33", "55", "FF", "1A", "2E", "72", "96", "A1", "F8", "13", "35"],
#     ["5F", "E1", "38", "48", "D8", "73", "95", "A4", "F7", "02", "06", "0A", "1E", "22", "66", "AA"],
#     ["E5", "34", "5C", "E4", "37", "59", "EB", "26", "6A", "BE", "D9", "70", "90", "AB", "E6", "31"],
#     ["53", "F5", "04", "0C", "14", "3C", "44", "CC", "4F", "D1", "68", "B8", "D3", "6E", "B2", "CD"],
#     ["4C", "D4", "67", "A9", "E0", "3B", "4D", "D7", "62", "A6", "F1", "08", "18", "28", "78", "88"],
#     ["83", "9E", "B9", "D0", "6B", "BD", "DC", "7F", "81", "98", "B3", "CE", "49", "DB", "76", "9A"],
#     ["B5", "C4", "57", "F9", "10", "30", "50", "F0", "0B", "1D", "27", "69", "BB", "D6", "61", "A3"],
#     ["FE", "19", "2B", "7D", "87", "92", "AD", "EC", "2F", "71", "93", "AE", "E9", "20", "60", "A0"],
#     ["FB", "16", "3A", "4E", "D2", "6D", "B7", "C2", "5D", "E7", "32", "56", "FA", "15", "3F", "41"],
#     ["C3", "5E", "E2", "3D", "47", "C9", "40", "C0", "5B", "ED", "2C", "74", "9C", "BF", "DA", "75"],
#     ["9F", "BA", "D5", "64", "AC", "EF", "2A", "7E", "82", "9D", "BC", "DF", "7A", "8E", "89", "80"],
#     ["9B", "B6", "C1", "58", "E8", "23", "65", "AF", "EA", "25", "6F", "B1", "C8", "43", "C5", "54"],
#     ["FC", "1F", "21", "63", "A5", "F4", "07", "09", "1B", "2D", "77", "99", "B0", "CB", "46", "CA"],
#     ["45", "CF", "4A", "DE", "79", "8B", "86", "91", "A8", "E3", "3E", "42", "C6", "51", "F3", "0E"],
#     ["12", "36", "5A", "EE", "29", "7B", "8D", "8C", "8F", "8A", "85", "94", "A7", "F2", "0D", "17"],
#     ["39", "4B", "DD", "7C", "84", "97", "A2", "FD", "1C", "24", "6C", "B4", "C7", "52", "F6", "01"]
# ]
#     # dig1=elem[0]
#     ch1=elem[0]
#     rowIdx= int(ch1,16)  # hex char to decimal
#     ch2 = elem[1]
#     colIdx = int(ch2,16)
#     elemRes= E_matrix[rowIdx][colIdx]
#     return elemRes    











# L_matrix = [
#     ["++", "00", "19", "01", "32", "02", "1A", "C6", "4B", "C7", "1B", "68", "33", "EE", "DF", "03"],
#     ["64", "04", "E0", "0E", "34", "8D", "81", "EF", "4C", "71", "08", "C8", "F8", "69", "1C", "C1"],
#     ["7D", "C2", "1D", "B5", "F9", "B9", "27", "6A", "4D", "E4", "A6", "72", "9A", "C9", "09", "78"],
#     ["65", "2F", "8A", "05", "21", "0F", "E1", "24", "12", "F0", "82", "45", "35", "93", "DA", "8E"],
#     ["96", "8F", "DB", "BD", "36", "D0", "CE", "94", "13", "5C", "D2", "F1", "40", "46", "83", "38"],
#     ["66", "DD", "FD", "30", "BF", "06", "8B", "62", "B3", "25", "E2", "98", "22", "88", "91", "10"],
#     ["7E", "6E", "48", "C3", "A3", "B6", "1E", "42", "3A", "6B", "28", "54", "FA", "85", "3D", "BA"],
#     ["2B", "79", "0A", "15", "9B", "9F", "5E", "CA", "4E", "D4", "AC", "E5", "F3", "73", "A7", "57"],
#     ["AF", "58", "A8", "50", "F4", "EA", "D6", "74", "4F", "AE", "E9", "D5", "E7", "E6", "AD", "E8"],
#     ["2C", "D7", "75", "7A", "EB", "16", "0B", "F5", "59", "CB", "5F", "B0", "9C", "A9", "51", "A0"],
#     ["7F", "0C", "F6", "6F", "17", "C4", "49", "EC", "D8", "43", "1F", "2D", "A4", "76", "7B", "B7"],
#     ["CC", "BB", "3E", "5A", "FB", "60", "B1", "86", "3B", "52", "A1", "6C", "AA", "55", "29", "9D"],
#     ["97", "B2", "87", "90", "61", "BE", "DC", "FC", "BC", "95", "CF", "CD", "37", "3F", "5B", "D1"],
#     ["53", "39", "84", "3C", "41", "A2", "6D", "47", "14", "2A", "9E", "5D", "56", "F2", "D3", "AB"],
#     ["44", "11", "92", "D9", "23", "20", "2E", "89", "B4", "7C", "B8", "26", "77", "99", "E3", "A5"],
#     ["67", "4A", "ED", "DE", "C5", "31", "FE", "18", "0D", "63", "8C", "80", "C0", "F7", "70", "07"]
# ]

# E_matrix = [
#     ["01", "03", "05", "0F", "11", "33", "55", "FF", "1A", "2E", "72", "96", "A1", "F8", "13", "35"],
#     ["5F", "E1", "38", "48", "D8", "73", "95", "A4", "F7", "02", "06", "0A", "1E", "22", "66", "AA"],
#     ["E5", "34", "5C", "E4", "37", "59", "EB", "26", "6A", "BE", "D9", "70", "90", "AB", "E6", "31"],
#     ["53", "F5", "04", "0C", "14", "3C", "44", "CC", "4F", "D1", "68", "B8", "D3", "6E", "B2", "CD"],
#     ["4C", "D4", "67", "A9", "E0", "3B", "4D", "D7", "62", "A6", "F1", "08", "18", "28", "78", "88"],
#     ["83", "9E", "B9", "D0", "6B", "BD", "DC", "7F", "81", "98", "B3", "CE", "49", "DB", "76", "9A"],
#     ["B5", "C4", "57", "F9", "10", "30", "50", "F0", "0B", "1D", "27", "69", "BB", "D6", "61", "A3"],
#     ["FE", "19", "2B", "7D", "87", "92", "AD", "EC", "2F", "71", "93", "AE", "E9", "20", "60", "A0"],
#     ["FB", "16", "3A", "4E", "D2", "6D", "B7", "C2", "5D", "E7", "32", "56", "FA", "15", "3F", "41"],
#     ["C3", "5E", "E2", "3D", "47", "C9", "40", "C0", "5B", "ED", "2C", "74", "9C", "BF", "DA", "75"],
#     ["9F", "BA", "D5", "64", "AC", "EF", "2A", "7E", "82", "9D", "BC", "DF", "7A", "8E", "89", "80"],
#     ["9B", "B6", "C1", "58", "E8", "23", "65", "AF", "EA", "25", "6F", "B1", "C8", "43", "C5", "54"],
#     ["FC", "1F", "21", "63", "A5", "F4", "07", "09", "1B", "2D", "77", "99", "B0", "CB", "46", "CA"],
#     ["45", "CF", "4A", "DE", "79", "8B", "86", "91", "A8", "E3", "3E", "42", "C6", "51", "F3", "0E"],
#     ["12", "36", "5A", "EE", "29", "7B", "8D", "8C", "8F", "8A", "85", "94", "A7", "F2", "0D", "17"],
#     ["39", "4B", "DD", "7C", "84", "97", "A2", "FD", "1C", "24", "6C", "B4", "C7", "52", "F6", "01"]
# ]


# # test lookUp L table func. ===> ok 
# # print(lookUpLTable("0b"))


# # test lookUp L table func. ===> ok  
# # print(lookUpETable("61")) # ==>  ok 
# # print(lookUpETable("5a"))



# # function do addition operation on 2 hex elements, return 1 hex element  *element=2 hex digits

# def add_hex_elements(elem1, elem2):
#     # convert hexadecimal elements to integers(decimal) for addition
#     int_elem1 = int(elem1, 16)
#     int_elem2 = int(elem2, 16)
#     print("elem1 as decimal: ",int_elem1,"elem2 as decimal: ", int_elem2 )
#     # Perform addition
#     result = int_elem1 + int_elem2
    
#     # Check for overflow (result > 255)
#     if result > 255:
#         result -= 255
    
#     # convert back to hexa string format
#     res_element = hex(result)[2:].upper()  # convert to uppercase(only for safety) and remove '0x' prefix
    
#     # Pad with zero if necessary to maintain two-digit format
#     res_element = res_element.zfill(2)
    
#     return res_element

# # example usage:
# # element1 = "01"
# # element2 = "0A"
# # result = add_hex_elements(element1, element2)
# # print("Result:", result)

# # ouput case multiply2Elem
# # Enter your key(32 digits) in hex digits format: 706f77657266756c7a656e61726d6f72
# # encrypted wordsList:  ['9C577E69', '6AC75C4F', '85EA59AD', '3A0C6E8A']
# # encrypted hex str:  9C577E696AC75C4F85EA59AD3A0C6E8A
# # encryptedRes:  9C577E696AC75C4F85EA59AD3A0C6E8A
 
# # ouput case multiply2Elem_newV 
# # Enter your key(32 digits) in hex digits format: 706f77657266756c7a656e61726d6f72
# # encrypted wordsList:  ['70F6DB6F', '73B3C01C', 'EA628A97', '0471B852']
# # encrypted hex str:  70F6DB6F73B3C01CEA628A970471B852
# # encryptedRes:  70F6DB6F73B3C01CEA628A970471B852

# # ouput case multiply2Elem_newV  and after handling "00" case in L table
# # Enter your key(32 digits) in hex digits format: 706f77657266756c7a656e61726d6f72
# # encrypted wordsList:  ['9C577E69', '6AC75C4F', '85EA59AD', '3A0C6E8A']
# # encrypted hex str:  9C577E696AC75C4F85EA59AD3A0C6E8A
# # encryptedRes:  9C577E696AC75C4F85EA59AD3A0C6E8A
 
# # Enter your key(32 digits) in hex digits format: 706f77657266756c7a656e61726d6f72
# # encrypted wordsList:  ['9C577E69', '6AC75C4F', '85EA59AD', '3A0C6E8A']
# # encrypted hex str:  9C577E696AC75C4F85EA59AD3A0C6E8A
# # encryptedRes:  9C577E696AC75C4F85EA59AD3A0C6E8A

# # from encryption import multiply2Elem_mixCol_newV, lookUpLTable, lookUpETable, add2HexElem_mixCol
# # test multiply2Elem_newV func. 
# # print(multiply2Elem_mixCol_newV("d4","02")) 

# txt16Chars = "wwwsunnyvalleyio"
# txt16Chars = str(txt16Chars)  # casting just for savety;encode,.hex funcs
# # txtBytes = txt16Chars.encode('utf-8')
# #  try ascii encoding 
# txtBytes = txt16Chars.encode('ascii')
# txtHex = txtBytes.hex()
# # print(txtHex)  # 77777773756e6e7976616c6c6579696f   * result case encoding ascii 

# # try decoding with ascii 
# # ascii_bytes = b"77777773756e6e7976616c6c6579696f"
# # decoded_text = ascii_bytes.decode('ascii')
# # print(decoded_text)

# # encoding:  1. txt to bytes 2. bytes to hex 
# # decoding:  1. hex to bytes 2. bytes to txt 

# # txtHex = "9C577E696AC75C4F85EA59AD3A0C6E8A"    # txtHex = "9C577E696AC75C4F85EA59AD3A0C6E8A"   res of enc.
# txtHex = "77777773756e6e7976616c6c6579696f"  # result using latin decoding wwwsunnyvalleyio
# hex_bytes = bytes.fromhex(txtHex)
# # print(hex_bytes)
# # Decode bytes to text
# text = hex_bytes.decode('latin-1')  # Assuming it's 
# # b'\x9cW~ij\xc7\\O\x85\xeaY\xad:\x0cn\x8a'
# print(text)



# # test input enc res to  dec func. 