import random

int(random.randint(0,9))
int(random.randint(1, 6))

three_digit = [random.randint (0, 9) for three in range(3)]
four_digit = [random.randint (1, 6) for four in range(4)]


#random_randint_str = str("Three digit code " + str(random.randint(0,9 ) ) )
#random_randint_str2 = str("Four digit code " + str(random.randint(1, 6)  ))
#tein aluksi kaksi yläpuolella olevaa riviä koodia, mutta ne eivät vaikuta mitenkään lopputulokseen. Jätin ne silti.

print("Your three digit lock code is " + str(three_digit))
print("Your four digit lock code is " + str(four_digit))