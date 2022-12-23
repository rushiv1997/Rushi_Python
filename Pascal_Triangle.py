def PascalTriangle(n):
   for i in range(n+1):
      for j in range(n-i):
         print(' ', end='')

      C = 1
      for j in range(1, i+1):
         print(C, ' ', end='')
         C = C * (i - j) // j
      print()

n = int(input("Enter the number:"))
PascalTriangle(n)
