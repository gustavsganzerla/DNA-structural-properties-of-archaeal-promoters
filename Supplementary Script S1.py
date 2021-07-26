import os

path = '/Users/gustavosganzerla/Desktop/estagio_docencia/cluster/data_preparation/bacteria/'
path_out = '/Users/gustavosganzerla/Desktop/estagio_docencia/cluster/data_preparation/bacteria/physical_analysis/'

filenames = os.listdir(path)


for item in filenames:
	if '.txt' in item:
		with open(path+item, 'r') as f:

			list_enthalpy = []
			list_stability = []
			list_bendability = []
			for sequence in f:
				size = len(sequence)
				


				for pos in range(size-1):
					if sequence.upper()[pos:pos+2]== 'AA':
						enthalpy=-7.6
						stability=-1
						bendability = 3.07
						list_enthalpy.append(enthalpy)
						list_stability.append(stability)
						list_bendability.append(bendability)


					if sequence.upper()[pos:pos+2]== 'AT':
						enthalpy=-7.2
						stability=-0.88
						bendability = 2.6
						list_enthalpy.append(enthalpy)
						list_stability.append(stability)
						list_bendability.append(bendability)


					if sequence.upper()[pos:pos+2]== 'TA':
						enthalpy=-7.2
						stability=-0.58
						bendability = 6.74
						list_enthalpy.append(enthalpy)
						list_stability.append(stability)
						list_bendability.append(bendability)


					if sequence.upper()[pos:pos+2]== 'AG':
						enthalpy=-8.2
						stability=-1.3
						bendability = 2.31
						list_enthalpy.append(enthalpy)
						list_stability.append(stability)
						list_bendability.append(bendability)


					if sequence.upper()[pos:pos+2]== 'GA':
						enthalpy=-7.6
						stability=-1.3
						bendability = 2.51
						list_enthalpy.append(enthalpy)
						list_stability.append(stability)
						list_bendability.append(bendability)


					if sequence.upper()[pos:pos+2]== 'TT':
						enthalpy=-7.6
						stability=-1
						bendability = 3.07
						list_enthalpy.append(enthalpy)
						list_stability.append(stability)
						list_bendability.append(bendability)


					if sequence.upper()[pos:pos+2]== 'AC':
						enthalpy=-8.5
						stability=-1.45
						bendability = 2.97
						list_enthalpy.append(enthalpy)
						list_stability.append(stability)
						list_bendability.append(bendability)


					if sequence.upper()[pos:pos+2]== 'CA':
						enthalpy=-8.5
						stability=-1.45
						bendability = 3.58
						list_enthalpy.append(enthalpy)
						list_stability.append(stability)
						list_bendability.append(bendability)


					if sequence.upper()[pos:pos+2]== 'TG':
						enthalpy=-8.4
						stability=-1.44
						bendability = 3.58
						list_enthalpy.append(enthalpy)
						list_stability.append(stability)
						list_bendability.append(bendability)


					if sequence.upper()[pos:pos+2]== 'GT':
						enthalpy=-8.4
						stability=-1.44
						bendability = 2.97
						list_enthalpy.append(enthalpy)
						list_stability.append(stability)
						list_bendability.append(bendability)


					if sequence.upper()[pos:pos+2]== 'TC':
						enthalpy=-7.8
						stability=-1.28
						bendability = 2.51
						list_enthalpy.append(enthalpy)
						list_stability.append(stability)
						list_bendability.append(bendability)


					if sequence.upper()[pos:pos+2]== 'CT':
						enthalpy=-7.8
						stability=-1.28
						bendability = 2.31
						list_enthalpy.append(enthalpy)
						list_stability.append(stability)
						list_bendability.append(bendability)


					if sequence.upper()[pos:pos+2]== 'CC':
						enthalpy=-8
						stability=-1.84
						bendability = 2.16
						list_enthalpy.append(enthalpy)
						list_stability.append(stability)
						list_bendability.append(bendability)


					if sequence.upper()[pos:pos+2]== 'CG':
						enthalpy=-10.6
						stability=-2.24
						bendability = 2.81
						list_enthalpy.append(enthalpy)
						list_stability.append(stability)
						list_bendability.append(bendability)


					if sequence.upper()[pos:pos+2]== 'GC':
						enthalpy=-10.6
						stability=-2.27
						bendability = 3.06
						list_enthalpy.append(enthalpy)
						list_stability.append(stability)
						list_bendability.append(bendability)


					if sequence.upper()[pos:pos+2]== 'GG':
						enthalpy=-8
						stability=-1.84
						bendability = 2.16
						list_enthalpy.append(enthalpy)
						list_stability.append(stability)
						list_bendability.append(bendability)



			with open (path_out+"enthalpy_"+item, 'a+') as out:
				for element in list_enthalpy:
					out.write(str(element) + "\n")

			with open(path_out+"stability_"+item, 'a+') as out2:
				for element in list_stability:
					out2.write(str(element) + "\n")

			with open(path_out+"bendability_"+item, 'a+') as out3:
				for element in list_bendability:
					out3.write(str(element) + "\n")








