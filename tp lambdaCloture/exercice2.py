#Question 2.1
print("Question 2.1")

def creer_multiplicateur(n):
    def multiplicateur(x):
        return x * n
    return multiplicateur

# Question 2.2
print("Question 2.2")

double = creer_multiplicateur(2)
triple = creer_multiplicateur(3)

print(double(5))  # Affiche 10
print(triple(5))  # Affiche 15

# Question 2.3
print("Question 2.3")

for i in [1, 2, 3, 4]:
    print(f"{i} doublé = {double(i)} ; {i} triplé = {triple(i)}")
