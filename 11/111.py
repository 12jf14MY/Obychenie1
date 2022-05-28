# # Создадим пустой словать Capitals
# Capitals = dict()
#
# # Заполним его несколькими значениями
# Capitals['Russia'] = ['Moscow', 'sdf', '47']
# Capitals['Ukraine'] = 'Kiev'
# Capitals['USA'] = 'Washington'
# print(Capitals)
# Countries = ['Russia', 'France', 'USA', 'Russia']
#
# for i in Countries:
#     #     # Для каждой страны из списка проверим, есть ли она в словаре Capitals
#     if i in Capitals:
#         print('Столица страны ', i, ': ', Capitals[i])
#         # else:
#         #     print('В базе нет страны c названием ', i)

Capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}
Capitals = dict(Russia = 'Moscow', Ukraine = 'Kiev', USA = 'Washington')
Capitals = dict([("Russia", "Moscow"), ("Ukraine", "Kiev"), ("USA", "Washington")])
Capitals = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))
