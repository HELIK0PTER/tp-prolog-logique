# Question 1
print("Question 1")

def composer(f, g):
    return lambda x: f(g(x))

# Question 2
print("Question 2")

# Par exemple, g(x) = x + 1, f(x) = x * x
incrementer = lambda x: x + 1
carre = lambda x: x * x

# Composition f(g(x)) = carre(incrementer(x)) => (x+1)^2
fonction_composee = composer(carre, incrementer)

for valeur in [1, 2, 3, 4]:
    print(valeur, "->", fonction_composee(valeur))
    # 1 -> 4, 2 -> 9, 3 -> 16, 4 -> 25
