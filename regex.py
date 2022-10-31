import re

if re.search("ape", "The ape at the apex"):
    print("There is an ape")
else:
    print("No ape")

allApes = re.findall("ape", "Find all apes in this ape string")
print(allApes)

the_str = "The ape at the apex"

# ape. means search for ape followed by a single character
for i in re.finditer("ape.", the_str):
    loc_tuple = i.span()
    print(loc_tuple)
    print(the_str[loc_tuple[0]:loc_tuple[1]])
