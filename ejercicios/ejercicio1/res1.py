# Importación del módulo de funciones generadoras - NO MODIFICAR
from pydoc import importfile
idg = importfile('C:/Users/leand/Documents/Python3Projects/PythonInputInstrToFunctConverter/input_data_generators.py')
sequential_idg_list = []
for i in range(2): sequential_idg_list.append([0])
# Fin de la importación del módulo de funciones generadoras - NO MODIFICAR
a = idg.random_int_from_closed_interval_data_gen(-10, 10)
b = idg.random_int_from_closed_interval_data_gen(-10, 10)
print(a + b)