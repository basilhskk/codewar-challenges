def loneliest(text):
    #Your code here
    text = list(text)
    print (text)
    mchar = ""
    mcount = 0
    count = 0
    ccount = 0
    tempchar = ""
    marr = []
    
    for char in text :
        
        if char !=" ":
            ccount = ccount + 1
            tempchar = char
            print(char)


        if(ccount == 2):
            count = 0
            ccount = 0
            # print(char)

            
        
        if char == " ":
            count = count+1
        
        if(count >= mcount):
            mcount = count
            mchar = tempchar
            marr.append([mcount,mchar])

    print(marr)
            
    return marr




# loneliest('a')
a = loneliest('a bcs           d k')

sorted_by_second = sorted(a, key=lambda tup: tup[0])

print(sorted_by_second)

# loneliest('a   b   c ')
# loneliest('  abc  d  z    f gk s ')
# loneliest('a  b  c  de  ')
# loneliest('abc')