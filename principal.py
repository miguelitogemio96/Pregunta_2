from pyswip import Prolog

prolog = Prolog()
prolog.consult('declaraciones.pl')

print('¿Juan es hermano de Marcela?')
res = bool(list(prolog.query("hermano_de(juan,marcela)")))
print(f'{res}\n')

print('¿Carlos es hermano de Juan?')
res = bool(list(prolog.query("hermano_de(carlos,juan)")))
print(f'{res}\n')

print('¿Pablo es abuelo de María?')
res = bool(list(prolog.query("abuelo_de(pablo,maria)")))
print(f'{res}\n')

print('¿María es abuela de Pablo?')
res = bool(list(prolog.query("abuelo_de(maria,pablo)")))
print(f'{res}\n')