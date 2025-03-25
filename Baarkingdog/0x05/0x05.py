import sys
N= int(sys.stdin.readline().rstrip())

stack=list(map(int,sys.stdin.readline().rstrip().split(" ")))
count=[0 for i in range(len(stack))]
# count=[]

rev_stack=reversed(stack)

for item in rev_stack:    
    pos=len(stack)
    index=len(stack)-1
    while(1):
        if item <= stack[pos-2]:
            count[index]=pos-1
            break  
        pos-=1
    stack.pop()


    # print(len(stack),pos-2)
    
# for item in count[:-1]:
#     print(item,end=" ")

# print(count[-1],end="")

print(*count)



