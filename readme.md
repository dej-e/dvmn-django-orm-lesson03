# Взламываем электронный дневник

Проект создан в учебный целях

Скрипт содержит ряд функция для работы с базой данных электронного дневника.

`get_child(child_name)` - В качестве аргумента принимает строку с именем ученика, возвращает объект с учетной записью ученика

`fix_mark(schoolkid)` - В качестве аргумента принимает учетную запись ученика, находит все оценки 2 и 3 и исправляет на 5

`remove_chastisements(schoolkid)` - В качестве аргумента принимает учетную запись ученика, удаляет все замечания указанного ученика

`create_commendation(child_name, subject)` - В качестве аргументов принимает строку с именем ученика и строку с наименование предмета. Для указанного ученика и предмета создает похвалу.