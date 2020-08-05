def main():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    for i in range(0, 110, 10):
        print(i, end=' ')
    print()

    for i in range(20, 0, -1):
        print(i, end=' ')
    print()

    Num_star = int(input("Number of stars:"))
    for i in range(Num_star):
        print("*", end=' ')
    print()

    row=1
    User_row=int(input("Please enter the row: "))
    while row <= User_row:
        col = 1
        while col <= row:
            print("*", end=' ')
            col +=1
        print()
        row += 1

if __name__=='__main__':
    main()

