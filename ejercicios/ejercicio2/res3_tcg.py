# Configuración inicial para generar archivos de entrada de este programa - NO MODIFICAR
import sys
input_data_list = []
input_data_file_route = None
if (len(sys.argv) == 2):
	input_data_file_route = sys.argv[1]
# Fin de configuración inicial para generar archivos de entrada de este programa - NO MODIFICAR
# Importación del módulo de funciones generadoras - NO MODIFICAR
from pydoc import importfile
idg = importfile('C:/Users/leand/Documents/Python3Projects/PythonInputInstrToFunctConverter/input_data_generators.py')
sequential_idg_list = []
for i in range(2): sequential_idg_list.append([0])
# Fin de la importación del módulo de funciones generadoras - NO MODIFICAR
B = idg.random_float_from_closed_interval_with_fixed_precision_data_gen(0.1, 10.0, 1)
input_data_list.append(B)
b = idg.random_float_from_closed_interval_with_fixed_precision_data_gen(0.1, 10.0, 1)
input_data_list.append(b)
h = idg.random_float_from_closed_interval_with_fixed_precision_data_gen(0.1, 10.0, 1)
input_data_list.append(h)
print(((B + b) / 2.0) * h)
# Configuración final para generar archivos de entrada de este programa - NO MODIFICAR
if (input_data_file_route != None and input_data_file_route.endswith('.txt')):
	with open(input_data_file_route, mode='w', encoding='utf-8') as input_file:
		counter = len(input_data_list) # Variable auxiliar para no dejar líneas en blanco en el archivo .txt
		for input_data in input_data_list:
			if (counter != 1):
				input_file.write(str(input_data) + '\n')
			else:
				input_file.write(str(input_data))
			counter -= 1
# Fin de configuración final para generar archivos de entrada de este programa - NO MODIFICAR
