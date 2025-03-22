typeType = None
print("type =", typeType)
print("type =", type(typeType))
typeType = True
print("type =", typeType)
print("type =", type(typeType))
if (typeType):
    print("type = true 1")
else:
    print("type = false 2")
typeType = 11111
print("type =", typeType)
print("type =", type(typeType))
if typeType == 111:
    print("type =", typeType)
elif typeType == 11111:
    print("type = 11111 elif")
elif typeType == 3333:
    print("type =", typeType)

typeType = 11111.11
print("type =", typeType)
print("type =", type(typeType))
typeType = "11111.11" + "222"
print("type =", typeType)
print("type =", type(typeType))
