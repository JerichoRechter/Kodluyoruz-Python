
l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
1- l[0] = [1,'a',['cat'],2] 
          -l=1
          -l='a'
          -l=['cat']       
              - l='cat'
          -l=2
        
2- l[1] = [[[3]],'dog']   
          -l=[[3]]         
              -l=[3]       
                 -l=3
          -l='dog'
3- l[2] = 4
4- l[3] = 5


l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
lnew = []
def flatten(n):
    for i in n:
        if isinstance(i, list):
            flatten(i)
        else:
            lnew.append(i)

flatten(l)
print(lnew)
