import numpy as np

#Створюємо двовимірний масив 3x3 з випадкових цілих чисел від 1 до 100
matrix = np.random.randint(1, 101, (3, 3))
print("Початковий масив:")
print(matrix)

#Обчислюємо суму всіх елементів масиву
total_sum = np.sum(matrix)
print(f"\nСума всіх елементів: {total_sum}")

#Знаходимо максимальне та мінімальне значення та їхні індекси
max_val = np.max(matrix)
min_val = np.min(matrix)

#unravel_index перетворює плоский індекс у двовимірний
max_idx = np.unravel_index(np.argmax(matrix), matrix.shape)
min_idx = np.unravel_index(np.argmin(matrix), matrix.shape)

print(f"Максимум: {max_val}, його індекс: {max_idx}")
print(f"Мінімум: {min_val}, його індекс: {min_idx}")

#Сортуємо масив по кожному рядку (axis=1 це сортування в межах рядка)
sorted_matrix = np.sort(matrix, axis=1)
print("\nМасив після сортування по рядках:")
print(sorted_matrix)