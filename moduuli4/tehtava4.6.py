import random

def approximate_pi(amount_of_draws):

     N = 0 #kaikkien arvottujen pisteiden lukumäärä
     n = 0 #yksikköympyrän sisään osuneiden pisteiden lukumäärä


     while N < amount_of_draws:
         x = random.uniform(-1,1)
         y = random.uniform(-1,1)

         if x**2 + y**2 < 1:
             n +=1
         N +=1

     pi_approximation = 4 * (n / N)
     return pi_approximation

def main():
    amount_of_draws = int(input("The number of random points to generate: "))
    pi_approximation = approximate_pi(amount_of_draws)
    print(f"Approximation of pi with {amount_of_draws} random points: {pi_approximation}")

if __name__ == "__main__":
    main()