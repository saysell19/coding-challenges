# # Given a number n, return a list of all prime numbers smaller than or equal to n.
# # write as a class

class PrimeFinder:
  def __init__(self, n):
    self.n = n


  def prime_finder(self):
    primes = []

    for i in range(1, self.n + 1):
      flag = 0

      if i < 2:
        continue

      if i == 2:
        primes.append(2)
        continue

      for x in range(2, i):
        if i % x == 0:
          flag = 1
          break

      if flag == 0:
        primes.append(i)
    return primes
  
  def __str__(self):
    return str(self.prime_finder())


# prime = PrimeFinder(100)
# print(prime)



