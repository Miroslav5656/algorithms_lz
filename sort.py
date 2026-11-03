import random
slt = [random.randint(0, 1000000) for i in range(100)] #рандомный список 100 чисел от 0 до 10000000
slt2 = slt.copy()
c = 0  #счетчик операций пузырька
print("Стартовый список: ", slt)
print("Сортировка пузырьком:")
i = 0
s = True #стоп флаг
while s is True: #цикл который работает пока стоп флаг правда
  s = False
  for i in range(len(slt) - 1):
    if slt[i] < slt[i + 1]:
      slt[i], slt[i + 1] = slt[i + 1], slt[i]
      c += 1
      s = True
      print(slt)
print("Отсортированный список пузырьком: ", slt) #результаты сортировки пузырьком
print("Количество операций: ", c)
c2 = 0  
print("Сортировка выбором:")
for j in range(len(slt2)):
  max_idx = j #берем что текущий элемент максимальный 
  for k in range(j + 1, len(slt2)): #цикл для поиска макстмального в оставшейся части
    if slt2[k] > slt2[max_idx]:#если нашли элемент больше взятого максимального то обозначаем найденный за макс эл
      max_idx = k
  if max_idx != j: #если нашли эл больше меняем их местами
    slt2[j], slt2[max_idx] = slt2[max_idx], slt2[j]
    c2 += 1
    print(slt2)
print("Отсортированный список выбором: ", slt2) #результат сортировки выбором
print("Количество операций: ", c2)