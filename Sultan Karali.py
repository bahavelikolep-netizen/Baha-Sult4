#Ist = [1,2,3,4,5]
#print("Исходный список:", Ist)
#print("Обратный  список:", Ist[::-1])

#def list_sort(Ist):
#    return sorted(Ist, key=abs, reverse=True)
#numbers = [3, -7, 1, -10, 4]
#print("Исходный список:", numbers)
#print("Сортировка по Убыванию |x|:", list_sort(numbers))

def change(Ist):
    if len(Ist) >=2:
        Ist[0], Ist[-1] = Ist[-1], Ist[0]
    return Ist
Data = [10,20,30,40]
print("До изменения:", Data)
print("После изменения:", change(Data))
