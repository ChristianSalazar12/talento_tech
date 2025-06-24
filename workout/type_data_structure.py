pets = ["Laika", "Boster", "Rocky", "Max"]
print("Lista de mascotas:")
for name in pets:
    print(f"->{name}")

print("\n\n")

breeds = ("Labrador", "Pitbull", "Bulldog", "Golden")
print("Razas de perros:")
for breed in breeds:
    print(f"-> {breed}")

print("\n\n")

animal_types = {"perro", "gato", "loro", "hámster"}
print("Tipos de mascotas:")
for animal in animal_types:
    print(f"-> {animal}")

print("\n\n")

ages = {"Laika": 3, "Boster": 5, "Rocky": 2, "Max": 4}
print("Edades de las mascotas:")
for name, age in ages.items():
    print(f"-> {name} tiene {age} años")
