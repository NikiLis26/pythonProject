courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

# Делаем список списков имён
mentors_names = []
for m in mentors:
	course_names = []
	for name in m:
		course_names.append(name.split()[0])
	mentors_names.append(course_names)

# Допишите ниже код, который добавляет списки имён в общий список mentors_names:
# Храните здесь пары курсов, в которых есть совпавшие имена
pairs = []
# Попарное сравнение "наборов" преподавателей на курсах. Каждую новую пару запоминаем для исключения повторов.
for id1 in range(len(mentors_names)):
	for id2 in range(len(mentors_names)):
		if id1 == id2: # Проверьте, что вы не сравниваете список сам с собой:
			continue
		intersection_set = set(mentors_names[id1]) & set(mentors_names[id2]) # Допишите  код для сравнения двух "наборов" преподавателей. Подсказка: используйте множества
		if len(intersection_set) > 0: # Допишите проверку, что результат не пустой, имена есть
			pair = (courses[id1], courses[id2]) # Допишите  код, который проверяет, что эта пара ещё не встречалась
			# Если pair еще не встречалась, то выведите на экран два курса и список преподавателей, которые есть на обоих курсах
			if pair not in pairs:
				pairs.append(pair)
				# Отсортируйте имена по алфавиту. Подсказка: используйте sorted() для списка
				all_names_sorted = sorted(list(intersection_set))
				# Допишите конструкцию вывода результата. Можете использовать string.join()
				print(f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {' , '.join(all_names_sorted)}")

