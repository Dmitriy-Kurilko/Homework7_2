from utils import check_fitness, get_profession_by_title,  get_student_by_pk


def main():
    pk = int(input('Введите номер студента: '))
    student = get_student_by_pk(pk)

    if not student:
        print('У нас нет такого студента.')
        return 0
    print(f'Студент {student["full_name"]}')
    print(f'Знает {", ".join(student["skills"])}')

    title = input(f'Выберите специальность для оценки студента {student["full_name"]}: ').title()
    profession = get_profession_by_title(title)
    if not profession:
        print('У нас нет такой специальности.')
        return 0
    fitness = check_fitness(pk, title)

    print(f'Пригодность {fitness["fit_percent"]}%')
    print(f'Jane Snake знает {", ".join(fitness["has"])}')
    print(f'Jane Snake не знает {", ".join(fitness["lacks"])}')

main()
