
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
    
    
