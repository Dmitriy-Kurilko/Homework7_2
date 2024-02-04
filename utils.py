import os
import json


def load_students():
    '''
    Возвращает данные students.json в виде словаря.
    '''
    with open(os.path.join('data', 'students.json')) as file:
        return json.load(file)


def loads_professions():
    '''
    Возвращает данные professions.json в виде словаря.
    '''
    with open(os.path.join('data', 'professions.json')) as file:
        return json.load(file)


def get_student_by_pk(pk):
    '''
    Возвращает данные студента по его pk(номеру).
    '''
    res = {}
    for i in load_students():
        if i['pk'] == pk:
            res = i
    if res == {}: return 0
    return res


def get_profession_by_title(title):
    '''
    Возвращает данные профессии по ее title(названию).
    '''
    res = {}
    for i in loads_professions():
        if i['title'] == title:
            res = i
    if res == {}:return 0
    return res


def check_fitness(student, profession):
    '''
    Возвращает на сколько подходит конкретный студент для конкретной профессии.
    '''
    data = {}
    student_skills = set(get_student_by_pk(student)['skills'])
    profession_skills = set(get_profession_by_title(profession)['skills'])
    data["has"] = student_skills.intersection(profession_skills)
    data["lacks"] = student_skills.difference(profession_skills)
    data["fit_percent"] = len(data["has"]) * 100 / len(profession_skills)
    return data
