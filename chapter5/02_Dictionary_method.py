mark={
    "sankar":98,
    "Akash" :90,
    "anik":56
}

print(mark.items())
print(mark.keys())
print(mark.values())
mark.update({"Akash":75,"Ashalata":72})
print(mark)

# print(mark.get("Akash2")) # Prints None
# print(mark["Akash2"]) #returns an error

mark.pop("anik")
print(mark)

mark.popitem()
print(mark)