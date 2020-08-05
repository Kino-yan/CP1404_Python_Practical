"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
def main():
    sales = 0
    while sales >=0:
        sales = float(input("Enter sales: $"))
        if sales < 0:
            print("-----END-----")
        elif sales < 1000:
            bonus = sales * 0.1
            print(bonus)
        elif sales >= 1000:
            bonus = sales * 0.15
            print(bonus)

if __name__=='__main__':
    main()

