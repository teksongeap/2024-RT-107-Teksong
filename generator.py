
def is_prime(n):
  """
  Check if a number is prime.

  Args:
    n: The number to check.

  Returns:
    True if n is prime, False otherwise.
  """
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def primes_gen(): 
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

gen = primes_gen()
for _ in range(10): print(next(gen), end=' ')

def unique_letters(word):
    seen = set()
    for char in word:
        if char not in seen:
            seen.add(char)
            yield char
        

for letter in unique_letters('hello'):
    print(letter, end=' ')
    
    def visualize_reserves(reserves):
    scale = 10
    bar = '█' * (reserves // scale)
    print(f"Reserves: {reserves} {bar}")

def visualize_loans(loans):
    scale = 10
    bar = '█' * (loans // scale)
    print(f"Loans:    {loans} {bar}")

def simulate_fractional_reserve_banking(initial_deposit, reserve_ratio, iterations):
    reserves = initial_deposit
    loans = 0
    money_supply = initial_deposit

    print(f"Initial Deposit: {initial_deposit}")
    print(f"Reserve Ratio: {reserve_ratio}")
    print(f"Iterations: {iterations}")
    print()

    for i in range(iterations):
        max_loanable = reserves - (reserves * reserve_ratio)
        new_loans = max_loanable
        reserves -= new_loans
        loans += new_loans
        money_supply += new_loans

        print(f"Iteration {i+1}:")
        visualize_reserves(reserves)
        visualize_loans(loans)
        print()

    print(f"Total Money Supply: {money_supply}")

# Example usage
initial_deposit = 1000
reserve_ratio = 0.1
iterations = 5

simulate_fractional_reserve_banking(initial_deposit, reserve_ratio, iterations)
