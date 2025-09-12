def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# Foydalanuvchidan son olish
n = int(input("Nechta Fibonachchi sonini chiqarmoqchisiz? "))
print("Fibonachchi sonlari:", fibonacci(n))