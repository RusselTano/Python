villes = [
    "paris",
    "Berlin",
    "Londre",
    "Strasbourg",
    "Napolie",
    "Douala",
    "Yaounde",
    "Rome",
]

print(villes[::-1])

prenom = "Dylane"

print(prenom[:3])

villes.append("Bafoussam")
villes.insert(3, "Bamenda")
villes2 = ["Amsteram", "Rome"]
villes.extend(villes2)
villes.sort()
print(villes.count("Rome"))
print(villes)

for i in villes:
    print(i)

for i, val in enumerate(villes):
    print(i + 1, val)
