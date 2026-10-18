name="shibsnkar"
# print(len(name))
# print(name.endswith("kar"))
# print(name.endswith("karu"))
# print(name.startswith("shi"))
# print(name.startswith("Shi"))
# print(name.capitalize())

# Correct usage of string functions
print(len(name))                # 9
print(name.lower())             # "shibsnkar"
print(name.upper())             # "SHIBSNKAR"
print(name.strip())             # "shibsnkar" (no spaces to strip here)
print(name.replace("s", "S"))   # "ShibSnkar"
print(name.split("s"))          # ['', 'hib', 'nkar']
print("-".join(name))           # "s-h-i-b-s-n-k-a-r"
print(name.find("kar"))         # 5
print(name.count("s"))          # 2
print(name.startswith("shi"))   # True
print(name.endswith("kar"))     # True
