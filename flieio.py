
# mode="a" means that it is appending/overwriting it
with open("mydata.txt", mode="w", encoding="utf-8") as myfile:
    myfile.write("Some random text \nmore random test \nthis is done")

with open("mydata.txt", encoding="utf-8") as myfile:
    print(myfile.read())

print(myfile.closed)