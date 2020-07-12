import os
i =0

#specify the folder path
folderName = "."

for root, dirs, files in os.walk(folderName):
    for filename in files:

        #specify the file you to remove. 
        removefile = str(i) +"set43"+".png"
        try:
        	os.remove(removefile)
        except:
        	i+=1
        	continue
        
        #i = i + 1
        #if ( i==725):
            #break
    
