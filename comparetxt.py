

def comparetxt(f1,f2):

    # load file 
    text_file = open(f1, "r")
    line1 = text_file.read().split(' ')

    text_file = open(f2, "r")
    line2 = text_file.read().split(' ')

    # remove new line character
    file1 = ' '.join(line1)
    file1 = file1.replace("\n","")
    file1 = file1.split(" ")

    file2 = ' '.join(line2)
    file2 = file2.replace("\n","")
    file2 = file2.split(" ")

    print(file1)
    print(file2) 
    #compare

    if len(file2)!=len(file1):
        print("file size did not match: exiting")
        return
    else:
        for num in range(len(file1)-1):
            if file1[num]==file2[num]:
                continue
            else:
                print(" Index {} not matching ".format(num))
                return

        print("Match!")
        return 
   
        



if __name__=="__main__":

    file1name = "1.txt"
    file2name = "2.txt"

    comparetxt(file1name,file2name)
    
