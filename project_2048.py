
import random
def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat
def getstatus(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]==2048:
                return "Won"
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                return "In Progress"
    for i in range(3):
        for j in range(3):
            if grid[i][j]==grid[i+1][j] or grid[i][j]==grid[i][j+1]:
                return "In Progress"
    for i in range(3):   
        if grid[i][3]==grid[i+1][3]:
            return "In Progress"
    for j in range(3):   
        if grid[3][j]==grid[3][j+1]:
            return "In Progress"
    return "Lost"
    


def add_2(grid):
    row=random.randint(0,3)
    col=random.randint(0,3)
    while(grid[row][col]!=0):
        row=random.randint(0,3)
        col=random.randint(0,3)
    grid[row][col]=2
    return grid

def compress(grid):
    mat = []
    changed=False
    for i in range(4):
        mat.append([0]*4)
    for i in range(4):
        col=0
        for j in range(4):
            if grid[i][j]!=0:
                mat[i][col]=grid[i][j]
                if col!=j:
                    changed=True
                col+=1
    return mat,changed

def merge(mat):
    changed=False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                mat[i][j]=2*mat[i][j]
                mat[i][j+1]=0
                changed=True
    return mat,changed

def reverse(grid):
    mat=[]
    for i in range(4):
        mat.append([])
        for j in range(4):
            mat[i].append(grid[i][4-j-1])
    return mat

def transpose(grid):
    mat=[]
    for i in range(4):
        mat.append([])
        for j in range(4):
            mat[i].append(grid[j][i])
    return mat

def move_up(grid):
    mat=transpose(grid)
    mat,changed1=compress(mat)
    mat,changed2=merge(mat)
    change=changed1 or changed2
    mat,temp=compress(mat)
    final_mat=transpose(mat)
   
    return final_mat,change

    
def move_down(grid):
    mat=transpose(grid)
    rev_mat=reverse(mat)
    rev_mat,changed1=compress(rev_mat)
    rev_mat,changed2=merge(rev_mat)
    change=changed1 or changed2
    rev_mat,temp=compress(rev_mat)
    final_rev_mat=reverse(rev_mat)
    final_mat=transpose(final_rev_mat)
   
    return final_mat,change
    

def move_right(grid):
    grid=reverse(grid)
    mat,changed1=compress(grid)
    mat,changed2=merge(mat)
    change=changed1 or changed2
    mat,temp=compress(mat)
    final_mat=reverse(mat)
    return final_mat,change



    
def move_left(grid):
    mat,changed1=compress(grid)
    mat,changed2=merge(mat)
    change=changed1 or changed2
    mat,temp=compress(mat)
    return mat,change


if __name__=="__main__":
    mat = start_game()
    mat=add_2(mat)
    mat=add_2(mat)
    for ele in mat:
        for x in ele:
            if x==0:
                print("_",end=" ")
            else:
                print(x,end=" ")
        print()
    while getstatus(mat)=="In Progress":
        print("press movement")
        ele=int(input())
        if ele == 1:
            mat,change = move_up(mat)
        elif ele == 2:
            mat,change = move_down(mat)
        elif ele == 3:
            mat,change= move_left(mat)
        else:
            mat,change = move_right(mat)
        if change:
            mat=add_2(mat)
            for ele in mat:
                for x in ele:
                    if x==0:
                        print("_",end=" ")
                    else:
                        print(x,end=" ")
                print()
    else:
        if getstatus(mat)=="Won":
            print("you won")
        else:
            print("you lose")
