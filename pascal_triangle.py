def print_pascals_triangle(n):
    if n < 0:
        print("please , use only positive integer numbers")
        return
    for i in range(n):
        coef = 1
        for j in range(1, n-i+1):
            print(" ", end="")
        for j in range(0, i+1):
            if j > 0:
                coef = coef * (i-j+1) // j
            print(coef, " ", end="")
        print()


print("Enter the number (positive integer) of rows:")
n = int(input())
print_pascals_triangle(n)
