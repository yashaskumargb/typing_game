#read the string file
import time as t 
#ensure that the paragragraph that u use for typing test must be saved to a file before u start the run , and also open the same file while running
def paragraph(file_path):
   file=open(file_path,"r") #opening the file path in reading mode
   text=file.readlines()
   text=str(text)
   text=text[2:len(text)-2]
   return text
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#error calculations
def error_calc(paragraph,entered_by_me):
    errors =0
    if(paragraph==entered_by_me):
        print("congragulations, typing completed")
    split_para=paragraph.split()
    split_mypara=entered_by_me.split()
    lo=len(split_para)
    lm=len(split_mypara)
    for i in range(lm):
        if(i<=lo and i<=lm):
            if(split_mypara[i]==split_para[i]):
                continue
            else:
                errors=errors+1
                print("word \"",split_mypara[i],"\" at",i,"th location is not matching")
        
        else:
            if(split_mypara[i]==split_para[i]):
                continue
            else:
                errors=errors+1
                print("word \"",split_mypara[i],"\" at",i,"th location is not matching")
            
    if(lm!=lo):    
        print("typing is failed becoz of",end=" ")
        
        if(lm<lo):
            print("%d less words are enterd \n" %(lo-lm))
        else:
            print("more words are enterd \n")        
        print("--------------------------------------------------")
    return errors
#-----------------------------------------------------------------------------
#speed
import time as t
def speed_calc(stime,etime,no_of_words):
    net_time=etime-stime
    speed=no_of_words/net_time
    return speed

#-----------------------------------------------------------------------------
original=paragraph("test_charlie.txt")
print(original)
print("-------------------------------------------------------------------")
print("press enter to start typing \n")
input()
stime=t.time()
print(">>>Dont press the enter button until typing is completed ")
print("-------------------------------------------------------------------")
mine=input()
etime=t.time()
len_mine=len(mine)
net_errors=error_calc(original,mine)
print("errors= %d" %(net_errors))
speed_of_typing=speed_calc(stime, etime, len_mine)
print("speed= %f word per seconds" %(speed_of_typing))
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
