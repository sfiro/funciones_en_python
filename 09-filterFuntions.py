#extraer los numeros pares de un listado de datos 
numbers = [1,2,3,4]
par = list(filter(lambda x: x%2 == 0, numbers))

print("los elementos pares del listado previo son:")
print(par)

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print(matches)
print(len(matches))

valoresFiltrados = list(filter(lambda ganar:ganar['home_team_result'] == 'Win',matches))
print("Valores filtrados")
print(valoresFiltrados)
print(len(valoresFiltrados))