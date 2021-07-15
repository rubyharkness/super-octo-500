import os
import glob

#print(os.listdir("C:\SWDevelopment\ULActions"))

# list = os.listdir(r'C:\SWDevelopment\ULActions')
# print(list)
# number_files = len(list)
# print number_files

path = 'C:\SWDevelopment\ULActions'
list = os.listdir(r'C:\SWDevelopment\ULActions')
list2 = []

for file in os.listdir(r'C:\SWDevelopment\ULActions'):
    if file.endswith('.cs'): 
        list2.append(file)
        print(file)

print list2

 #revisit this later   
# for file in os.listdir(r'C:\SWDevelopment\ULActions'): 
#     print file
#     f = open("C:\\SWDevelopment\\ULActions\\" + file, "a")
#     f.writelines(file)
#     f.close()

for file in os.listdir(r'C:\SWDevelopment\ULActions'): 
    print file
    f = open("C:\\SWDevelopment\\ULActions\\" + file, "r")
    #Print the class name Class = NameOfClass
    #Print the properties Property = NameOfProperty
    text = f.read()
 
search_words = set(['class'])

for item in os.listdir(r'C:\SWDevelopment\ULActions'):
    f = open("C:\\SWDevelopment\\ULActions\\" + item, "r")
    sentences = f.readlines()
    for sentence in sentences: 
        words_in_sentence = set(sentence.split())
        if words_in_sentence.intersection(search_words): 
            words2 = sentence.split()
            print("The class is: {} ".format(words2[2]))
            
search_words2 = set(['public'])

for item in os.listdir(r'C:\SWDevelopment\ULActions'):
    f = open("C:\\SWDevelopment\\ULActions\\" + item, "r")
    sentences = f.readlines()
    for sentence in sentences: 
        words_in_sentence = set(sentence.split())
        if words_in_sentence.intersection(search_words2): 
            words2 = sentence.split()
           # print words2
            if len(words2) == 3: 
                print("The properties are: {} ".format(words2[2]))
    f.close()
 