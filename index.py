import math

def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def generate_primes(n):
  primes = []
  for i in range(2, n + 1):
    if is_prime(i):
      primes.append(i)
  return primes

def app(request):
  n = request.get('n')
  primes = generate_primes(int(n))
  return 'The prime numbers up to {} are: {}'.format(n, primes)
