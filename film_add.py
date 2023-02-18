def film_param():
    film = {}
    film['name'] = input("Название фильма:")
    film['len'] = input('длнительность фильма (мин):')
    film['year'] = int(input('Год выхода:'))
    film['rate'] = float(input('рейт зис щит:'))
    return(film)

def make_list(i):
    list_of_films = []
    for _ in range(i):
        list_of_films.append(film_param())
    print(list_of_films)

make_list(2)