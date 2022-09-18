# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('file.txt', 'r') as fin:
   for line in fin:
      file = line.split()
      for word in file:
         if 'абв' in word:
            file.remove(word)
      sentence = ' '.join(file)
      print(sentence)
# with open("file.txt", "r") as fin:
#      for line in fin:
#         file = line.split()
#         for word in file:
#             if "абв" in word:
#                file.remove(word)
#         sentence = " ".join(file)
#         print(sentence)