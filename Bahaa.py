#Ist = [1,2,3,4,5]
#print("Исходный список:", Ist)
#print("Обратный  список:", Ist[::-1])

#def list_sort(Ist):
#    return sorted(Ist, key=abs, reverse=True)
#numbers = [5, -4, 7, -14, 8]
#print("Исходный список:", numbers)
#print("Сортировка по Убыванию |x|:", list_sort(numbers))


def change(Ist):
    if len(Ist) >=2:
        Ist[0], Ist[-1] = Ist[-1], Ist[0]
    return Ist
Data = [20,30,40,50]
print("До изменения:", Data)
print("После изменения:", change(Data))