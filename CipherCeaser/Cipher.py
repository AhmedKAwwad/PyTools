text = str(input("Text: "))
s = int(input("number: "))
# print(text)
def encrypt(text,s):
   result = ""
   # transverse the plain text
   for i in range(len(text)):
      char = text[i]
      # print(char)
      # Encrypt uppercase characters in plain text
      if char.isalpha():
         if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
            # print(result)
            # Encrypt lowercase characters in plain text
         else:
            result += chr((ord(char) + s - 97) % 26 + 97)
      else:
         result += char
   return result
#check the above function
# text = "CyberTalents"
# s = 4
print ("Plain Text : " + text)
print ("Shift pattern : " + str(s))
print ("Cipher: " + encrypt(text,s))