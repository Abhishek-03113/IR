import os 
import sys 
import pathlib 


counter = 0 

while counter != 5: 
    
    f = open(f'assignment_{counter+1}.ipynb', 'x') 
    f.close() 
    
    counter += 1 
    print(f'File {counter} created')

print('All files created')

    