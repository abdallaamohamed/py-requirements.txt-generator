# importing libraries
import os
import sys
import sys
import pip
from pip._internal import main as pip


# defining location of parent folder
BASE_DIRECTORY = r"<Folder PATH>"
output_file = open('requirements.txt', 'w')
output = {}
file_list = []

# scanning through sub folders
for (dirpath, dirnames, filenames) in os.walk(BASE_DIRECTORY):
    for f in filenames:
        if 'py' in str(f):
            e = os.path.join(str(dirpath), str(f))
            file_list.append(e)

for f in file_list:
    print (f)
    txtfile = open(f, 'r',encoding='utf-8',errors='ignore')
    output[f] = []
    for line in txtfile:
        if 'import' in line or 'from' in line :
            if line.startswith("import") or line.startswith("from"):
               output[f].append(line)



tabs = []
for tab in output:
    tabs.append(tab)

# to remove duplicates 

Modulelist = []
tabs.sort()
for tab in tabs:
    #output_file.write(tab + '\n')
    #output_file.write('\n')
    for row in output[tab]:
        Modulelist.append(row)
        #output_file.write(row)

        #output_file.write(row + '')
    #output_file.write('\n')
    #output_file.write('----------------------------------------------------------\n')
# remove duplicates 
Modulelist = list(set(Modulelist)) 
#Extract lines that starts with "import OR from"

#Requirment List
requirements = []
for module in Modulelist:
    if module.startswith('from'):                    
        head, sep, tail = module.partition('import')       

        requirements.append(head.replace('from ','').rstrip() +'\n')       
    else:
        requirements.append(module.replace('import ','') + '')
# remove duplicates for requirements
requirements = list(set(requirements)) 

for req in requirements:
    if req not in sys.modules:
       print((req).rstrip() + " module does not exist")
       output_file.write(req)
    #else:
    #   print(req + "dont exist")  
requirements = [s.strip('\n') for s in requirements]

pkgs = requirements
for package in pkgs:
    try:
        import package
    except ImportError as e:
         pip(['install', package])
