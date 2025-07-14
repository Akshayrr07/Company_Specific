def isSafe(m,r,c):
    n = len(m)

    for i in range(r):
        if m[i][c]:
            return False
        
    for i,j in zip(range(r-1,-1,-1), range(c-1,-1,-1)):
        if m[i][j]:
            return False
        
    for i,j in zip(range(r-1,-1,-1),range(c+1,n)):
        if m[i][j]:
            return False
        
    return True

def place(r,m,s):
    n = len(m)

    if r == n:
        b = []
        for i in range(n):
            row = ""
            for j in range(n):
                row += 'Q' if m[i][j] else '.'
            b.append(row)
        s.append(b)
        return 
    
    for i in range(n):
        if isSafe(m,r,i):
            m[r][i] = 1
            place(r+1,m,s)
            m[r][i] = 0

def nQueen(n):
    
    m = [[0]*n for _ in range(n)]
    s = []
    place(0,m,s)
    return s

if __name__ == '__main__':
    n = int(input())
    for i in nQueen(n):
        for j in i:
            print(' '.join(j))
        print()