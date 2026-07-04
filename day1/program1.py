for i,j in zip(range(1,6),range(5,0,-1)):#i=1,j=5
    if i==3 and j==3:
        continue #skip
print(i," ",j)
    #  1 5
    #  2 4
    #  4 2
    #  5 1


#-----------------------------------------------------------------------------------

dict ={'c':97,'a':96,'b':98}
for _ in sorted(dict):
   print(dict[_])