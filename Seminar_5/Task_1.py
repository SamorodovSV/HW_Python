# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open("file_4.txt", "r") as fin:
     for line in fin:
        file_4 = line.split()
        for word in file_4:
            if "абв" in word:
               file_4.remove(word)
        sentence = " ".join(file_4)
        print(sentence)