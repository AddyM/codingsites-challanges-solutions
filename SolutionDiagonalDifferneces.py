# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_diag_diff(Metrics,N):
    
    sum_diag = sum_invert_diag = 0
    
    for row in range(N):
        for column in range(N):
            if row == column :
                sum_diag +=Metrics[row][column]
                
            if (((row+column)-(N-1) == 0 )):
                sum_invert_diag +=Metrics[row][column]
                
  
    return abs(sum_diag - sum_invert_diag)
Array =[]
Test = int(input())
for test in range(Test):
    
    row = map(int,raw_input().split(' '))
    Array.append(row)
    
print get_diag_diff(Array,Test)
