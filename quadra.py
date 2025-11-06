import math
import matplotlib.pyplot as plt


months = []
temps = []


with open("input.txt", "r") as file:
    data = file.read().split()
    a, b, c = map(float, data)

print(f"Solving equation: {a}x² + {b}x + {c} = 0")

if a == 0:
    if b != 0:
        x = -c / b
        print(f"This is a linear equation. Root: x = {x:.3f}")
    else:
        print("No solution (a and b cannot both be 0).")
else:
    D = b**2 - 4*a*c
    print(f"Discriminant (D) = {D:.3f}")

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"Two real roots: x₁ = {x1:.3f}, x₂ = {x2:.3f}")
    elif D == 0:
        x = -b / (2*a)
        print(f"One real root: x = {x:.3f}")
    else:
        real = -b / (2*a)
        imag = math.sqrt(-D) / (2*a)
        print(f"Complex roots: x₁ = {real:.3f} + {imag:.3f}i, x₂ = {real:.3f} - {imag:.3f}i")





with open("input.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            months.append(parts[0])
            temps.append(float(parts[1]))


plt.bar(months, temps, color='skyblue')
plt.title("Average Monthly Temperatures (2023)")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.show()
