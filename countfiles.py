import os 

list = os.listdir(r'C:\SWDevelopment\super-octo-500')
print(list)
number_files = len(list)
print number_files

list = os.listdir(r'C:\SWDevelopment\super-octo-500')
list2 = []

for file in os.listdir(r'C:\SWDevelopment\super-octo-500'):
    if file.endswith('.py'): 
        list2.append(file)
        print(file)

print list2
        
# number_files = len(list)
# print number_files
