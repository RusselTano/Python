liste1 = []
for i in range(10):
  liste1.append(i**2)

print(liste1)

liste2 = [i**2 for i in range(10)]
print(liste2)

liste3 = [[i+j for i in range(3)] for j in range(3)]
print(liste3)