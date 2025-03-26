#1021
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split(" "))
target=list(map(int,sys.stdin.readline().rstrip().split(" ")))
deq=deque([i for i in range(1,N+1)])
stack=[]



cnt=0
for item in target:
    temp=deq.popleft()
    deq.appendleft(temp)    
    print(temp)
    cnt_0=0
    cnt_1=0
    deq_left=deq
    while item!=temp:
        deq_left.rotate(-1)
        temp=deq.popleft()
        deq_left.appendleft(temp)
        cnt_0+=1
    print(deq)
    deq_right=deq    
    while item!=temp:
        deq_right.rotate(1)
        temp=deq.popleft()
        deq_right.appendleft(temp)
        print(deq_right)
        print(deq)
        cnt_1+=1
    print(deq)
    print(cnt_0,cnt_1)
    
    if cnt_0 > cnt_1:
        cnt+=cnt_1
        deq=deq_right
    else:
        cnt+=cnt_0
        deq=deq_left
    

    deq.popleft()

print(cnt)




