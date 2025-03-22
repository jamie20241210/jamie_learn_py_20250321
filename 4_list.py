shopList = []

shopList.append(2)
shopList.append(1)
shopList.append(3)
print(shopList)
print('min =', min(shopList))
print('max =', max(shopList))
print('len =', len(shopList))
print('0 =', shopList[0])
shopList[0] = 11111
print('0 =', shopList[0])
sortedList = sorted(shopList)
print('sorted list =', sortedList)

