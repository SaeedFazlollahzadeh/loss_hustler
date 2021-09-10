ace_girls_khas_humans_specs = \
    ['Cute', 'Beautiful', 'Zhazzab', 'Oof', 'Banoo']
ace_girls_khas_humans = \
    ['Anahita', 'Ariana', 'Ava', 'Azadeh', 'Daria', 'Farah', 'Fatemeh', 'Leila', 'Mahnaz', 'Maryam', 'Mona',
     'Nahid', 'Nasrin', 'Nazanin', 'Niloufar', 'Roxana', 'Sara', 'Shirin', 'Soraya', 'Tara', 'Yasmin', 'Alya',
     'Asal', 'Bahar', 'Baran', 'Dana', 'Donya', 'Firuzeh', 'Hadeesa', 'Iran', 'Mahsa', 'Mehr', 'Mina', 'Minoo',
     'Neda', 'Noor', 'Parisa', 'Roya', 'Shadi', 'Shahnaz', 'Shams', 'Yasaman', 'Zahra', 'Ziba']

bikhodi_space_allocated_boys_names_specs = \
    ['Aghaei', 'Eshgh', 'Sotoon', 'Yavar', 'Ghavi', 'Gharniyeh Meshki', 'Charshoone', 'Por Roo']
bikhodi_space_allocated_boys_names = \
    ['Saeed', 'Ali', 'Hamid', 'Hamed', 'Vahid', 'Mohammad', 'Hossein', 'MohammadHossein', 'Soltan', 'Sotoon',
     'Aghaei', 'Gang']

while True:
    instagram_or_twitter = input('Choose 1 for Twitter or 2 for Instagram: ')
    girls_or_boys = input('Choose 1 for \'ace_girls_khas_humans\', or 2 for \'bikhodi_space_allocated_boys_names\': ')
    name_or_list = input('Enter 1 for entering a name, or 2 for choosing from the list: ')

    if instagram_or_twitter == '1' or instagram_or_twitter == '2':
        print(f'ig {instagram_or_twitter} is correct')
        if instagram_or_twitter == '1':
            instagram_or_twitter = 'tweets'
            break
        elif instagram_or_twitter == '2':
            instagram_or_twitter = 'Instagram posts'
        break
    else:
        print(f'ig {instagram_or_twitter} is not correct')
    if girls_or_boys == '1' or girls_or_boys == '2':
        print(f'girls_or_boys {girls_or_boys} is correct')
        break
    else:
        print(f'girls_or_boys {girls_or_boys} is not correct')
    if name_or_list == '1' or name_or_list == '2':
        print(f'names_or_not {name_or_list} is correct')
        if name_or_list == '1':
            name_or_list = 'enter a name'
        elif name_or_list == '2':
            name_or_list = 'choose from the list'
        break
    else:
        print(f'names_or_not {name_or_list} is not correct')
        break
spec = ''
index = 0
if girls_or_boys == '1':
    spec = ace_girls_khas_humans_specs
elif girls_or_boys == '2':
    spec = bikhodi_space_allocated_boys_names_specs
if name_or_list == '1':
    name = input('Enter a name: ')
    for tarif in spec:
        print(f'Hi "{name}", I saw your {instagram_or_twitter} and love you because you are {tarif}.')
elif girls_or_boys == '1' and name_or_list == '2':
    girls_or_boys = ace_girls_khas_humans
    spec = ace_girls_khas_humans_specs
    for names in girls_or_boys:
        print(f'the index number of girls names is {girls_or_boys.index(names)}', end=f' {names}.\n')
    index = input('Choose the index number: ')
    index = int(index)
elif girls_or_boys == '2' and name_or_list == '2':
    girls_or_boys = bikhodi_space_allocated_boys_names
    spec = bikhodi_space_allocated_boys_names_specs
    for names in girls_or_boys:
        print(f'the index number of boys names is {girls_or_boys.index(names)}', end=f' {names}\n')
    index = input('Choose the index number: ')
    index = int(index)

chosen = girls_or_boys[index]
if name_or_list == '2':
    for tarif in spec:
        print(f'Hi "{chosen}", I saw your {instagram_or_twitter} and love you because you are {tarif}.')

print('finish')
