countrie_set = {'Hai', 'R.D.', 'Chi'}

nuevo_set = ''
countries_wait = {'Bol', 'Mex'}

agrega = input(' Agrega otro pais: ')

if agrega in countries_wait:
    nuevo_set = agrega
    print(nuevo_set) 
    countrie_set.add(nuevo_set)
    print(countrie_set)
else:
        print('Este país no está en la lista')

# Haciendo la operación CRUD
countrie_set.add('EEUU')
print(countrie_set)

countrie_set.remove('Chi')
print(countrie_set)

countrie_set.discard('R.D.')
print(countrie_set)

countrie_set.update({'Col', 'Venezuela', 'Ita'})
print(countrie_set)
