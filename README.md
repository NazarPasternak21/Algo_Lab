# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"

## Виконав: Пастеранк Назарій Миколайович (Група ІР-24)

###Лабораторна робота №1 (Варіант 1 Рівень 1)

Дані два масиви цілих чисел nums1 і nums2, де nums1 є підмасивом nums2, якщо всі елементи nums1 знаходяться в nums2, в тому ж порядку. ​ Напишіть функцію is_subarray, яка приймає два масиви цілих чисел та повертає True, якщо nums1 є підмасивом nums2, та False в іншому випадку. ​ Приклади Вхідні дані: nums1 = 1,2,3, nums2 = 1,2,3,4 Результат: True Пояснення: Всі елементи nums1 ([1,2,3]) присутні в nums2. ​ Вхідні дані: nums1 = [4,2], nums2 = [1,2,3,4] Результат: False Пояснення: Елементи nums1 ([4,2]) не знаходяться в тому ж порядку в nums2. ​ Вхідні дані: nums1 = [1,3,5], nums2 = [1,2,3,4,5] Результат: True Пояснення: Елементи nums1 ([1,3,5]) присутні в nums2. ​ Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest та перевірити роботу вашої функції на прикладах, наведених вище

### Лабораторна робота №2 (Варіант 1 Рівень 2)

Love
​
Андрій закоханий у Ілону. Вони вирішили провести День святого Валентина разом в Ашані, але Андрій, як ми всі знаємо, дуже зайнятий на роботі, тому він не зміг прийти. Тепер якраз Ілона знову наповнена гнівом і готова його вбити. Але є щось, що ви можете зробити.
​
Андрій розповідає Ілоні, що він програміст-початківець і, як правило, зайнятий вирішенням важливих проблем на проекті. Тож Ілона вирішує перевірити його алгоритмічні навички. Вона пише масив N цілих чисел. Вона дає йому число P і запитує, чи може він знайти три ( тільки три) цілих числа Ai Aj Ak (i ≠ j ≠ k) в масиві, сума якого дорівнює числу P, тобто
​
Ai + Aj + Ak  = P
​
Отже, чим швидше Андрій скаже відповідь “Такі числа є” або “Таких чисел немає” тим швидше він отримає поцілунок
​
Вхідні дані:
Масив цілих чисел A1, A2 A3 ……………. AN 
Р - Шукане число 
​
Обмеження
3<= N <= 1000
1<= Ai <= 10^9 де 1<= i <=N
1<= P <= 3*10^9
​
Приклад
​
Input
1 2 3
6
​
Output
True

### Лабораторна робота №3 (Варіант 1 Рівень 2)

Для бінарного дерева знайдіть суму всіх листків, які є лівими дітьми.

    3
   / \
  9  20
    /  \
   15   7

Лівий лист цього дерева - 9 та 15, тому сума лівих листів становить 9 + 15 = 24.

Реалізуйте функцію, яка отримує на вхід кореневий вузол дерева, та повертає значення суми branchSums:

def branchSums(root):
	pass

Вхідні дані: Дерево подається у вигляді вузлів, де кожен вузол має ціле значення. Корінь дерева завжди не є лівим листом

Клас, який описує бінарне дерево (та будь який вузол дерева) має вигляд:

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу BinaryTree наступним чином:

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)

Вихідні дані: Сума всіх лівих листів у бінарному дереві.
