# dictionaries is an object made up of key value pairs, but it cannot contain duplicate keys

heroes = {
    "Superman": "Clark Kent",
    "Batman": "Bruce Wayne"
}

villians = dict([
    ("Lex Luthor", "Lex Luthor"),
    ("Loki", "Loki")
])

print(heroes)
print(villians)

print("Length", len(heroes))
print(heroes["Superman"])
heroes["Flash"] = "Barry Allen"
print(list(heroes))
print(list(heroes.items()))
print(list(heroes.keys()))
print(list(heroes.values()))

del heroes['Flash']

print(heroes)
print(heroes.pop("Batman"))
print(heroes)
print("Superman" in heroes)
for k in heroes:
    print(k)

for v in heroes.values():
    print(v)

d1 = {"name": "Lucas", "price": .88}
print("%(name)s costs $%(price).2f" % d1)





