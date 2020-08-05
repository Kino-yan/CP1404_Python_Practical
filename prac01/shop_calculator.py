def main():
    while True:
        Num_items = int(input("Number of items: "))
        if Num_items <= 0:
            print("Invalid number of items! Please enter again!")
            continue
        else:
            count=1
            total=0
            while count<=Num_items:
                price=float(input("Price of item: "))
                count +=1
                total += price
            print("Total price for",Num_items,"items is $%.2f"%total)
            break

if __name__=='__main__':
    main()
