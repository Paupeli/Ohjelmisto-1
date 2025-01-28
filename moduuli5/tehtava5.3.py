integer = (int(input("Enter an integer: ")))

def is_prime(num):
    flag = True

    if num <2:
        flag = False
    else:
        for _ in range(2,num):
            if num % _ == 0:
                flag = False
                break
    return flag
if is_prime(integer):
    print(f"{integer} is a prime number")
else:
    print(f"{integer} is not a prime number")