numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1,len(numbers)):
    is_prime = True
    number = numbers[i]
    for j in range(2,number):
        if number%j==0:
             not_primes.append(numbers[i])
             is_prime = False
             break
    if is_prime:
         primes.append(numbers[i])
print('Primes:',primes)
print('Not primes:',not_primes)





