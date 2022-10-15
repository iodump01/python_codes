n = int(input("Enter the height for the pattern"))
for i in range(n):
    for j in range(i+1):
        print("*",end = "")
    print("\r")
