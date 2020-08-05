import random

print(random.randint(5, 20))  # line 1  The smallest number is 5, the largest number is 20.
print(random.randrange(3, 10, 2))  # line 2 The smallest number is 3, the largest number is 9. Line 2 cannot produce a 4, because the step number set at 2.
print(random.uniform(2.5, 5.5))  # line 3 The smallest number is 2.5, the largest number is 5.5.
print(random.randint(1,100))