# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 19:32:17 2016

@author: bacro
"""

tmp='onethousand'
def count_letters(nstring):
    let_count=0
    space = ' '
    hyp = '-'
    for each in nstring:
        if each != space:
            if each != hyp:
                let_count += 1
    return let_count
    
print(count_letters(tmp))


def num_word(n): #number has to be less than 1000
    dict_19 = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
    dict_90 ={20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
    tmps=str(n)
    words=""
    #determine how long the string is
    len_tmps = len(tmps)
    if len_tmps == 3: #in the hundreds
        words += dict_19[int(tmps[0])] + 'hundred'
        resid_num  = n - int(tmps[0])*100
        if resid_num>0:
            words += 'and'
            str_res=str(resid_num) #length of residual number
            if len(str_res)==1:
                words += dict_19[int(str_res)]
            else:
                if resid_num<=19:
                    words += dict_19[resid_num]
                else:
                    words += dict_90[int(str_res[0])*10] 
                    if str_res[1]!='0':
                        words+=dict_19[int(str_res[1])]
    else:
        if int(tmps)<=19:
            words += dict_19[int(tmps)]
        else:
            words += dict_90[int(tmps[0])*10]
            if int(tmps[1]) != 0:
                words += dict_19[int(tmps[1])]
    
    return len(words)
    
nsum=0
for i in range(1,1000):
    nsum+=num_word(i)
    
print(nsum+14)
    
    
    
        
        