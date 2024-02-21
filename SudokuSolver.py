from typing import Tuple, List
def input_sudoku() -> List[List[int]]:
	sudoku= list()
	for i in range(9):
		row = list(map(int, input().rstrip(" ").split(" ")))
		sudoku.append(row)
	return sudoku

def print_sudoku(sudoku:List[List[int]]) -> None:
	for i in range(9):
		for j in range(9):
			print(sudoku[i][j], end = " ")
		print()

def get_block_num(sudoku,pos):
    r=pos[0]
    c=pos[1]
    x=int((r-1)/3)
    y=int((c-1)/3)+1
    b=y+3*x
    return b

def get_position_inside_block(sudoku,pos):
    c=0
    x=get_block_num(sudoku,pos)
    for i in range(1,10):
        for j in range(1,10):
            if get_block_num(sudoku,(i,j))==x:
                c+=1
            if pos==(i,j):
                return c    
    return 0

def get_block(sudoku,x):
    l=[]
    for i in range(1,10):
        for j in range(1,10):
            if get_block_num(sudoku,(i,j))==x:
                l.append(sudoku[i-1][j-1])
    return l

def get_row(sudoku,i):
    return sudoku[i-1]

def get_column(sudoku,x):
    l=[]
    for i in range(0,9):
        l.append(sudoku[i][x-1])
    return l


def find_first_unassigned_position(sudoku):
    l=[]
    for i in range(0,9):
        for j in range(0,9):
            if sudoku[i][j]==0:
                l.append((i+1,j+1))
    def total():
        return len(l)            
    if l==[]:
        return (-1,-1)
    else:
        return l[0]                

def valid_list(l):
    x=[]
    for i in range(0,len(l)):
        if l[i]!=0:
            x.append(l[i])        
    n=len(x)
    for i in range(0,n):
        for j in range(0,n):
            if i!=j:
                if x[i]==x[j]:
                    return False
    return True

def valid_sudoku(sudoku):
    a=False
    for i in range(1,10):
        b=get_block(sudoku,i)
        r=get_row(sudoku,i)
        c=get_column(sudoku,i)
        if valid_list(b)==True:
            if valid_list(r)==True:
                if valid_list(c)==True:
                    a=True
                else:
                    a=False
            else:
                a=False
        else:
            a=False                    
    return a                

def get_candidates(sudoku,pos):
    cand_lis=[]
    sod=sudoku
    '''
    block_pos=get_block(sod,get_block_num(sod,pos))
    row_pos=get_row(sod,pos[0])
    col_pos=get_column(sod,pos[1])'''
    for i in range(1,10):
        sod[pos[0]-1][pos[1]-1]=i
        block_pos=get_block(sod,get_block_num(sod,pos))
        row_pos=get_row(sod,pos[0])
        col_pos=get_column(sod,pos[1])
        if valid_list(block_pos)==True and valid_list(row_pos)==True and valid_list(col_pos)==True:
            cand_lis.append(i)
        sod[pos[0]-1][pos[1]-1]=0                         
    return cand_lis        

def make_move(sudoku,pos,num):
    sudoku[pos[0]-1][pos[1]-1]=num
    return sudoku

def undo_move(sudoku,pos):
    sudoku[pos[0]-1][pos[1]-1]=0
    return sudoku

def sudoku_solver(sudoku):
    if find_first_unassigned_position(sudoku)==(-1,-1):
        return (True,sudoku)
    while find_first_unassigned_position(sudoku)!=(-1,-1):
        gc=get_candidates(sudoku,find_first_unassigned_position(sudoku))
        for j in gc:
            f_u=find_first_unassigned_position(sudoku)
            sudoku=make_move(sudoku,f_u,j)
            if sudoku_solver(sudoku)[0]==True:
                return (True,sudoku)
            sudoku=undo_move(sudoku,f_u)
        return (False,sudoku)
            
if __name__ == "__main__":

	
	sudoku = input_sudoku()

	
	possible, sudoku = sudoku_solver(sudoku)

	if possible:
		print("Found a valid solution for the given sudoku :)")
		print_sudoku(sudoku)

	else:
		print("The given sudoku cannot be solved :(")
		print_sudoku(sudoku)

