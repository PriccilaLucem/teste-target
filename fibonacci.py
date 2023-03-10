def fib(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    if b == n:
        return True
    else:
        return False

num = int(input("Digite um número: "))
fibonacci = [0, 1]

while fibonacci[-1] < num:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

if num in fibonacci:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")