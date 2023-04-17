import copy
curr=[
    [0,2,3],
    [1,5,6],
    [4,7,8]]
goal=[
    [1,2,3],
    [4,5,6],
    [7,8,0]]
def mm(curr):
    c=0
    for i in range(3):
        for j in range(3):
            if curr[i][j]!=goal[i][j]:
                c+=1
    return c
valid={
    (0,0):[1,2],
    (0,1):[1,2,3],
    (0,2):[2,3],
    (1,0):[0,1,2],
    (1,1):[0,1,2,3],
    (1,2):[0,2,3],
    (2,0):[0,1],
    (2,1):[0,1,3],
    (2,2):[0,3]
}
def ps(curr):
    for i in range(3):
        for j in range(3):
            if curr[i][j]==0:
                return (i,j)
q=[]
v=[]
pos=(0,0)
def bfs(q,v,curr,goal,pos):
    v.append(curr)
    q.append(curr)
    while q:
        s=q.pop(0)
        z=copy.deepcopy(s)
        print(s)
        if s==goal:
            print("solved")
            break
        m=99   
        for i in valid[pos]:
            curr=copy.deepcopy(z)
            if i==0:
                curr[pos[0]][pos[1]],curr[pos[0]-1][pos[1]]=curr[pos[0]-1][pos[1]],curr[pos[0]][pos[1]]
            elif i==1:
                curr[pos[0]][pos[1]],curr[pos[0]][pos[1]+1]=curr[pos[0]][pos[1]+1],curr[pos[0]][pos[1]]
            elif i==2:
                curr[pos[0]][pos[1]],curr[pos[0]+1][pos[1]]=curr[pos[0]+1][pos[1]],curr[pos[0]][pos[1]]
            else:
                curr[pos[0]][pos[1]],curr[pos[0]][pos[1]-1]=curr[pos[0]][pos[1]-1],curr[pos[0]][pos[1]]
            #print(curr)
            if mm(curr)<m:
                m=mm(curr)
                if curr not in v:
                    v.append(curr)
                    if len(q)==0:
                        q.append(curr)
                    else:
                        q.pop(0)
                        q.append(curr)
        pos=ps(curr)
bfs(q,v,curr,goal,pos)
    