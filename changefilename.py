import os 
  
# Function to rename multiple files 
def rename():
    '''
    Change the foldername and dst filename you want to save

    '''
    i = 0
    foldername ="set8"
    for filename in os.listdir(foldername): 
        dst = str(i)+foldername + ".png"
        src =foldername+'/'+filename 
        dst =foldername+'/'+ dst 
          
        
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__':
    
      
    rename() 
