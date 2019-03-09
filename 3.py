'''
Выведите таблицу размером \( n \times n \), заполненную числами от \( 1 \) до \( n^2 \) по спирали, 
выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь \( n=5 \)):
Sample Input:

5
Sample Output:

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''

n = int(input())
i, j = 0, 0
start_lane = 0;
end_lane = n-1;
start_column = 0
end_column = n-1;
numb = 1;
lines = (n*2)
a=[]
for q in range (n):
    a.append([])
    for w in range(n):
        a[q] += '0'
for lane in range (lines):
    if (lane%4 == 0):
            for j in range(start_column,end_column+1):
                i = start_lane
                a[i][j] = numb
                numb+=1
            start_lane+=1
    elif ( lane%4 == 1):
            for i in range(start_lane, end_lane+1):
                j = end_column
                a[i][j] = numb
                numb+=1
            end_column-=1   
    elif ( lane%4 == 2):
            for j in range (end_column,start_column-1,-1):
                i = end_lane
                a[i][j] = numb
                numb+=1
            end_lane-=1
    elif ( lane%4 == 3):
            for i in range (end_lane,start_lane-1,-1): 
                j = start_column
                a[i][j] = numb
                numb+=1
            start_column+=1
            
for q in range (n):
    for w in range(n):
        print(a[q][w],end=' ')
    print()

