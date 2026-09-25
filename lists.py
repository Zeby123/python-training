fruits=['Banana','Mango','Lemon','Grapes','Bananas']
print(fruits)
print(type(fruits))
print(fruits[1:4])

days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print(days[0])
print(days[2:6])

#append
fruits.append("Strawberries")
fruits.append('apple')
fruits.insert(3,'Watermelon')
print(fruits)

#updating; eg; Thursday to Thur
days[3]='Thur'
print(days)
days.append('January')
days.insert(3,'December')
print(days)

#insert
fruits.insert(3,'Watermelon')

#remove
fruits.remove('Banana')

#pop
fruits.pop(2)

print(fruits)