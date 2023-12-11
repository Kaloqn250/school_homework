def prints_all(developers):
    for developer in developers:
        for key, value in developer.items():
            if isinstance(value, list):
                print(f'{key} : {", ".join(value)}')
            else:
                print(f'{key} : {value}')
        print()


def prints_all_that_know_certain_language(developers, language):
    for developer in developers:
        if language in developer['languages']:
            for key, value in developer.items():
                if isinstance(value, list):
                    print(f'{key} : {", ".join(value)}')
                else:
                    print(f'{key} : {value}')
        print()


def prints_all_that_know_certain_programming_language(developers, dev_language):
    for developer in developers:
        if dev_language in developer['programming_languages']:
            for key, value in developer.items():
                if isinstance(value, list):
                    print(f'{key} : {", ".join(value)}')
                else:
                    print(f'{key} : {value}')
        print()


def prints_all_under_certain_age(developers, search_age):
    for developer in developers:
        if developer['age'] <= search_age:
            for key, value in developer.items():
                if isinstance(value, list):
                    print(f'{key} : {", ".join(value)}')
                else:
                    print(f'{key} : {value}')
        print()


def prints_all_with_bigger_internship(developers, search_internship):
    for developer in developers:
        if developer['internship'] >= search_internship:
            for key, value in developer.items():
                if isinstance(value, list):
                    print(f'{key} : {", ".join(value)}')
                else:
                    print(f'{key} : {value}')
        print()


def prints_person_with_biggest_internship(developers):
    max_internship = 0
    for developer in developers:
        if developer['internship'] > max_internship:
            max_internship = developer['internship']
    for developer in developers:
        if developer['internship'] == max_internship:
            for key, value in developer.items():
                if isinstance(value, list):
                    print(f'{key} : {", ".join(value)}')
                else:
                    print(f'{key} : {value}')
        print()


developers_count = int(input())
developers_list = []

for _ in range(developers_count):
    full_name = input()
    age = int(input())
    programming_languages = input().split(', ')
    languages = input().split(', ')
    internship = int(input())
    developers_list.append({'full_name': full_name, 'age': age, 'programming_languages': programming_languages,
                            'languages':  languages, 'internship': internship})

command = input()

while command != 'Stop':
    if command == 'All':
        prints_all(developers_list)
    elif command == 'Certain language':
        search_language = input('Insert language to search - ')
        prints_all_that_know_certain_language(developers_list, search_language)
    elif command == 'Certain programming language':
        search_dev_language = input('Insert programming language to search - ')
        prints_all_that_know_certain_programming_language(developers_list, search_dev_language)
    elif command == 'Under certain age':
        search_age = int(input('Insert age to search - '))
        prints_all_under_certain_age(developers_list, search_age)
    elif command == 'Bigger internship':
        search_internship = int(input('Insert internship to search - '))
        prints_all_with_bigger_internship(developers_list, search_internship)
    elif command == 'Biggest internship':
        prints_person_with_biggest_internship(developers_list)
    else:
        print('Invalid input')
    command = input()
