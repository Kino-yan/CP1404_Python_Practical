"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    print(cal_result(score))



def cal_result(score):
    if score < 0 or score > 100:
        return "Invaild score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

if __name__=='__main__':
    main()


