def leftrotate(m):
  n = len(m[0])
  for i in range(n // 2):
    for j in range(i, n-i-1):
      tmp = m[i][j]
      m[i][j] = m[j][n-1-i]
      m[j][n-1-i] = m[n-1-i][n-1-j]
      m[n-1-i][n-1-j] = m[n-1-j][i]
      m[n-1-j][i] = tmp
  return m   
  
  ###given a list of values as a matrix[[1,2,3],[4,5,6],[7,8,9]]
  ###1 2 3 
  ###4 5 6
  ###7 8 9
  ###We can rotate this in counterclockwise using the above code
  ###3 6 9
  ###2 5 8 New change 
  ###1 4 7
m = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
print(leftrotate(m))

#1 2 3 4
#5 6 7 8
#9 10 11 12
#13 14 15 16
#rotate
#4 8 12 16 
#3 7 11 15
#2 6 10 14
#1 5 9  13
  
