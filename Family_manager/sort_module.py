# Сортировка шелла
def shell_sort(data_list, key=None, reverse=False):
    """
    Сортировка Шелла для списка словарей с поддержкой пользовательского ключа и направления.
    """
    n = len(data_list)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = data_list[i]
            j = i

            # Определяем условие сравнения с учетом ключа и направления
            while j >= gap and (
                    (key(data_list[j - gap]) > key(temp) if not reverse else key(data_list[j - gap]) < key(temp))
            ):
                data_list[j] = data_list[j - gap]
                j -= gap
            data_list[j] = temp
        gap //= 2
    return data_list