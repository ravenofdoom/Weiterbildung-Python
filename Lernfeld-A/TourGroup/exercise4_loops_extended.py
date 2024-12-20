# 1. Löse eine verschachelte Liste auf:

print("Aufgabe 1\n")

nested_list = [1, [2, [3, 4], 5], 6]
flat_list = []
stack = nested_list.copy()

# Tipp: Nutze 'isinstance' und die Listenmethode 'append'

while len(stack) > 0:
    current = stack.pop()
    if isinstance(current, list):
        stack.extend(current[::-1])
    else:
        flat_list.append(current)

print(flat_list) # [1, 2, 3, 4, 5, 6]

# 2. Lass eine Liste um eine bestimmte Anzahl von Positionen nach rechts rotieren.

print("Aufgabe 2\n")

lst = [1, 2, 3, 4, 5]
rotated_list = []
rotation = int(input("How many positions should be rotated? "))

for i in range(len(lst)):
    rotated_list.append(lst[i - rotation])

print(rotated_list)  # [4, 5, 1, 2, 3]

# 3. Schreibe einen Algorithmus, der eine Liste und eine Liste von booleschen Werten
# annimmt und eine neue Liste zurückgibt, die nur die Elemente der ursprünglichen Liste enthält,
# für die der entsprechende boolesche Wert True ist.

print("Aufgabe 3\n")

zahlen=[1, 2, 3, 4, 5]
tf=[True, False, True, False, True]
# zielliste -> [1, 3, 5]

# Tipp: Nutze die Builtin Funktion 'zip'

zielliste = []

# for wert, boolisch in list(zip(zahlen, tf)):
#     if boolisch == True:
#         zielliste.append(wert)

zielliste = [element for element, boolean in zip(zahlen, tf) if boolean] # if bool == True

print(zielliste)  # [1, 3, 5]

# 4. Schreibe einen Algorithmus, der zwei Listen annimmt und eine neue Liste zurückgibt, 
# die die Elemente der beiden Listen abwechselnd enthält. Wenn die Listen unterschiedliche 
# Längen haben, sollen die restlichen Elemente der längeren Liste am Ende hinzugefügt werden.

print("Aufgabe 4\n")

lst1 = [1, 2, 3]
lst2 = [4, 5, 6, 7]
gemischt = []

print("Alternative 2: ")
while (len(lst1) > 0) or (len(lst2) > 0):
    if len(lst1) > 0:
        gemischt.append(lst1.pop(0))
    if len(lst2) > 0:
        gemischt.append(lst2.pop(0))

print(gemischt)  # [1, 4, 2, 5, 3, 6, 7]

# 5. Verschmelze zwei sortierte Listen so, dass eine neue sortierte Liste entsteht.

print("Aufgabe 5\n")

lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
merged = []

while (len(lst1) > 0) or (len(lst2) > 0):
    if len(lst1) > 0:
        merged.append(lst1.pop())
    if len(lst2) > 0:
        merged.append(lst2.pop())

merged.sort()

print(merged)  # [1, 2, 3, 4, 5, 6]

# 6. Schreibe einen Algorithmus, der eine verschachtelte Liste annimmt 
# und die Elemente der verschachtelten Liste sortiert. Die Funktion sollte sowohl 
# die Elemente innerhalb der verschachtelten Listen als auch die verschachtelten Listen selbst sortieren.

print("Aufgabe 6\n")

nested_list2 = [[6, 4, 5], [3, 1, 2], [9, 7, 8]]

for element in nested_list2:
    element.sort()

nested_list2.sort()

print(nested_list2)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



# 7. Schreibe einen Algorithmus, der eine verschachtelte Liste annimmt und 
# die Summe aller Elemente in der verschachtelten Liste berechnet.

print("Aufgabe 7\n")

nested_list3 = [1, [2, [3, 4], 5], 6]
total_sum = 0

stack = nested_list3.copy()

while len(stack) > 0:
    current = stack.pop()
    if isinstance(current, list):
        stack.extend(current[::-1]) # Liste entpacken und umgekehrt auf den Stack legen
    else:
        total_sum += current

# Tipp: 'isinstance'

print(total_sum)  # 21


# 8. Erzeuge eine Liste bis 100, in der statt einer durch 5 teilbaren Zahl eine Liste eingefügt wird, 
# die alle bis dorthin durch 5 teilbaren Zahlen enthält. Also: [[0],1,2,3,4,[0,5],6,7,8,9,[0,5,10]...

print("Aufgabe 8\n")

result = []
dividable_by_5 = []

for number in range(0, 101):
    if number % 5 == 0:
        dividable_by_5.append(number)
        result.append(dividable_by_5.copy())
    else:
        result.append(number)

print(result)


# 9. Sortiere eine Liste so um, dass die erste Hälfte und die zweite Hälfte gegeneinander vertauscht werden.

print("Aufgabe 9\n")

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for x in lst:
    result.append(lst[x - len(lst)//2]) # erster Durchlauf => 0 - 5 = -5

print(result)


# 10. Führe die Listen [1,2,3,4,5] und [8,7,6,5,4] zusammen und entferne die Duplikate, einmal ohne Beachtung der Reihenfolge, 
# einmal mit Beachtung der Reihenfolge.

print("Aufgabe 10\n")

liste10a=[1,2,3,4,5]
liste10b=[8,7,6,5,4]
liste10_from_set=[]
liste10_unsorted=[]

liste10_unsorted = liste10a + liste10b
for num in liste10_unsorted:
    if liste10_unsorted.count(num) > 1:
        liste10_unsorted.remove(num)
print(liste10_from_set, "\n")

liste10_from_set = set(liste10a + liste10b)
print(liste10_unsorted, "\n")