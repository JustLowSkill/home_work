from films import film_list

list_by_rating = []
list_by_year = []
star_wars_list = []

for i, film in enumerate(film_list):
    if film['rating'] > 8.9:
        list_by_rating.append(f'{i + 1}. {film["title"]}')
    if 2003 <= film['year'] <= 2005:
        list_by_year.append(film["title"])
    if 'star wars' in film["title"].lower():
        star_wars_list.append(f'{i}. {film["title"]}')
for film in list_by_rating:
    print(film)
print('\n\n\n')
for i, film in enumerate(list_by_year):
    print(f'{i + 1}. {film}')
print('\n\n\n')
print(f'самый часто встречающийся год: {max(film_list, key=lambda x: [film["year"] for film in film_list].count(x["year"]))["year"]}')# еще как вариант можно через словарь сделать и добавить условия, что если год в словаре, то значение +=1, если нет, то добавить год:1
print('\n\n\n')
for film in star_wars_list:
    print(film)
