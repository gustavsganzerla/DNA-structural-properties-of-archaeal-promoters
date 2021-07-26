import os

path = '/Users/gustavosganzerla/Desktop/project_arp/full_seqs/'
path_out = '/Users/gustavosganzerla/Desktop/project_arp/tata_less/full_sequences/'

filenames = os.listdir(path)

for organism in filenames:
	if '.txt' in organism:
		tata_containing=0
		tata_less=0
		with open(path+organism, 'r') as file:
			vetor_dados= file.readlines()
			vetor_dados = [line3.strip() for line3 in vetor_dados]
			list_tata_containing = []
			list_tata_less = []
			
			for sequence in vetor_dados:

				if 'haloferax' in organism:
					if 'ATAAAAAT' in sequence or 'TTAAAAAT' in sequence or 'AGAAAAAT' in sequence or 'TGAAAAAT' in #sequence or 'ATATAAAT' in sequence or 'TTATAAAT' in sequence or 'AGATAAAT' in sequence or 'TGATAAAT' in sequence or 'ATAAATAT' in #sequence or 'TTAAATAT' in sequence or 'AGAAATAT' in sequence or 'TGAAATAT' in sequence or 'ATATATAT' in sequence or 'TTATATAT' in #sequence or 'AGATATAT' in sequence or 'TGATATTT' in sequence:
						tata_containing+=1
						list_tata_containing.append(sequence)

					else:
						tata_less+=1
						list_tata_less.append(sequence)
						

				if 'thermococcus' in organism:
					if 'CTTATAAA' in sequence or 'TTTATAAA' in sequence or 'CTTTTAAA' in sequence or 'TTTTTAAA' in #sequence or 'CTTATAAC' in sequence or 'TTTATAAC' in sequence or 'CTTTTAAC' in sequence or 'TTTTTAAC' in sequence or 'CTTATAAG' in #sequence or 'TTTATAAG' in sequence or 'CTTTTAAG' in sequence or 'TTTTTAAG' in sequence:
						tata_containing+=1
						list_tata_containing.append(sequence)

					else:
						tata_less+=1
						list_tata_less.append(sequence)

				else:
					if 'AAAAAAACC' in sequence or 'TAAAAACC' in sequence or 'ATAAAACC' in sequence or 'TTAAAACC' in sequence or 'AATAAACC' in sequence or 'TATAAACC' in sequence or 'ATTAAACC' in sequence or 'TTTAAACC' in sequence or 'AAAAAGCC' in sequence or 'TAAAAGCC' in sequence or 'ATAAAGCC' in sequence or 'TTAAAGCC' in sequence or 'AATAAGCC' in sequence or 'TATAAGCC' in sequence or 'ATTAAGCC' in sequence or 'TTTAAGCC' in sequence or 'AAAAAAGC' in sequence or 'TAAAAAGC' in sequence or 'ATAAAAGC' in sequence or 'TTAAAAGC' in sequence or 'AATAAAGC' in sequence or 'TATAAAGC' in sequence or 'ATTAAAGC' in sequence or 'TTTAAAGC' in sequence or 'AAAAAGGC' in sequence or 'TAAAAGGC' in sequence or 'ATAAAGGC' in sequence or 'TTAAAGGC' in sequence or 'AATAAGGC' in sequence or 'TATAAGGC' in sequence or 'ATTAAGGC' in sequence or 'TTTAAGGC' in sequence or 'AAAAAAACT' in sequence or 'TAAAAACT' in sequence or 'ATAAAACT' in sequence or 'TTAAAACT' in sequence or 'AATAAACT' in sequence or 'TATAAACT' in sequence or 'ATTAAACT' in sequence or 'TTTAAACT' in sequence or 'AAAAAGCT' in sequence or 'TAAAAGCT' in sequence or 'ATAAAGCT' in sequence or 'TTAAAGCT' in sequence or 'AATAAGCT' in sequence or 'TATAAGCT' in sequence or 'ATTAAGCT' in sequence or 'TTTAAGCT' in sequence or 'AAAAAAGT' in sequence or 'TAAAAAGT' in sequence or 'ATAAAAGT' in sequence or 'TTAAAAGT' in sequence or 'AATAAAGT' in sequence or 'TATAAAGT' in sequence or 'ATTAAAGT' in sequence or 'TTTAAAGT' in sequence or 'AAAAAGGT' in sequence or 'TAAAAGGT' in sequence or 'ATAAAGGT' in sequence or 'TTAAAGGT' in sequence or 'AATAAGGT' in sequence or 'TATAAGGT' in sequence or 'ATTAAGGT' in sequence or 'TTTAAGGT' in sequence:
					tata_containing+=1
					list_tata_containing.append(sequence)
					
				else:
					tata_less+=1
					list_tata_less.append(sequence)
					
			print(tata_containing)
			print(tata_less)

			with open(path_out+"tata_contaning_"+organism, 'a+') as out:
				for element in list_tata_containing:
					out.write(element+"\n")
			with open(path_out+"tata_less_"+organism, 'a+') as out2:
				for element in list_tata_less:
					out2.write(element+"\n")


