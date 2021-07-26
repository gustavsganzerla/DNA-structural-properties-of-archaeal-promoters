file = open("/Users/gustavosganzerla/Desktop/project_arp/tata_less/MEME/lists/tata_less_sulfolobus_solfataricus.txt", "r")

out = open("/Users/gustavosganzerla/Desktop/project_arp/tata_less/MEME/lists/curvature/tata_less_bmht_sulfolobus_solfataricus.txt","w")

out2 = open("/Users/gustavosganzerla/Desktop/project_arp/tata_less/MEME/lists/curvature/tata_less_cs_sulfolobus_solfataricus.txt","w")




vetor_dados= file.readlines() 
vetor_dados = [line3.strip() for line3 in vetor_dados]

list_curvature_bmht=[]
list_curvature_cs=[]


for item in vetor_dados:
	size = len(item)
	curvature_bhmt=0
	curvature_cs=0

	for pos in range(size-1):

		if item.upper()[pos:pos+5] == 'AAAAA':
			curvature_bmht = 20.5085
			curvature_cs = 8.0576
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)


		if item.upper()[pos:pos+5] == 'AAAAC':
			curvature_bmht = 18.829
			curvature_cs = 8.3764
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)


		if item.upper()[pos:pos+5] == 'AAAAG':
			curvature_bmht = 14.6722
			curvature_cs = 6.0322
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		
		if item.upper()[pos:pos+5] == 'AAAAT':
			curvature_bmht = 19.3481
			curvature_cs = 7.7649
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAACA':
			curvature_bmht = 12.7578
			curvature_cs = 7.8361
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAACC':
			curvature_bmht = 14.6619
			curvature_cs = 6.7548
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAACG':
			curvature_bmht = 12.1994
			curvature_cs = 8.1523
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAACT':
			curvature_bmht = 11.6134
			curvature_cs = 9.0687
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAAGA':
			curvature_bmht = 9.5294
			curvature_cs = 5.7194
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAAGC':
			curvature_bmht = 8.1228
			curvature_cs = 7.919
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAAGG':
			curvature_bmht = 5.818
			curvature_cs = 3.0708
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAAGT':
			curvature_bmht = 6.7001
			curvature_cs = 3.8875
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAATA':
			curvature_bmht = 15.14
			curvature_cs = 10.0639
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAATC':
			curvature_bmht = 15.3853
			curvature_cs = 11.5069
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAATG':
			curvature_bmht = 13.9236
			curvature_cs = 8.4669
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAATT':
			curvature_bmht = 19.1138
			curvature_cs = 8.7371
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AACAA':
			curvature_bmht = 9.8299
			curvature_cs = 12.8404
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AACAC':
			curvature_bmht = 5.5053
			curvature_cs = 9.1061
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AACAG':
			curvature_bmht = 8.3559
			curvature_cs = 10.9649
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AACAT':
			curvature_bmht = 5.7201
			curvature_cs = 8.3651
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AACCA':
			curvature_bmht = 9.6203
			curvature_cs = 3.9404
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AACCC':
			curvature_bmht = 9.6203
			curvature_cs = 3.9404
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AACCG':
			curvature_bmht = 8.7284
			curvature_cs = 5.3583
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AACCT':
			curvature_bmht = 8.806
			curvature_cs = 6.2778
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AACGA':
			curvature_bmht = 7.6902
			curvature_cs = 10.6593
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AACGC':
			curvature_bmht = 5.3591
			curvature_cs = 12.507
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AACGG':
			curvature_bmht = 5.3889
			curvature_cs = 8.3966
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AACGT':
			curvature_bmht = 5.3649
			curvature_cs = 9.0697
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AACTA':
			curvature_bmht = 6.3747
			curvature_cs = 8.8245
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AACTC':
			curvature_bmht = 3.4746
			curvature_cs = 9.8484
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AACTG':
			curvature_bmht = 9.3694
			curvature_cs = 9.8098
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AACTT':
			curvature_bmht = 6.1929
			curvature_cs = 7.8512
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAGAA':
			curvature_bmht = 4.0781
			curvature_cs = 11.3987
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAGAC':
			curvature_bmht = 5.1342
			curvature_cs = 12.6631
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAGAG':
			curvature_bmht = 6.9703
			curvature_cs = 9.9068
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAGAT':
			curvature_bmht = 4.7791
			curvature_cs = 11.5373
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAGCA':
			curvature_bmht = 1.9829
			curvature_cs = 12.9608
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAGCC':
			curvature_bmht = 3.1553
			curvature_cs = 12.1447
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAGCG':
			curvature_bmht = 1.4962
			curvature_cs = 13.6033
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAGCT':
			curvature_bmht = 1.9785
			curvature_cs = 13.3797
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAGGA':
			curvature_bmht = 1.0725
			curvature_cs = 5.5863
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAGGC':
			curvature_bmht = 2.0564
			curvature_cs = 7.8634
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAGGG':
			curvature_bmht = 4.3163
			curvature_cs = 2.7086
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAGGT':
			curvature_bmht = 3.1868
			curvature_cs = 3.6739
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAGTA':
			curvature_bmht = 1.3871
			curvature_cs = 9.2012
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAGTC':
			curvature_bmht = 2.8274
			curvature_cs = 10.8822
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAGTG':
			curvature_bmht = 2.6312
			curvature_cs = 6.7637
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AAGTT':
			curvature_bmht = 2.7354
			curvature_cs = 7.7796
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AATAA':
			curvature_bmht = 9.6365
			curvature_cs = 11.2839
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AATAC':
			curvature_bmht = 9.3919
			curvature_cs = 11.9968
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AATAG':
			curvature_bmht = 7.9396
			curvature_cs = 9.3205
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AATAT':
			curvature_bmht = 9.4814
			curvature_cs = 11.151
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AATCA':
			curvature_bmht = 10.3892
			curvature_cs = 16.6708
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AATCC':
			curvature_bmht = 9.9543
			curvature_cs = 12.4215
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AATCG':
			curvature_bmht = 7.1539
			curvature_cs = 13.9008
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AATCT':
			curvature_bmht = 6.4214
			curvature_cs = 14.364
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AATGA':
			curvature_bmht = 14.1028
			curvature_cs = 16.4098
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AATGC':
			curvature_bmht = 8.5869
			curvature_cs = 12.5811
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AATGG':
			curvature_bmht = 10.3562
			curvature_cs = 13.7572
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AATGT':
			curvature_bmht = 6.6364
			curvature_cs = 9.4534
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AATTA':
			curvature_bmht = 16.0259
			curvature_cs = 10.231
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AATTC':
			curvature_bmht = 15.5417
			curvature_cs = 11.7188
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AATTG':
			curvature_bmht = 19.6591
			curvature_cs = 8.8733
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AATTT':
			curvature_bmht = 19.6591
			curvature_cs = 8.8733
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACAAA':
			curvature_bmht = 10.8475
			curvature_cs = 12.4933
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACAAC':
			curvature_bmht = 9.0922
			curvature_cs = 13.0655
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACAAG':
			curvature_bmht = 5.3952
			curvature_cs = 10.4883
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACAAT':
			curvature_bmht = 9.5916
			curvature_cs = 12.3059
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACACA':
			curvature_bmht = 1.825
			curvature_cs = 7.7539
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACACC':
			curvature_bmht = 3.5771
			curvature_cs = 6.7189
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACACG':
			curvature_bmht = 2.2568
			curvature_cs = 8.1928
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACACT':
			curvature_bmht = 2.6491
			curvature_cs = 8.783
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACAGA':
			curvature_bmht = 8.0707
			curvature_cs = 10.572
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACAGC':
			curvature_bmht = 5.6921
			curvature_cs = 12.7001
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACAGG':
			curvature_bmht = 8.1017
			curvature_cs = 7.7724
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACAGT':
			curvature_bmht = 7.3219
			curvature_cs = 8.7379
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACATA':
			curvature_bmht = 4.186
			curvature_cs = 10.41
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACATC':
			curvature_bmht = 5.639
			curvature_cs = 11.9539
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACATG':
			curvature_bmht = 3.46
			curvature_cs = 8.5052
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACATT':
			curvature_bmht = 8.3052
			curvature_cs = 9.0175
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACCAA':
			curvature_bmht = 4.2173
			curvature_cs = 4.7618
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACCAC':
			curvature_bmht = 6.6391
			curvature_cs = 6.3229
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACCAG':
			curvature_bmht = 9.3979
			curvature_cs = 4.1601
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACCAT':
			curvature_bmht = 6.0069
			curvature_cs = 5.1201
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACCCA':
			curvature_bmht = 7.5981
			curvature_cs = 2.3252
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACCCC':
			curvature_bmht = 7.5981
			curvature_cs = 2.3252
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACCCG':
			curvature_bmht = 8.6433
			curvature_cs = 3.2062
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACCCT':
			curvature_bmht = 9.2588
			curvature_cs = 2.4265
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACCGA':
			curvature_bmht = 7.9478
			curvature_cs = 8.227
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACCGC':
			curvature_bmht = 5.704
			curvature_cs = 10.5325
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACCGG':
			curvature_bmht = 8.3858
			curvature_cs = 5.1217
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACCGT':
			curvature_bmht = 7.5129
			curvature_cs = 6.2683
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACCTA':
			curvature_bmht = 9.8036
			curvature_cs = 4.8862
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACCTC':
			curvature_bmht = 7.7164
			curvature_cs = 6.3189
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACCTG':
			curvature_bmht = 13.5827
			curvature_cs = 5.2641
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACCTT':
			curvature_bmht = 6.8537
			curvature_cs = 3.621
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACGAA':
			curvature_bmht = 2.6313
			curvature_cs = 13.0651
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACGAC':
			curvature_bmht = 4.7476
			curvature_cs = 14.0005
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACGAG':
			curvature_bmht = 7.7784
			curvature_cs = 11.2266
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACGAT':
			curvature_bmht = 4.1305
			curvature_cs = 13.0333
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACGCA':
			curvature_bmht = 1.0639
			curvature_cs = 14.5562
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACGCC':
			curvature_bmht = 1.5761
			curvature_cs = 13.5813
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACGCG':
			curvature_bmht = 2.29
			curvature_cs = 15.0741
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACGCT':
			curvature_bmht = 3.1585
			curvature_cs = 15.3373
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACGGA':
			curvature_bmht = 2.7394
			curvature_cs = 7.7004
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACGGC':
			curvature_bmht = 3.1219
			curvature_cs = 9.3987
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACGGG':
			curvature_bmht = 5.9994
			curvature_cs = 5.9775
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACGGT':
			curvature_bmht = 4.8252
			curvature_cs = 6.3351
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACGTA':
			curvature_bmht = 3.1637
			curvature_cs = 10.5177
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACGTC':
			curvature_bmht = 3.6349
			curvature_cs = 12.0428
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACGTG':
			curvature_bmht = 4.2733
			curvature_cs = 8.6684
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACGTT':
			curvature_bmht = 0.9582
			curvature_cs = 9.1358
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACTAA':
			curvature_bmht = 4.602
			curvature_cs = 6.4347
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACTAC':
			curvature_bmht = 5.2584
			curvature_cs = 6.9387
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACTAG':
			curvature_bmht = 9.8393
			curvature_cs = 4.4074
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACTAT':
			curvature_bmht = 4.7572
			curvature_cs = 6.2007
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACTCA':
			curvature_bmht = 7.9805
			curvature_cs = 11.5575
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACTCC':
			curvature_bmht = 4.8942
			curvature_cs = 7.3837
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACTCG':
			curvature_bmht = 6.9345
			curvature_cs = 8.8413
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACTCT':
			curvature_bmht = 7.5831
			curvature_cs = 9.5149
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACTGA':
			curvature_bmht = 11.4639
			curvature_cs = 7.351
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACTGC':
			curvature_bmht = 10.9291
			curvature_cs = 8.3435
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACTGG':
			curvature_bmht = 14.2667
			curvature_cs = 6.9555
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACTGT':
			curvature_bmht = 13.0798
			curvature_cs = 6.7107
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACTTA':
			curvature_bmht = 2.4909
			curvature_cs = 5.128
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACTTC':
			curvature_bmht = 1.9984
			curvature_cs = 6.6047
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACTTG':
			curvature_bmht = 5.6648
			curvature_cs = 3.8158
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ACTTT':
			curvature_bmht = 5.6648
			curvature_cs = 3.8158
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGAAA':
			curvature_bmht = 7.4837
			curvature_cs = 12.9121
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGAAC':
			curvature_bmht = 5.8876
			curvature_cs = 13.6463
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGAAG':
			curvature_bmht = 3.4998
			curvature_cs = 10.9603
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGAAT':
			curvature_bmht = 6.3004
			curvature_cs = 12.7909
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGACA':
			curvature_bmht = 4.7312
			curvature_cs = 12.963
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGACC':
			curvature_bmht = 6.7621
			curvature_cs = 11.9565
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGACG':
			curvature_bmht = 7.6068
			curvature_cs = 13.4419
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGACT':
			curvature_bmht = 8.1971
			curvature_cs = 13.8473
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGAGA':
			curvature_bmht = 10.3715
			curvature_cs = 11.4788
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGAGC':
			curvature_bmht = 8.3444
			curvature_cs = 13.7071
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGAGG':
			curvature_bmht = 11.1915
			curvature_cs = 8.4661
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGAGT':
			curvature_bmht = 10.274
			curvature_cs = 9.5622
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGATA':
			curvature_bmht = 5.2279
			curvature_cs = 15.6739
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGATC':
			curvature_bmht = 3.1478
			curvature_cs = 17.1941
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGATG':
			curvature_bmht = 3.7536
			curvature_cs = 13.7522
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGATT':
			curvature_bmht = 7.4462
			curvature_cs = 14.2881
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGCAA':
			curvature_bmht = 10.298
			curvature_cs = 24.8635
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGCAC':
			curvature_bmht = 2.063
			curvature_cs = 15.3228
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGCAG':
			curvature_bmht = 5.914
			curvature_cs = 23.0256
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGCAT':
			curvature_bmht = 2.7566
			curvature_cs = 14.509
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGCCA':
			curvature_bmht = 5.751
			curvature_cs = 10.0273
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGCCC':
			curvature_bmht = 5.7511
			curvature_cs = 10.0274
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGCCG':
			curvature_bmht = 5.6133
			curvature_cs = 11.5069
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGCCT':
			curvature_bmht = 6.0261
			curvature_cs = 11.9937
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGCGA':
			curvature_bmht = 4.7175
			curvature_cs = 16.8933
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGCGC':
			curvature_bmht = 2.213
			curvature_cs = 18.7523
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGCGG':
			curvature_bmht = 4.7254
			curvature_cs = 14.4263
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGCGT':
			curvature_bmht = 3.8254
			curvature_cs = 15.2344
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGCTA':
			curvature_bmht = 6.1556
			curvature_cs = 14.5623
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGCTC':
			curvature_bmht = 4.4406
			curvature_cs = 15.8153
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGCTG':
			curvature_bmht = 9.9934
			curvature_cs = 14.5301
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGCTT':
			curvature_bmht = 3.3819
			curvature_cs = 13.3554
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGGAA':
			curvature_bmht = 4.3098
			curvature_cs = 9.959
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGGAC':
			curvature_bmht = 3.3998
			curvature_cs = 11.1519
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGGAG':
			curvature_bmht = 4.3682
			curvature_cs = 8.3716
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGGAT':
			curvature_bmht = 3.4946
			curvature_cs = 10.0546
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGGCA':
			curvature_bmht = 4.2894
			curvature_cs = 11.5126
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGGCC':
			curvature_bmht = 3.9439
			curvature_cs = 10.6522
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGGCG':
			curvature_bmht = 1.2571
			curvature_cs = 12.1276
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGGCT':
			curvature_bmht = 0.7715
			curvature_cs = 12.0431
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGGGA':
			curvature_bmht = 1.986
			curvature_cs = 4.2084
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGGGC':
			curvature_bmht = 4.4986
			curvature_cs = 6.3517
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGGGG':
			curvature_bmht = 5.3622
			curvature_cs = 2.1723
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGGGT':
			curvature_bmht = 4.6053
			curvature_cs = 2.5285
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGGTA':
			curvature_bmht = 2.6238
			curvature_cs = 7.6584
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGGTC':
			curvature_bmht = 5.3197
			curvature_cs = 9.3249
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGGTG':
			curvature_bmht = 4.1722
			curvature_cs = 5.3373
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGGTT':
			curvature_bmht = 4.2407
			curvature_cs = 6.2274
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGTAA':
			curvature_bmht = 3.1005
			curvature_cs = 10.7863
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGTAC':
			curvature_bmht = 0.2094
			curvature_cs = 11.8406
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGTAG':
			curvature_bmht = 4.9487
			curvature_cs = 9.0441
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGTAT':
			curvature_bmht = 0.6644
			curvature_cs = 10.8092
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGTCA':
			curvature_bmht = 7.7631
			curvature_cs = 16.8242
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGTCC':
			curvature_bmht = 4.2044
			curvature_cs = 12.1957
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGTCG':
			curvature_bmht = 3.3929
			curvature_cs = 13.685
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGTCT':
			curvature_bmht = 3.4765
			curvature_cs = 13.7308
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGTGA':
			curvature_bmht = 3.2553
			curvature_cs = 15.2741
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGTGC':
			curvature_bmht = 3.9089
			curvature_cs = 12.6214
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGTGG':
			curvature_bmht = 1.4251
			curvature_cs = 12.3459
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGTGT':
			curvature_bmht = 3.63
			curvature_cs = 8.7864
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGTTA':
			curvature_bmht = 6.7418
			curvature_cs = 10.3138
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGTTC':
			curvature_bmht = 7.0384
			curvature_cs = 11.9581
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGTTG':
			curvature_bmht = 10.6548
			curvature_cs = 8.8817
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'AGTTT':
			curvature_bmht = 10.6548
			curvature_cs = 8.8817
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATAAA':
			curvature_bmht = 10.6397
			curvature_cs = 11.6514
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATAAC':
			curvature_bmht = 8.5817
			curvature_cs = 12.0411
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATAAG':
			curvature_bmht = 4.5108
			curvature_cs = 9.6222
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATAAT':
			curvature_bmht = 9.1604
			curvature_cs = 11.3944
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATACA':
			curvature_bmht = 3.5784
			curvature_cs = 11.4836
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATACC':
			curvature_bmht = 6.0251
			curvature_cs = 10.408
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATACG':
			curvature_bmht = 5.5174
			curvature_cs = 11.8178
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATACT':
			curvature_bmht = 5.8276
			curvature_cs = 12.6522
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATAGA':
			curvature_bmht = 7.3933
			curvature_cs = 9.238
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATAGC':
			curvature_bmht = 5.1765
			curvature_cs = 11.252
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATAGG':
			curvature_bmht = 7.937
			curvature_cs = 6.7255
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATAGT':
			curvature_bmht = 7.0312
			curvature_cs = 7.5192
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATATA':
			curvature_bmht = 5.473
			curvature_cs = 13.6796
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATATC':
			curvature_bmht = 5.104
			curvature_cs = 15.0666
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATATG':
			curvature_bmht = 3.9625
			curvature_cs = 12.1326
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATATT':
			curvature_bmht = 9.0379
			curvature_cs = 12.3798
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATCAA':
			curvature_bmht = 12.9659
			curvature_cs = 19.7339
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATCAC':
			curvature_bmht = 10.396
			curvature_cs = 20.495
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATCAG':
			curvature_bmht = 5.6851
			curvature_cs = 17.8008
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATCAT':
			curvature_bmht = 11.1199
			curvature_cs = 19.6308
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATCCA':
			curvature_bmht = 7.6005
			curvature_cs = 9.5213
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATCCC':
			curvature_bmht = 7.6006
			curvature_cs = 9.5213
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATCCG':
			curvature_bmht = 5.6538
			curvature_cs = 10.9001
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATCCT':
			curvature_bmht = 5.4127
			curvature_cs = 11.8395
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATCGA':
			curvature_bmht = 4.6448
			curvature_cs = 16.01
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATCGC':
			curvature_bmht = 3.3775
			curvature_cs = 17.6184
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATCGG':
			curvature_bmht = 1.3534
			curvature_cs = 13.9686
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATCGT':
			curvature_bmht = 1.8182
			curvature_cs = 14.5621
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATCTA':
			curvature_bmht = 2.4134
			curvature_cs = 14.4024
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATCTC':
			curvature_bmht = 0.9436
			curvature_cs = 15.4294
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATCTG':
			curvature_bmht = 5.9964
			curvature_cs = 15.0353
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATCTT':
			curvature_bmht = 3.4147
			curvature_cs = 13.3702
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATGAA':
			curvature_bmht = 12.3945
			curvature_cs = 19.2705
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATGAC':
			curvature_bmht = 12.8558
			curvature_cs = 19.9538
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATGAG':
			curvature_bmht = 11.8506
			curvature_cs = 17.3052
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATGAT':
			curvature_bmht = 12.7886
			curvature_cs = 19.1349
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATGCA':
			curvature_bmht = 6.5917
			curvature_cs = 14.8237
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATGCC':
			curvature_bmht = 7.9209
			curvature_cs = 13.7882
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATGCG':
			curvature_bmht = 5.1528
			curvature_cs = 15.2562
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATGCT':
			curvature_bmht = 4.4676
			curvature_cs = 15.7941
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATGGA':
			curvature_bmht = 7.9331
			curvature_cs = 14.3011
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATGGC':
			curvature_bmht = 6.851
			curvature_cs = 15.7019
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATGGG':
			curvature_bmht = 4.141
			curvature_cs = 12.6495
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATGGT':
			curvature_bmht = 5.1499
			curvature_cs = 13.0494
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATGTA':
			curvature_bmht = 3.4666
			curvature_cs = 10.7874
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATGTC':
			curvature_bmht = 5.0187
			curvature_cs = 12.1526
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATGTG':
			curvature_bmht = 2.794
			curvature_cs = 9.3709
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATGTT':
			curvature_bmht = 7.5854
			curvature_cs = 9.5136
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATTAA':
			curvature_bmht = 10.949
			curvature_cs = 11.0951
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATTAC':
			curvature_bmht = 11.9725
			curvature_cs = 11.8715
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATTAG':
			curvature_bmht = 11.8913
			curvature_cs = 9.1592
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATTAT':
			curvature_bmht = 11.7511
			curvature_cs = 10.9887
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATTCA':
			curvature_bmht = 9.6049
			curvature_cs = 16.6165
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATTCC':
			curvature_bmht = 10.8024
			curvature_cs = 12.2854
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATTCG':
			curvature_bmht = 8.7977
			curvature_cs = 13.7718
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATTCT':
			curvature_bmht = 8.45
			curvature_cs = 14.163
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATTGA':
			curvature_bmht = 20.7443
			curvature_cs = 12.2757
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATTGC':
			curvature_bmht = 19.294
			curvature_cs = 14.3409
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATTGG':
			curvature_bmht = 16.9765
			curvature_cs = 9.5492
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATTGT':
			curvature_bmht = 17.9233
			curvature_cs = 10.4807
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATTTA':
			curvature_bmht = 17.8854
			curvature_cs = 10.1404
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATTTC':
			curvature_bmht = 16.6805
			curvature_cs = 11.6649
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATTTG':
			curvature_bmht = 20.9804
			curvature_cs = 8.7599
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'ATTTT':
			curvature_bmht = 20.9804
			curvature_cs = 8.7599
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAAAA':
			curvature_bmht = 15.1927
			curvature_cs = 9.3423
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAAAC':
			curvature_bmht = 13.0776
			curvature_cs = 8.2116
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAAAG':
			curvature_bmht = 8.6526
			curvature_cs = 8.3814
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAAAT':
			curvature_bmht = 13.6934
			curvature_cs = 8.7381
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAACA':
			curvature_bmht = 6.6101
			curvature_cs = 8.4631
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAACC':
			curvature_bmht = 8.5628
			curvature_cs = 7.828
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAACG':
			curvature_bmht = 6.3546
			curvature_cs = 8.0378
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAACT':
			curvature_bmht = 5.9644
			curvature_cs = 10.0632
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAAGA':
			curvature_bmht = 5.1873
			curvature_cs = 4.7777
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAAGC':
			curvature_bmht = 2.7834
			curvature_cs = 3.8999
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAAGG':
			curvature_bmht = 3.7437
			curvature_cs = 7.107
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAAGT':
			curvature_bmht = 3.2482
			curvature_cs = 5.9128
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAATA':
			curvature_bmht = 8.9986
			curvature_cs = 7.4323
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAATC':
			curvature_bmht = 9.5047
			curvature_cs = 7.7822
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAATG':
			curvature_bmht = 7.8419
			curvature_cs = 8.1958
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAATT':
			curvature_bmht = 13.0135
			curvature_cs = 7.098
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CACAA':
			curvature_bmht = 6.3413
			curvature_cs = 13.2762
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CACAC':
			curvature_bmht = 1.8231
			curvature_cs = 9.5402
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CACAG':
			curvature_bmht = 4.8234
			curvature_cs = 11.3902
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CACAT':
			curvature_bmht = 2.523
			curvature_cs = 8.8133
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CACCA':
			curvature_bmht = 5.6877
			curvature_cs = 4.3987
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CACCC':
			curvature_bmht = 5.6878
			curvature_cs = 4.3988
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CACCG':
			curvature_bmht = 5.6763
			curvature_cs = 5.8091
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CACCT':
			curvature_bmht = 6.1204
			curvature_cs = 6.7371
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CACGA':
			curvature_bmht = 4.8053
			curvature_cs = 11.086
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CACGC':
			curvature_bmht = 2.3342
			curvature_cs = 12.9059
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CACGG':
			curvature_bmht = 4.9483
			curvature_cs = 8.8538
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CACGT':
			curvature_bmht = 4.0289
			curvature_cs = 9.5147
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CACTA':
			curvature_bmht = 6.3803
			curvature_cs = 9.2855
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CACTC':
			curvature_bmht = 4.6799
			curvature_cs = 10.3074
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CACTG':
			curvature_bmht = 10.2242
			curvature_cs = 10.2338
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CACTT':
			curvature_bmht = 3.5079
			curvature_cs = 8.3062
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAGAA':
			curvature_bmht = 2.3773
			curvature_cs = 6.5173
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAGAC':
			curvature_bmht = 5.154
			curvature_cs = 6.8927
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAGAG':
			curvature_bmht = 9.8108
			curvature_cs = 4.4903
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAGAT':
			curvature_bmht = 4.3022
			curvature_cs = 6.2361
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAGCA':
			curvature_bmht = 4.9895
			curvature_cs = 7.7172
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAGCC':
			curvature_bmht = 3.0144
			curvature_cs = 6.6358
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAGCG':
			curvature_bmht = 5.9225
			curvature_cs = 8.0334
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAGCT':
			curvature_bmht = 6.7893
			curvature_cs = 8.9516
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAGGA':
			curvature_bmht = 6.925
			curvature_cs = 4.5376
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAGGC':
			curvature_bmht = 7.467
			curvature_cs = 3.7291
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAGGG':
			curvature_bmht = 10.4397
			curvature_cs = 6.8611
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAGGT':
			curvature_bmht = 9.2706
			curvature_cs = 5.6642
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAGTA':
			curvature_bmht = 7.4946
			curvature_cs = 3.9641
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAGTC':
			curvature_bmht = 7.8073
			curvature_cs = 4.9396
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAGTG':
			curvature_bmht = 8.7177
			curvature_cs = 4.2471
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CAGTT':
			curvature_bmht = 3.5651
			curvature_cs = 3.2581
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CATAA':
			curvature_bmht = 6.2049
			curvature_cs = 11.7231
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CATAC':
			curvature_bmht = 5.2793
			curvature_cs = 12.4147
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CATAG':
			curvature_bmht = 4.4638
			curvature_cs = 9.7524
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CATAT':
			curvature_bmht = 5.477
			curvature_cs = 11.5822
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CATCA':
			curvature_bmht = 8.6204
			curvature_cs = 17.0564
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CATCC':
			curvature_bmht = 6.8424
			curvature_cs = 12.8432
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CATCG':
			curvature_bmht = 3.8581
			curvature_cs = 14.3193
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CATCT':
			curvature_bmht = 2.9526
			curvature_cs = 14.8057
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CATGA':
			curvature_bmht = 10.1187
			curvature_cs = 16.8241
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CATGC':
			curvature_bmht = 5.5505
			curvature_cs = 12.9834
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CATGG':
			curvature_bmht = 6.5043
			curvature_cs = 14.195
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CATGT':
			curvature_bmht = 3.3666
			curvature_cs = 9.9029
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CATTA':
			curvature_bmht = 12.0243
			curvature_cs = 10.6363
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CATTC':
			curvature_bmht = 11.8742
			curvature_cs = 12.1066
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CATTG':
			curvature_bmht = 15.8163
			curvature_cs = 9.2887
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CATTT':
			curvature_bmht = 15.8163
			curvature_cs = 9.2888
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCAAA':
			curvature_bmht = 7.6401
			curvature_cs = 6.7996
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCAAC':
			curvature_bmht = 5.6955
			curvature_cs = 8.0406
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCAAG':
			curvature_bmht = 2.7311
			curvature_cs = 5.2957
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCAAT':
			curvature_bmht = 6.2086
			curvature_cs = 6.9172
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCACA':
			curvature_bmht = 3.9463
			curvature_cs = 7.2131
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCACC':
			curvature_bmht = 5.9389
			curvature_cs = 6.4994
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCACG':
			curvature_bmht = 6.8711
			curvature_cs = 7.8987
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCACT':
			curvature_bmht = 7.4979
			curvature_cs = 7.5487
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCAGA':
			curvature_bmht = 9.8098
			curvature_cs = 7.7962
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCAGC':
			curvature_bmht = 7.8984
			curvature_cs = 10.1864
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCAGG':
			curvature_bmht = 10.8732
			curvature_cs = 4.6741
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCAGT':
			curvature_bmht = 9.9032
			curvature_cs = 5.9854
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCATA':
			curvature_bmht = 4.4228
			curvature_cs = 10.6388
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCATC':
			curvature_bmht = 2.5777
			curvature_cs = 12.3237
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCATG':
			curvature_bmht = 2.9312
			curvature_cs = 8.1606
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCATT':
			curvature_bmht = 6.8735
			curvature_cs = 9.2225
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCCAA':
			curvature_bmht = 3.5409
			curvature_cs = 4.9901
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCCAC':
			curvature_bmht = 6.3912
			curvature_cs = 6.626
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCCAG':
			curvature_bmht = 9.7019
			curvature_cs = 4.9453
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCCAT':
			curvature_bmht = 5.6579
			curvature_cs = 5.4673
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCCCA':
			curvature_bmht = 7.4557
			curvature_cs = 3.3789
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCCCC':
			curvature_bmht = 7.4557
			curvature_cs = 3.3789
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCCCG':
			curvature_bmht = 8.8973
			curvature_cs = 3.7704
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCCCT':
			curvature_bmht = 9.5931
			curvature_cs = 2.1723
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCCGA':
			curvature_bmht = 8.3145
			curvature_cs = 8.0615
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCCGC':
			curvature_bmht = 6.283
			curvature_cs = 10.4554
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCCGG':
			curvature_bmht = 9.2044
			curvature_cs = 4.7689
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCCGT':
			curvature_bmht = 8.2485
			curvature_cs = 6.0608
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCCTA':
			curvature_bmht = 10.6368
			curvature_cs = 4.116
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCCTC':
			curvature_bmht = 8.7213
			curvature_cs = 5.7195
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCCTG':
			curvature_bmht = 14.4712
			curvature_cs = 3.88
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCCTT':
			curvature_bmht = 7.3798
			curvature_cs = 2.7085
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCGAA':
			curvature_bmht = 1.7269
			curvature_cs = 12.4287
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCGAC':
			curvature_bmht = 4.5474
			curvature_cs = 13.491
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCGAG':
			curvature_bmht = 8.2294
			curvature_cs = 10.6945
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCGAT':
			curvature_bmht = 3.7875
			curvature_cs = 12.4578
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCGCA':
			curvature_bmht = 1.8424
			curvature_cs = 13.9574
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCGCC':
			curvature_bmht = 0.7108
			curvature_cs = 13.0323
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCGCG':
			curvature_bmht = 3.1186
			curvature_cs = 14.5243
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCGCT':
			curvature_bmht = 4.0304
			curvature_cs = 14.6127
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCGGA':
			curvature_bmht = 3.8328
			curvature_cs = 6.828
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCGGC':
			curvature_bmht = 4.2305
			curvature_cs = 8.7613
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCGGG':
			curvature_bmht = 7.1827
			curvature_cs = 4.7173
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCGGT':
			curvature_bmht = 6.0067
			curvature_cs = 5.2524
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCGTA':
			curvature_bmht = 4.3169
			curvature_cs = 9.9768
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCGTC':
			curvature_bmht = 4.6539
			curvature_cs = 11.5785
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCGTG':
			curvature_bmht = 5.4557
			curvature_cs = 7.8885
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCGTT':
			curvature_bmht = 0.368
			curvature_cs = 8.5565
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCTAA':
			curvature_bmht = 5.6828
			curvature_cs = 5.3789
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCTAC':
			curvature_bmht = 6.4219
			curvature_cs = 6.1394
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCTAG':
			curvature_bmht = 10.9444
			curvature_cs = 3.4125
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCTAT':
			curvature_bmht = 5.9389
			curvature_cs = 5.2429
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCTCA':
			curvature_bmht = 8.6491
			curvature_cs = 11.0168
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCTCC':
			curvature_bmht = 5.8529
			curvature_cs = 6.5429
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCTCG':
			curvature_bmht = 8.0676
			curvature_cs = 8.033
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCTCT':
			curvature_bmht = 8.7401
			curvature_cs = 8.4662
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCTGA':
			curvature_bmht = 12.5813
			curvature_cs = 6.0254
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCTGC':
			curvature_bmht = 12.1038
			curvature_cs = 7.2177
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCTGG':
			curvature_bmht = 15.4381
			curvature_cs = 5.5732
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCTGT':
			curvature_bmht = 14.2493
			curvature_cs = 5.3064
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCTTA':
			curvature_bmht = 1.9507
			curvature_cs = 4.4947
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCTTC':
			curvature_bmht = 1.1464
			curvature_cs = 6.1223
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCTTG':
			curvature_bmht = 4.4991
			curvature_cs = 3.0708
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CCTTT':
			curvature_bmht = 4.4991
			curvature_cs = 3.0708
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGAAA':
			curvature_bmht = 8.0886
			curvature_cs = 13.699
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGAAC':
			curvature_bmht = 6.7118
			curvature_cs = 14.1313
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGAAG':
			curvature_bmht = 4.3032
			curvature_cs = 11.6732
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGAAT':
			curvature_bmht = 7.0762
			curvature_cs = 13.461
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGACA':
			curvature_bmht = 5.1867
			curvature_cs = 13.5606
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGACC':
			curvature_bmht = 7.3688
			curvature_cs = 12.4896
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGACG':
			curvature_bmht = 7.9118
			curvature_cs = 13.9091
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGACT':
			curvature_bmht = 8.4244
			curvature_cs = 14.6926
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGAGA':
			curvature_bmht = 10.3592
			curvature_cs = 11.3208
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGAGC':
			curvature_bmht = 8.1935
			curvature_cs = 13.284
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGAGG':
			curvature_bmht = 10.8691
			curvature_cs = 8.812
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGAGT':
			curvature_bmht = 10.0166
			curvature_cs = 9.6197
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGATA':
			curvature_bmht = 5.9711
			curvature_cs = 15.7765
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGATC':
			curvature_bmht = 4.0382
			curvature_cs = 17.1509
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGATG':
			curvature_bmht = 4.4359
			curvature_cs = 14.2239
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGATT':
			curvature_bmht = 8.34
			curvature_cs = 14.4803
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGCAA':
			curvature_bmht = 10.9033
			curvature_cs = 24.988
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGCAC':
			curvature_bmht = 2.7474
			curvature_cs = 15.747
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGCAG':
			curvature_bmht = 6.8096
			curvature_cs = 23.0619
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGCAT':
			curvature_bmht = 3.2912
			curvature_cs = 15.1044
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGCCA':
			curvature_bmht = 6.5706
			curvature_cs = 10.7323
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGCCC':
			curvature_bmht = 6.5706
			curvature_cs = 10.7323
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGCCG':
			curvature_bmht = 6.158
			curvature_cs = 12.1193
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGCCT':
			curvature_bmht = 6.4672
			curvature_cs = 13.0247
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGCGA':
			curvature_bmht = 5.1964
			curvature_cs = 17.2346
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGCGC':
			curvature_bmht = 2.6594
			curvature_cs = 18.8311
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGCGG':
			curvature_bmht = 4.5019
			curvature_cs = 15.1835
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGCGT':
			curvature_bmht = 3.7884
			curvature_cs = 15.7862
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGCTA':
			curvature_bmht = 5.8926
			curvature_cs = 15.5935
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGCTC':
			curvature_bmht = 3.8315
			curvature_cs = 16.6412
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGCTG':
			curvature_bmht = 9.635
			curvature_cs = 16.1273
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGCTT':
			curvature_bmht = 3.7566
			curvature_cs = 14.5387
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGGAA':
			curvature_bmht = 4.9726
			curvature_cs = 10.032
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGGAC':
			curvature_bmht = 4.2949
			curvature_cs = 10.8927
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGGAG':
			curvature_bmht = 4.6442
			curvature_cs = 8.1396
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGGAT':
			curvature_bmht = 4.3762
			curvature_cs = 9.9607
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGGCA':
			curvature_bmht = 4.3118
			curvature_cs = 11.4908
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGGCC':
			curvature_bmht = 4.4569
			curvature_cs = 10.4925
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGGCG':
			curvature_bmht = 1.4866
			curvature_cs = 11.981
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGGCT':
			curvature_bmht = 0.5737
			curvature_cs = 12.3626
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGGGA':
			curvature_bmht = 1.497
			curvature_cs = 5.0711
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGGGC':
			curvature_bmht = 4.0157
			curvature_cs = 6.403
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGGGG':
			curvature_bmht = 4.4979
			curvature_cs = 4.6543
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGGGT':
			curvature_bmht = 3.8097
			curvature_cs = 4.3244
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGGTA':
			curvature_bmht = 1.9731
			curvature_cs = 7.44
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGGTC':
			curvature_bmht = 4.8392
			curvature_cs = 8.9242
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGGTG':
			curvature_bmht = 3.4187
			curvature_cs = 5.8498
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGGTT':
			curvature_bmht = 4.5627
			curvature_cs = 6.0968
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGTAA':
			curvature_bmht = 3.1129
			curvature_cs = 11.048
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGTAC':
			curvature_bmht = 0.9181
			curvature_cs = 11.7699
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGTAG':
			curvature_bmht = 4.5707
			curvature_cs = 9.0878
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGTAT':
			curvature_bmht = 1.1376
			curvature_cs = 10.9183
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGTCA':
			curvature_bmht = 7.5263
			curvature_cs = 16.4585
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGTCC':
			curvature_bmht = 4.183
			curvature_cs = 12.1929
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGTCG':
			curvature_bmht = 2.7396
			curvature_cs = 13.6734
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGTCT':
			curvature_bmht = 2.6709
			curvature_cs = 14.1269
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGTGA':
			curvature_bmht = 4.0876
			curvature_cs = 15.3113
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGTGC':
			curvature_bmht = 3.5999
			curvature_cs = 12.3613
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGTGG':
			curvature_bmht = 1.1533
			curvature_cs = 12.7538
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGTGT':
			curvature_bmht = 2.8899
			curvature_cs = 9.2136
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGTTA':
			curvature_bmht = 7.6051
			curvature_cs = 10.0102
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGTTC':
			curvature_bmht = 7.7381
			curvature_cs = 11.5059
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGTTG':
			curvature_bmht = 11.4712
			curvature_cs = 8.6479
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CGTTT':
			curvature_bmht = 11.4712
			curvature_cs = 8.6479
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTAAA':
			curvature_bmht = 9.6303
			curvature_cs = 8.2169
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTAAC':
			curvature_bmht = 6.4493
			curvature_cs = 8.7255
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTAAG':
			curvature_bmht = 2.4398
			curvature_cs = 6.1937
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTAAT':
			curvature_bmht = 7.3107
			curvature_cs = 7.9937
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTACA':
			curvature_bmht = 2.1238
			curvature_cs = 8.1116
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTACC':
			curvature_bmht = 1.3128
			curvature_cs = 7.0562
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTACG':
			curvature_bmht = 3.9221
			curvature_cs = 8.51
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTACT':
			curvature_bmht = 4.8317
			curvature_cs = 9.2091
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTAGA':
			curvature_bmht = 8.0149
			curvature_cs = 6.4285
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTAGC':
			curvature_bmht = 7.3477
			curvature_cs = 8.7181
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTAGG':
			curvature_bmht = 10.6866
			curvature_cs = 3.4371
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTAGT':
			curvature_bmht = 9.5014
			curvature_cs = 4.4935
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTATA':
			curvature_bmht = 0.7674
			curvature_cs = 10.6198
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTATC':
			curvature_bmht = 3.6339
			curvature_cs = 12.126
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTATG':
			curvature_bmht = 1.9492
			curvature_cs = 8.8244
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTATT':
			curvature_bmht = 4.6569
			curvature_cs = 9.2492
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTCAA':
			curvature_bmht = 12.8642
			curvature_cs = 16.6029
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTCAC':
			curvature_bmht = 9.6147
			curvature_cs = 17.4895
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTCAG':
			curvature_bmht = 5.6855
			curvature_cs = 14.7351
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTCAT':
			curvature_bmht = 10.4878
			curvature_cs = 16.5523
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTCCA':
			curvature_bmht = 2.5924
			curvature_cs = 6.0866
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTCCC':
			curvature_bmht = 2.5924
			curvature_cs = 6.0867
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTCCG':
			curvature_bmht = 0.6249
			curvature_cs = 7.5029
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTCCT':
			curvature_bmht = 1.4661
			curvature_cs = 8.3716
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTCGA':
			curvature_bmht = 0.9119
			curvature_cs = 12.757
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTCGC':
			curvature_bmht = 3.0504
			curvature_cs = 14.5274
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTCGG':
			curvature_bmht = 4.7163
			curvature_cs = 10.5436
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTCGT':
			curvature_bmht = 3.7157
			curvature_cs = 11.2063
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTCTA':
			curvature_bmht = 5.5809
			curvature_cs = 10.9362
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTCTC':
			curvature_bmht = 6.441
			curvature_cs = 11.9928
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTCTG':
			curvature_bmht = 8.9542
			curvature_cs = 11.6692
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTCTT':
			curvature_bmht = 2.2158
			curvature_cs = 9.9068
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTGAA':
			curvature_bmht = 3.7597
			curvature_cs = 9.3649
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTGAC':
			curvature_bmht = 4.4782
			curvature_cs = 10.0082
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTGAG':
			curvature_bmht = 9.1379
			curvature_cs = 7.3729
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTGAT':
			curvature_bmht = 3.9262
			curvature_cs = 9.1986
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTGCA':
			curvature_bmht = 7.2199
			curvature_cs = 10.725
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTGCC':
			curvature_bmht = 4.8152
			curvature_cs = 9.6755
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTGCG':
			curvature_bmht = 7.0061
			curvature_cs = 11.1327
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTGCT':
			curvature_bmht = 7.6895
			curvature_cs = 11.7738
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTGGA':
			curvature_bmht = 8.2524
			curvature_cs = 5.2544
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTGGC':
			curvature_bmht = 9.5023
			curvature_cs = 5.929
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTGGG':
			curvature_bmht = 12.0326
			curvature_cs = 5.8193
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTGGT':
			curvature_bmht = 10.9527
			curvature_cs = 5.1437
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTGTA':
			curvature_bmht = 8.9398
			curvature_cs = 6.7211
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTGTC':
			curvature_bmht = 10.0076
			curvature_cs = 8.0236
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTGTG':
			curvature_bmht = 10.4008
			curvature_cs = 5.7193
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTGTT':
			curvature_bmht = 5.74
			curvature_cs = 5.5385
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTTAA':
			curvature_bmht = 5.5541
			curvature_cs = 7.968
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTTAC':
			curvature_bmht = 6.5405
			curvature_cs = 8.9839
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTTAG':
			curvature_bmht = 7.6668
			curvature_cs = 6.1885
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTTAT':
			curvature_bmht = 6.2522
			curvature_cs = 7.9655
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTTCA':
			curvature_bmht = 5.9265
			curvature_cs = 13.9683
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTTCC':
			curvature_bmht = 5.6242
			curvature_cs = 9.344
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTTCG':
			curvature_bmht = 3.2855
			curvature_cs = 10.8352
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTTCT':
			curvature_bmht = 2.9811
			curvature_cs = 10.9603
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTTGA':
			curvature_bmht = 15.3083
			curvature_cs = 9.5948
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTTGC':
			curvature_bmht = 14.02
			curvature_cs = 11.8692
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTTGG':
			curvature_bmht = 11.5165
			curvature_cs = 6.5261
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTTGT':
			curvature_bmht = 12.5082
			curvature_cs = 7.6526
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTTTA':
			curvature_bmht = 12.413
			curvature_cs = 7.4648
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTTTC':
			curvature_bmht = 11.4381
			curvature_cs = 9.1204
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTTTG':
			curvature_bmht = 15.6895
			curvature_cs = 6.0323
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'CTTTT':
			curvature_bmht = 15.6896
			curvature_cs = 6.0323
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAAAA':
			curvature_bmht = 16.266
			curvature_cs = 11.1388
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAAAC':
			curvature_bmht = 14.806
			curvature_cs = 11.3521
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAAAG':
			curvature_bmht = 11.0122
			curvature_cs = 9.1204
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAAAT':
			curvature_bmht = 15.2574
			curvature_cs = 10.8204
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAACA':
			curvature_bmht = 9.5801
			curvature_cs = 10.8669
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAACC':
			curvature_bmht = 11.8175
			curvature_cs = 9.7792
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAACG':
			curvature_bmht = 9.9538
			curvature_cs = 11.1232
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAACT':
			curvature_bmht = 9.6483
			curvature_cs = 12.1528
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAAGA':
			curvature_bmht = 8.7641
			curvature_cs = 8.2715
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAAGC':
			curvature_bmht = 6.4924
			curvature_cs = 10.1457
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAAGG':
			curvature_bmht = 6.1716
			curvature_cs = 6.1223
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAAGT':
			curvature_bmht = 6.3103
			curvature_cs = 6.708
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAATA':
			curvature_bmht = 11.8176
			curvature_cs = 12.7779
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAATC':
			curvature_bmht = 11.5298
			curvature_cs = 14.0887
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAATG':
			curvature_bmht = 10.4089
			curvature_cs = 11.4349
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAATT':
			curvature_bmht = 15.5381
			curvature_cs = 11.5354
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GACAA':
			curvature_bmht = 6.8702
			curvature_cs = 15.6764
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GACAC':
			curvature_bmht = 4.1342
			curvature_cs = 11.9463
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GACAG':
			curvature_bmht = 9.1446
			curvature_cs = 13.7318
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GACAT':
			curvature_bmht = 3.6156
			curvature_cs = 11.3145
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GACCA':
			curvature_bmht = 9.6377
			curvature_cs = 6.9915
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GACCC':
			curvature_bmht = 9.6378
			curvature_cs = 6.9916
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GACCG':
			curvature_bmht = 10.0949
			curvature_cs = 8.3432
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GACCT':
			curvature_bmht = 10.546
			curvature_cs = 9.3798
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GACGA':
			curvature_bmht = 9.2331
			curvature_cs = 13.4377
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GACGC':
			curvature_bmht = 6.7323
			curvature_cs = 15.0784
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GACGG':
			curvature_bmht = 8.5908
			curvature_cs = 11.422
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GACGT':
			curvature_bmht = 8.0107
			curvature_cs = 11.9906
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GACTA':
			curvature_bmht = 9.8919
			curvature_cs = 11.9195
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GACTC':
			curvature_bmht = 7.3005
			curvature_cs = 12.8902
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GACTG':
			curvature_bmht = 13.3719
			curvature_cs = 12.8135
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GACTT':
			curvature_bmht = 7.8944
			curvature_cs = 10.9517
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAGAA':
			curvature_bmht = 3.5822
			curvature_cs = 13.7162
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAGAC':
			curvature_bmht = 6.7435
			curvature_cs = 14.7896
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAGAG':
			curvature_bmht = 10.4486
			curvature_cs = 11.9928
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAGAT':
			curvature_bmht = 5.9374
			curvature_cs = 13.7524
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAGCA':
			curvature_bmht = 2.4118
			curvature_cs = 15.2488
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAGCC':
			curvature_bmht = 2.8747
			curvature_cs = 14.3288
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAGCG':
			curvature_bmht = 5.0812
			curvature_cs = 15.8201
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAGCT':
			curvature_bmht = 5.9511
			curvature_cs = 15.8824
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAGGA':
			curvature_bmht = 5.4044
			curvature_cs = 8.0739
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAGGC':
			curvature_bmht = 4.6758
			curvature_cs = 10.0523
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAGGG':
			curvature_bmht = 8.0013
			curvature_cs = 5.7195
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAGGT':
			curvature_bmht = 6.8117
			curvature_cs = 6.412
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAGTA':
			curvature_bmht = 5.6603
			curvature_cs = 11.2749
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAGTC':
			curvature_bmht = 4.71
			curvature_cs = 12.8783
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAGTG':
			curvature_bmht = 6.3199
			curvature_cs = 9.1563
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GAGTT':
			curvature_bmht = 2.0954
			curvature_cs = 9.8532
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GATAA':
			curvature_bmht = 6.6283
			curvature_cs = 14.1511
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GATAC':
			curvature_bmht = 7.8367
			curvature_cs = 14.7048
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GATAG':
			curvature_bmht = 8.8191
			curvature_cs = 12.1439
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GATAT':
			curvature_bmht = 7.5202
			curvature_cs = 13.9591
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GATCA':
			curvature_bmht = 6.1291
			curvature_cs = 19.1236
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GATCC':
			curvature_bmht = 6.5456
			curvature_cs = 15.1542
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GATCG':
			curvature_bmht = 4.5058
			curvature_cs = 16.6035
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GATCT':
			curvature_bmht = 4.277
			curvature_cs = 17.2416
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GATGA':
			curvature_bmht = 11.6766
			curvature_cs = 19.0713
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GATGC':
			curvature_bmht = 5.2943
			curvature_cs = 15.1753
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GATGG':
			curvature_bmht = 7.9191
			curvature_cs = 16.6055
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GATGT':
			curvature_bmht = 4.1473
			curvature_cs = 12.4083
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GATTA':
			curvature_bmht = 13.5597
			curvature_cs = 12.8634
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GATTC':
			curvature_bmht = 12.4198
			curvature_cs = 14.2202
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GATTG':
			curvature_bmht = 16.7052
			curvature_cs = 11.5872
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GATTT':
			curvature_bmht = 16.7052
			curvature_cs = 11.5872
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCAAA':
			curvature_bmht = 15.6971
			curvature_cs = 21.7174
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCAAC':
			curvature_bmht = 14.59
			curvature_cs = 22.0566
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCAAG':
			curvature_bmht = 11.2418
			curvature_cs = 19.6883
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCAAT':
			curvature_bmht = 14.9478
			curvature_cs = 21.4544
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCACA':
			curvature_bmht = 3.6557
			curvature_cs = 10.7224
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCACC':
			curvature_bmht = 5.6846
			curvature_cs = 9.641
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCACG':
			curvature_bmht = 3.9313
			curvature_cs = 11.0314
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCACT':
			curvature_bmht = 3.885
			curvature_cs = 11.9356
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCAGA':
			curvature_bmht = 10.3333
			curvature_cs = 18.9365
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCAGC':
			curvature_bmht = 7.9438
			curvature_cs = 20.5872
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCAGG':
			curvature_bmht = 7.9471
			curvature_cs = 16.7669
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCAGT':
			curvature_bmht = 8.014
			curvature_cs = 17.4321
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCATA':
			curvature_bmht = 6.0487
			curvature_cs = 12.8389
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCATC':
			curvature_bmht = 6.8187
			curvature_cs = 14.2115
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCATG':
			curvature_bmht = 4.962
			curvature_cs = 11.3455
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCATT':
			curvature_bmht = 10.0927
			curvature_cs = 11.5516
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCCAA':
			curvature_bmht = 6.1638
			curvature_cs = 6.6572
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCCAC':
			curvature_bmht = 8.0995
			curvature_cs = 7.8162
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCCAG':
			curvature_bmht = 9.9456
			curvature_cs = 5.037
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCCAT':
			curvature_bmht = 7.6053
			curvature_cs = 6.7267
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCCCA':
			curvature_bmht = 8.891
			curvature_cs = 3.4439
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCCCC':
			curvature_bmht = 8.8911
			curvature_cs = 3.4439
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCCCG':
			curvature_bmht = 9.3051
			curvature_cs = 4.9373
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCCCT':
			curvature_bmht = 9.7576
			curvature_cs = 5.4344
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCCGA':
			curvature_bmht = 8.4441
			curvature_cs = 10.3881
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCCGC':
			curvature_bmht = 5.947
			curvature_cs = 12.4085
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCCGG':
			curvature_bmht = 7.895
			curvature_cs = 7.8066
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCCGT':
			curvature_bmht = 7.2721
			curvature_cs = 8.6479
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCCTA':
			curvature_bmht = 9.222
			curvature_cs = 8.0143
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCCTC':
			curvature_bmht = 6.7133
			curvature_cs = 9.202
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCCTG':
			curvature_bmht = 12.7727
			curvature_cs = 8.6404
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCCTT':
			curvature_bmht = 7.1112
			curvature_cs = 6.9109
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCGAA':
			curvature_bmht = 4.7231
			curvature_cs = 15.7878
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCGAC':
			curvature_bmht = 6.2553
			curvature_cs = 16.5121
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCGAG':
			curvature_bmht = 8.1275
			curvature_cs = 13.8354
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCGAT':
			curvature_bmht = 5.8234
			curvature_cs = 15.6661
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCGCA':
			curvature_bmht = 1.6365
			curvature_cs = 17.1978
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCGCC':
			curvature_bmht = 3.6849
			curvature_cs = 16.1632
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCGCG':
			curvature_bmht = 2.706
			curvature_cs = 17.6312
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCGCT':
			curvature_bmht = 3.1333
			curvature_cs = 18.1548
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCGGA':
			curvature_bmht = 2.028
			curvature_cs = 10.8235
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCGGC':
			curvature_bmht = 1.0226
			curvature_cs = 12.2059
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCGGG':
			curvature_bmht = 4.0645
			curvature_cs = 9.3832
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCGGT':
			curvature_bmht = 2.8672
			curvature_cs = 9.6564
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCGTA':
			curvature_bmht = 1.8998
			curvature_cs = 13.1591
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCGTC':
			curvature_bmht = 1.6784
			curvature_cs = 14.5269
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCGTG':
			curvature_bmht = 2.3489
			curvature_cs = 11.6699
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCGTT':
			curvature_bmht = 2.9412
			curvature_cs = 11.874
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCTAA':
			curvature_bmht = 2.5151
			curvature_cs = 9.7369
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCTAC':
			curvature_bmht = 3.6442
			curvature_cs = 10.0096
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCTAG':
			curvature_bmht = 8.4049
			curvature_cs = 7.7132
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCTAT':
			curvature_bmht = 2.9506
			curvature_cs = 9.4345
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCTCA':
			curvature_bmht = 6.4657
			curvature_cs = 14.1706
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCTCC':
			curvature_bmht = 2.9856
			curvature_cs = 10.4833
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCTCG':
			curvature_bmht = 4.825
			curvature_cs = 11.8709
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCTCT':
			curvature_bmht = 5.4952
			curvature_cs = 12.7766
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCTGA':
			curvature_bmht = 9.9544
			curvature_cs = 10.7612
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCTGC':
			curvature_bmht = 9.1133
			curvature_cs = 11.6746
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCTGG':
			curvature_bmht = 12.4597
			curvature_cs = 10.0867
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCTGT':
			curvature_bmht = 11.2913
			curvature_cs = 10.0207
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCTTA':
			curvature_bmht = 4.4521
			curvature_cs = 8.1179
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCTTC':
			curvature_bmht = 3.7133
			curvature_cs = 9.3316
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCTTG':
			curvature_bmht = 7.7454
			curvature_cs = 6.9903
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GCTTT':
			curvature_bmht = 7.7455
			curvature_cs = 6.9903
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGAAA':
			curvature_bmht = 10.5504
			curvature_cs = 11.3648
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGAAC':
			curvature_bmht = 9.5602
			curvature_cs = 11.8575
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGAAG':
			curvature_bmht = 6.9463
			curvature_cs = 9.3439
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGAAT':
			curvature_bmht = 9.854
			curvature_cs = 11.1449
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGACA':
			curvature_bmht = 6.9955
			curvature_cs = 11.2589
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGACC':
			curvature_bmht = 9.4112
			curvature_cs = 10.1978
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGACG':
			curvature_bmht = 9.1004
			curvature_cs = 11.639
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGACT':
			curvature_bmht = 9.3548
			curvature_cs = 12.3528
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGAGA':
			curvature_bmht = 10.439
			curvature_cs = 9.2638
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGAGC':
			curvature_bmht = 7.9657
			curvature_cs = 11.3769
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGAGG':
			curvature_bmht = 9.8923
			curvature_cs = 6.5428
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGAGT':
			curvature_bmht = 9.3054
			curvature_cs = 7.4549
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGATA':
			curvature_bmht = 8.416
			curvature_cs = 13.6311
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGATC':
			curvature_bmht = 6.8939
			curvature_cs = 15.07
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGATG':
			curvature_bmht = 6.817
			curvature_cs = 11.9538
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGATT':
			curvature_bmht = 11.1988
			curvature_cs = 12.2966
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGCAA':
			curvature_bmht = 13.3186
			curvature_cs = 22.8557
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGCAC':
			curvature_bmht = 5.5104
			curvature_cs = 13.4947
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGCAG':
			curvature_bmht = 9.7012
			curvature_cs = 20.9616
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGCAT':
			curvature_bmht = 5.8455
			curvature_cs = 12.808
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGCCA':
			curvature_bmht = 9.1959
			curvature_cs = 8.4006
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGCCC':
			curvature_bmht = 9.1959
			curvature_cs = 8.4006
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGCCG':
			curvature_bmht = 8.1053
			curvature_cs = 9.8093
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGCCT':
			curvature_bmht = 8.129
			curvature_cs = 10.6677
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGCGA':
			curvature_bmht = 7.0598
			curvature_cs = 15.011
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGCGC':
			curvature_bmht = 4.8346
			curvature_cs = 16.7044
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGCGG':
			curvature_bmht = 4.5854
			curvature_cs = 12.8571
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGCGT':
			curvature_bmht = 4.6232
			curvature_cs = 13.5015
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGCTA':
			curvature_bmht = 5.5553
			curvature_cs = 13.2385
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGCTC':
			curvature_bmht = 2.6576
			curvature_cs = 14.3073
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGCTG':
			curvature_bmht = 8.5957
			curvature_cs = 13.8103
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGCTT':
			curvature_bmht = 5.5751
			curvature_cs = 12.1803
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGGAA':
			curvature_bmht = 7.6164
			curvature_cs = 7.865
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGGAC':
			curvature_bmht = 7.1709
			curvature_cs = 8.8823
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGGAG':
			curvature_bmht = 6.0891
			curvature_cs = 6.0867
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGGAT':
			curvature_bmht = 7.2805
			curvature_cs = 7.8628
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGGCA':
			curvature_bmht = 5.8036
			curvature_cs = 9.3739
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGGCC':
			curvature_bmht = 6.8906
			curvature_cs = 8.4298
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGGCG':
			curvature_bmht = 4.0326
			curvature_cs = 9.9232
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGGCT':
			curvature_bmht = 3.2997
			curvature_cs = 10.1269
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGGGA':
			curvature_bmht = 2.9881
			curvature_cs = 2.7239
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGGGC':
			curvature_bmht = 4.102
			curvature_cs = 4.1929
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGGGG':
			curvature_bmht = 2.222
			curvature_cs = 3.3789
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGGGT':
			curvature_bmht = 2.3648
			curvature_cs = 2.4683
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGGTA':
			curvature_bmht = 2.5619
			curvature_cs = 5.3695
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGGTC':
			curvature_bmht = 4.7125
			curvature_cs = 6.9719
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGGTG':
			curvature_bmht = 2.4481
			curvature_cs = 3.5086
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGGTT':
			curvature_bmht = 6.6511
			curvature_cs = 3.9562
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGTAA':
			curvature_bmht = 4.8414
			curvature_cs = 8.8224
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGTAC':
			curvature_bmht = 3.7747
			curvature_cs = 9.6761
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGTAG':
			curvature_bmht = 4.1043
			curvature_cs = 6.9228
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGTAT':
			curvature_bmht = 3.9477
			curvature_cs = 8.7448
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGTCA':
			curvature_bmht = 7.8713
			curvature_cs = 14.5327
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGTCC':
			curvature_bmht = 5.5954
			curvature_cs = 10.0726
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGTCG':
			curvature_bmht = 2.7101
			curvature_cs = 11.5651
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGTCT':
			curvature_bmht = 1.8252
			curvature_cs = 11.8769
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGTGA':
			curvature_bmht = 6.9596
			curvature_cs = 13.1901
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGTGC':
			curvature_bmht = 4.3998
			curvature_cs = 10.3614
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGTGG':
			curvature_bmht = 3.3211
			curvature_cs = 10.4946
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGTGT':
			curvature_bmht = 2.3131
			curvature_cs = 6.9271
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGTTA':
			curvature_bmht = 10.4961
			curvature_cs = 8.0154
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGTTC':
			curvature_bmht = 10.3828
			curvature_cs = 9.6052
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGTTG':
			curvature_bmht = 14.2925
			curvature_cs = 6.6025
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GGTTT':
			curvature_bmht = 14.2925
			curvature_cs = 6.6025
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTAAA':
			curvature_bmht = 10.5581
			curvature_cs = 10.955
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTAAC':
			curvature_bmht = 8.2764
			curvature_cs = 11.3959
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTAAG':
			curvature_bmht = 3.9295
			curvature_cs = 8.9283
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTAAT':
			curvature_bmht = 8.9143
			curvature_cs = 10.7151
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTACA':
			curvature_bmht = 2.7205
			curvature_cs = 10.8166
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTACC':
			curvature_bmht = 5.1646
			curvature_cs = 9.7477
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTACG':
			curvature_bmht = 4.7389
			curvature_cs = 11.1752
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTACT':
			curvature_bmht = 5.1194
			curvature_cs = 11.9508
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTAGA':
			curvature_bmht = 6.9662
			curvature_cs = 8.7259
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTAGC':
			curvature_bmht = 4.9329
			curvature_cs = 10.8185
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTAGG':
			curvature_bmht = 7.924
			curvature_cs = 6.0759
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTAGT':
			curvature_bmht = 6.9334
			curvature_cs = 6.9422
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTATA':
			curvature_bmht = 4.7091
			curvature_cs = 13.1175
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTATC':
			curvature_bmht = 4.6981
			curvature_cs = 14.5409
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTATG':
			curvature_bmht = 3.2639
			curvature_cs = 11.4901
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTATT':
			curvature_bmht = 8.4232
			curvature_cs = 11.7944
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTCAA':
			curvature_bmht = 13.0644
			curvature_cs = 19.1576
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTCAC':
			curvature_bmht = 10.3455
			curvature_cs = 19.9577
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTCAG':
			curvature_bmht = 5.583
			curvature_cs = 17.2428
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTCAT':
			curvature_bmht = 11.1069
			curvature_cs = 19.0708
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTCCA':
			curvature_bmht = 6.8775
			curvature_cs = 8.8241
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTCCC':
			curvature_bmht = 6.8775
			curvature_cs = 8.8241
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTCCG':
			curvature_bmht = 4.809
			curvature_cs = 10.2219
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTCCT':
			curvature_bmht = 4.548
			curvature_cs = 11.1107
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTCGA':
			curvature_bmht = 3.8141
			curvature_cs = 15.3906
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTCGC':
			curvature_bmht = 2.8589
			curvature_cs = 17.0525
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTCGG':
			curvature_bmht = 0.7444
			curvature_cs = 13.2783
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTCGT':
			curvature_bmht = 0.9836
			curvature_cs = 13.9038
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTCTA':
			curvature_bmht = 2.1352
			curvature_cs = 13.679
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTCTC':
			curvature_bmht = 1.8072
			curvature_cs = 14.7326
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTCTG':
			curvature_bmht = 5.9728
			curvature_cs = 14.2716
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTCTT':
			curvature_bmht = 2.6737
			curvature_cs = 12.63
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTGAA':
			curvature_bmht = 10.0955
			curvature_cs = 17.6006
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTGAC':
			curvature_bmht = 10.3751
			curvature_cs = 18.3023
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTGAG':
			curvature_bmht = 9.4835
			curvature_cs = 15.6409
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTGAT':
			curvature_bmht = 10.3354
			curvature_cs = 17.4712
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTGCA':
			curvature_bmht = 6.4124
			curvature_cs = 14.262
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTGCC':
			curvature_bmht = 7.4975
			curvature_cs = 13.24
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTGCG':
			curvature_bmht = 4.6164
			curvature_cs = 14.7177
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTGCT':
			curvature_bmht = 3.8519
			curvature_cs = 15.188
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTGGA':
			curvature_bmht = 5.5159
			curvature_cs = 12.6313
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTGGC':
			curvature_bmht = 4.8497
			curvature_cs = 14.0257
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTGGG':
			curvature_bmht = 1.7155
			curvature_cs = 11.0629
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTGGT':
			curvature_bmht = 2.8502
			curvature_cs = 11.4127
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTGTA':
			curvature_bmht = 3.1762
			curvature_cs = 10.2145
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTGTC':
			curvature_bmht = 5.2098
			curvature_cs = 11.6262
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTGTG':
			curvature_bmht = 2.932
			curvature_cs = 8.6975
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTGTT':
			curvature_bmht = 7.2671
			curvature_cs = 8.9094
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTTAA':
			curvature_bmht = 10.1805
			curvature_cs = 10.5078
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTTAC':
			curvature_bmht = 11.1224
			curvature_cs = 11.352
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTTAG':
			curvature_bmht = 11.0488
			curvature_cs = 8.6065
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTTAT':
			curvature_bmht = 10.9155
			curvature_cs = 10.43
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTTCA':
			curvature_bmht = 9.0998
			curvature_cs = 16.1724
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTTCC':
			curvature_bmht = 10.0799
			curvature_cs = 11.7529
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTTCG':
			curvature_bmht = 7.9845
			curvature_cs = 13.2444
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTTCT':
			curvature_bmht = 7.6107
			curvature_cs = 13.5584
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTTGA':
			curvature_bmht = 19.9714
			curvature_cs = 11.8107
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTTGC':
			curvature_bmht = 18.5682
			curvature_cs = 13.9356
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTTGG':
			curvature_bmht = 16.1931
			curvature_cs = 8.985
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTTGT':
			curvature_bmht = 17.1564
			curvature_cs = 9.9709
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTTTA':
			curvature_bmht = 17.0971
			curvature_cs = 9.6664
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTTTC':
			curvature_bmht = 15.9594
			curvature_cs = 11.2309
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTTTG':
			curvature_bmht = 20.2516
			curvature_cs = 8.2639
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'GTTTT':
			curvature_bmht = 20.2516
			curvature_cs = 8.2639
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAAAA':
			curvature_bmht = 17.0099
			curvature_cs = 8.3752
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAAAC':
			curvature_bmht = 15.0261
			curvature_cs = 8.8234
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAAAG':
			curvature_bmht = 10.6693
			curvature_cs = 6.3468
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAAAT':
			curvature_bmht = 15.6139
			curvature_cs = 8.13
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAACA':
			curvature_bmht = 8.6369
			curvature_cs = 8.2331
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAACC':
			curvature_bmht = 10.5271
			curvature_cs = 7.1672
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAACG':
			curvature_bmht = 8.1447
			curvature_cs = 8.6047
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAACT':
			curvature_bmht = 7.6329
			curvature_cs = 9.3745
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAAGA':
			curvature_bmht = 6.1028
			curvature_cs = 6.3833
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAAGC':
			curvature_bmht = 4.1791
			curvature_cs = 8.6331
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAAGG':
			curvature_bmht = 3.2444
			curvature_cs = 3.5092
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAAGT':
			curvature_bmht = 3.4536
			curvature_cs = 4.4857
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAATA':
			curvature_bmht = 11.0295
			curvature_cs = 10.644
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAATC':
			curvature_bmht = 11.4841
			curvature_cs = 12.1257
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAATG':
			curvature_bmht = 9.8712
			curvature_cs = 8.9195
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAATT':
			curvature_bmht = 15.0465
			curvature_cs = 9.2891
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TACAA':
			curvature_bmht = 5.7034
			curvature_cs = 13.3566
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TACAC':
			curvature_bmht = 1.5048
			curvature_cs = 9.6356
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TACAG':
			curvature_bmht = 6.2155
			curvature_cs = 11.5198
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TACAT':
			curvature_bmht = 1.5841
			curvature_cs = 8.8325
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TACCA':
			curvature_bmht = 6.7821
			curvature_cs = 4.3568
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TACCC':
			curvature_bmht = 6.7821
			curvature_cs = 4.3568
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TACCG':
			curvature_bmht = 7.1924
			curvature_cs = 5.8248
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TACCT':
			curvature_bmht = 7.6902
			curvature_cs = 6.5245
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TACGA':
			curvature_bmht = 6.3698
			curvature_cs = 11.2104
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TACGC':
			curvature_bmht = 3.9405
			curvature_cs = 13.1255
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TACGG':
			curvature_bmht = 6.3943
			curvature_cs = 8.7962
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TACGT':
			curvature_bmht = 5.5692
			curvature_cs = 9.5528
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TACTA':
			curvature_bmht = 7.8047
			curvature_cs = 9.0992
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TACTC':
			curvature_bmht = 5.735
			curvature_cs = 10.2214
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TACTG':
			curvature_bmht = 11.5734
			curvature_cs = 9.7987
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TACTT':
			curvature_bmht = 5.1141
			curvature_cs = 8.0364
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAGAA':
			curvature_bmht = 0.7119
			curvature_cs = 12.082
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAGAC':
			curvature_bmht = 4.0201
			curvature_cs = 13.3756
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAGAG':
			curvature_bmht = 8.2998
			curvature_cs = 10.6329
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAGAT':
			curvature_bmht = 3.1605
			curvature_cs = 12.2387
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAGCA':
			curvature_bmht = 3.2349
			curvature_cs = 13.6452
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAGCC':
			curvature_bmht = 0.9858
			curvature_cs = 12.8496
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAGCG':
			curvature_bmht = 3.9118
			curvature_cs = 14.2991
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAGCT':
			curvature_bmht = 4.796
			curvature_cs = 14.0148
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAGGA':
			curvature_bmht = 4.8914
			curvature_cs = 6.268
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAGGC':
			curvature_bmht = 5.6075
			curvature_cs = 8.5837
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAGGG':
			curvature_bmht = 8.448
			curvature_cs = 3.2109
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAGGT':
			curvature_bmht = 7.2935
			curvature_cs = 4.3122
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAGTA':
			curvature_bmht = 5.4685
			curvature_cs = 9.9313
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAGTC':
			curvature_bmht = 6.0487
			curvature_cs = 11.6166
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAGTG':
			curvature_bmht = 6.7377
			curvature_cs = 7.4551
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TAGTT':
			curvature_bmht = 1.75
			curvature_cs = 8.5158
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TATAA':
			curvature_bmht = 5.5184
			curvature_cs = 11.789
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TATAC':
			curvature_bmht = 5.5225
			curvature_cs = 12.5715
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TATAG':
			curvature_bmht = 5.8926
			curvature_cs = 9.8574
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TATAT':
			curvature_bmht = 5.4621
			curvature_cs = 11.6866
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TATCA':
			curvature_bmht = 7.1955
			curvature_cs = 17.3115
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TATCC':
			curvature_bmht = 5.9337
			curvature_cs = 12.9852
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TATCG':
			curvature_bmht = 3.0328
			curvature_cs = 14.4717
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TATCT':
			curvature_bmht = 2.2852
			curvature_cs = 14.8539
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TATGA':
			curvature_bmht = 10.023
			curvature_cs = 16.9899
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TATGC':
			curvature_bmht = 4.5726
			curvature_cs = 13.1925
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TATGG':
			curvature_bmht = 6.2431
			curvature_cs = 14.2645
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TATGT':
			curvature_bmht = 2.5103
			curvature_cs = 9.9108
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TATTA':
			curvature_bmht = 11.9488
			curvature_cs = 10.8391
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TATTC':
			curvature_bmht = 11.4065
			curvature_cs = 12.3593
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TATTG':
			curvature_bmht = 15.5242
			curvature_cs = 9.4597
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TATTT':
			curvature_bmht = 15.5242
			curvature_cs = 9.4597
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCAAA':
			curvature_bmht = 18.221
			curvature_cs = 16.6052
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCAAC':
			curvature_bmht = 15.8109
			curvature_cs = 17.1147
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCAAG':
			curvature_bmht = 11.1307
			curvature_cs = 14.5913
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCAAT':
			curvature_bmht = 16.5075
			curvature_cs = 16.3994
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCACA':
			curvature_bmht = 8.647
			curvature_cs = 16.5175
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCACC':
			curvature_bmht = 9.9558
			curvature_cs = 15.457
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCACG':
			curvature_bmht = 7.1195
			curvature_cs = 16.8953
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCACT':
			curvature_bmht = 6.3635
			curvature_cs = 17.5844
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCAGA':
			curvature_bmht = 3.8265
			curvature_cs = 14.3619
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCAGC':
			curvature_bmht = 3.1632
			curvature_cs = 16.3088
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCAGG':
			curvature_bmht = 0.3033
			curvature_cs = 11.7966
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCAGT':
			curvature_bmht = 1.0862
			curvature_cs = 12.6483
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCATA':
			curvature_bmht = 10.9978
			curvature_cs = 18.8124
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCATC':
			curvature_bmht = 12.183
			curvature_cs = 20.192
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCATG':
			curvature_bmht = 10.1973
			curvature_cs = 17.2101
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCATT':
			curvature_bmht = 15.1199
			curvature_cs = 17.5076
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCCAA':
			curvature_bmht = 5.0012
			curvature_cs = 5.8863
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCCAC':
			curvature_bmht = 5.9888
			curvature_cs = 7.2388
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCCAG':
			curvature_bmht = 7.3415
			curvature_cs = 4.5992
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCCAT':
			curvature_bmht = 5.6839
			curvature_cs = 6.073
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCCCA':
			curvature_bmht = 6.5964
			curvature_cs = 2.7238
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCCCC':
			curvature_bmht = 6.5964
			curvature_cs = 2.724
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCCCG':
			curvature_bmht = 6.7146
			curvature_cs = 4.1495
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCCCT':
			curvature_bmht = 7.1522
			curvature_cs = 4.2084
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCCGA':
			curvature_bmht = 5.8396
			curvature_cs = 9.5762
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCCGC':
			curvature_bmht = 3.3456
			curvature_cs = 11.735
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCCGG':
			curvature_bmht = 5.6526
			curvature_cs = 6.7476
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCCGT':
			curvature_bmht = 4.8536
			curvature_cs = 7.7249
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCCTA':
			curvature_bmht = 7.0592
			curvature_cs = 6.7707
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCCTC':
			curvature_bmht = 5.0048
			curvature_cs = 8.0739
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCCTG':
			curvature_bmht = 10.824
			curvature_cs = 7.2074
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCCTT':
			curvature_bmht = 4.5146
			curvature_cs = 5.5863
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCGAA':
			curvature_bmht = 4.3156
			curvature_cs = 14.7597
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCGAC':
			curvature_bmht = 4.3278
			curvature_cs = 15.582
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCGAG':
			curvature_bmht = 5.5252
			curvature_cs = 12.8527
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCGAT':
			curvature_bmht = 4.2071
			curvature_cs = 14.6788
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCGCA':
			curvature_bmht = 3.3171
			curvature_cs = 16.2105
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCGCC':
			curvature_bmht = 3.6593
			curvature_cs = 15.2004
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCGCG':
			curvature_bmht = 0.7274
			curvature_cs = 16.6836
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCGCT':
			curvature_bmht = 0.5275
			curvature_cs = 17.0875
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCGGA':
			curvature_bmht = 0.7549
			curvature_cs = 9.5937
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCGGC':
			curvature_bmht = 3.2448
			curvature_cs = 11.1277
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCGGG':
			curvature_bmht = 4.441
			curvature_cs = 7.9838
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCGGT':
			curvature_bmht = 3.5373
			curvature_cs = 8.3209
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCGTA':
			curvature_bmht = 1.457
			curvature_cs = 12.1591
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCGTC':
			curvature_bmht = 4.0664
			curvature_cs = 13.6024
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCGTG':
			curvature_bmht = 3.0536
			curvature_cs = 10.5006
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCGTT':
			curvature_bmht = 3.6387
			curvature_cs = 10.8252
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCTAA':
			curvature_bmht = 4.4616
			curvature_cs = 8.4126
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCTAC':
			curvature_bmht = 3.2237
			curvature_cs = 8.8019
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCTAG':
			curvature_bmht = 7.3187
			curvature_cs = 6.383
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCTAT':
			curvature_bmht = 3.1477
			curvature_cs = 8.1461
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCTCA':
			curvature_bmht = 8.9538
			curvature_cs = 13.1873
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCTCC':
			curvature_bmht = 5.2914
			curvature_cs = 9.2638
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCTCG':
			curvature_bmht = 6.0838
			curvature_cs = 10.6889
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCTCT':
			curvature_bmht = 6.4436
			curvature_cs = 11.4788
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCTGA':
			curvature_bmht = 8.9759
			curvature_cs = 9.3428
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCTGC':
			curvature_bmht = 8.8206
			curvature_cs = 10.3349
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCTGG':
			curvature_bmht = 12.0803
			curvature_cs = 8.677
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCTGT':
			curvature_bmht = 10.8829
			curvature_cs = 8.5869
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCTTA':
			curvature_bmht = 3.6332
			curvature_cs = 6.9355
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCTTC':
			curvature_bmht = 4.7307
			curvature_cs = 8.2716
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCTTG':
			curvature_bmht = 7.6897
			curvature_cs = 5.7194
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TCTTT':
			curvature_bmht = 7.6897
			curvature_cs = 5.7194
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGAAA':
			curvature_bmht = 8.009
			curvature_cs = 11.9573
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGAAC':
			curvature_bmht = 7.3472
			curvature_cs = 11.3333
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGAAG':
			curvature_bmht = 5.8633
			curvature_cs = 10.3551
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGAAT':
			curvature_bmht = 7.5203
			curvature_cs = 11.4224
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGACA':
			curvature_bmht = 6.9147
			curvature_cs = 11.2684
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGACC':
			curvature_bmht = 9.0807
			curvature_cs = 10.3298
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGACG':
			curvature_bmht = 9.6012
			curvature_cs = 11.1151
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGACT':
			curvature_bmht = 10.0761
			curvature_cs = 12.8809
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGAGA':
			curvature_bmht = 11.82
			curvature_cs = 7.4681
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGAGC':
			curvature_bmht = 9.5293
			curvature_cs = 7.9289
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGAGG':
			curvature_bmht = 11.936
			curvature_cs = 7.8435
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGAGT':
			curvature_bmht = 11.1907
			curvature_cs = 7.3045
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGATA':
			curvature_bmht = 7.6004
			curvature_cs = 11.4313
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGATC':
			curvature_bmht = 5.3536
			curvature_cs = 12.1385
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGATG':
			curvature_bmht = 6.1092
			curvature_cs = 11.361
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGATT':
			curvature_bmht = 9.5464
			curvature_cs = 10.6907
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGCAA':
			curvature_bmht = 13.6561
			curvature_cs = 24.6109
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGCAC':
			curvature_bmht = 5.6826
			curvature_cs = 15.4251
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGCAG':
			curvature_bmht = 9.6623
			curvature_cs = 22.6758
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGCAT':
			curvature_bmht = 6.1032
			curvature_cs = 14.81
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGCCA':
			curvature_bmht = 8.9696
			curvature_cs = 10.4741
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGCCC':
			curvature_bmht = 8.9696
			curvature_cs = 10.4741
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGCCG':
			curvature_bmht = 7.6913
			curvature_cs = 11.8387
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGCCT':
			curvature_bmht = 7.6577
			curvature_cs = 12.8102
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGCGA':
			curvature_bmht = 6.6429
			curvature_cs = 16.8973
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGCGC':
			curvature_bmht = 4.5501
			curvature_cs = 18.4556
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGCGG':
			curvature_bmht = 3.9663
			curvature_cs = 14.9145
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGCGT':
			curvature_bmht = 4.0932
			curvature_cs = 15.4832
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGCTA':
			curvature_bmht = 4.8987
			curvature_cs = 15.3698
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGCTC':
			curvature_bmht = 1.9955
			curvature_cs = 16.3794
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGCTG':
			curvature_bmht = 7.9512
			curvature_cs = 16.0119
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGCTT':
			curvature_bmht = 5.1826
			curvature_cs = 14.3459
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGGAA':
			curvature_bmht = 5.1984
			curvature_cs = 7.5271
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGGAC':
			curvature_bmht = 5.5434
			curvature_cs = 6.9138
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGGAG':
			curvature_bmht = 6.3395
			curvature_cs = 6.0215
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGGAT':
			curvature_bmht = 5.3907
			curvature_cs = 6.9849
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGGCA':
			curvature_bmht = 3.2894
			curvature_cs = 7.9922
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGGCC':
			curvature_bmht = 4.3784
			curvature_cs = 7.0236
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGGCG':
			curvature_bmht = 1.8305
			curvature_cs = 7.8991
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGGCT':
			curvature_bmht = 1.603
			curvature_cs = 9.5881
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGGGA':
			curvature_bmht = 0.5234
			curvature_cs = 8.4005
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGGGC':
			curvature_bmht = 2.3246
			curvature_cs = 6.6925
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGGGG':
			curvature_bmht = 3.2828
			curvature_cs = 11.0633
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGGGT':
			curvature_bmht = 2.324
			curvature_cs = 9.8178
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGGTA':
			curvature_bmht = 0.2533
			curvature_cs = 5.9932
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGGTC':
			curvature_bmht = 3.1389
			curvature_cs = 5.6701
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGGTG':
			curvature_bmht = 1.8357
			curvature_cs = 7.7282
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGGTT':
			curvature_bmht = 4.074
			curvature_cs = 6.3012
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGTAA':
			curvature_bmht = 5.2686
			curvature_cs = 10.7196
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGTAC':
			curvature_bmht = 3.7658
			curvature_cs = 11.3928
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGTAG':
			curvature_bmht = 3.4531
			curvature_cs = 8.7404
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGTAT':
			curvature_bmht = 4.0811
			curvature_cs = 10.569
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGTCA':
			curvature_bmht = 8.5035
			curvature_cs = 16.0347
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGTCC':
			curvature_bmht = 6.0904
			curvature_cs = 11.823
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGTCG':
			curvature_bmht = 3.2888
			curvature_cs = 13.2975
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGTCT':
			curvature_bmht = 2.4361
			curvature_cs = 13.8055
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGTGA':
			curvature_bmht = 7.0578
			curvature_cs = 14.9373
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGTGC':
			curvature_bmht = 4.9502
			curvature_cs = 11.9588
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGTGG':
			curvature_bmht = 3.5939
			curvature_cs = 12.439
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGTGT':
			curvature_bmht = 2.9288
			curvature_cs = 8.9219
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGTTA':
			curvature_bmht = 10.5629
			curvature_cs = 9.6117
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGTTC':
			curvature_bmht = 10.6292
			curvature_cs = 11.0841
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGTTG':
			curvature_bmht = 14.4399
			curvature_cs = 8.2662
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TGTTT':
			curvature_bmht = 14.4399
			curvature_cs = 8.2662
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTAAA':
			curvature_bmht = 10.3738
			curvature_cs = 9.971
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTAAC':
			curvature_bmht = 9.0546
			curvature_cs = 10.6236
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTAAG':
			curvature_bmht = 6.0346
			curvature_cs = 7.9834
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTAAT':
			curvature_bmht = 9.4337
			curvature_cs = 9.8102
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTACA':
			curvature_bmht = 5.9129
			curvature_cs = 9.963
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTACC':
			curvature_bmht = 8.3385
			curvature_cs = 8.9375
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTACG':
			curvature_bmht = 8.0122
			curvature_cs = 10.4152
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTACT':
			curvature_bmht = 8.2865
			curvature_cs = 10.9331
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTAGA':
			curvature_bmht = 9.5074
			curvature_cs = 8.4579
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTAGC':
			curvature_bmht = 7.082
			curvature_cs = 10.7346
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTAGG':
			curvature_bmht = 9.2532
			curvature_cs = 5.4113
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTAGT':
			curvature_bmht = 8.5718
			curvature_cs = 6.519
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTATA':
			curvature_bmht = 7.4204
			curvature_cs = 12.6185
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTATC':
			curvature_bmht = 6.1243
			curvature_cs = 14.1426
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTATG':
			curvature_bmht = 5.8223
			curvature_cs = 10.7272
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTATT':
			curvature_bmht = 10.4005
			curvature_cs = 11.2338
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTCAA':
			curvature_bmht = 12.113
			curvature_cs = 18.569
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTCAC':
			curvature_bmht = 10.0493
			curvature_cs = 19.4886
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTCAG':
			curvature_bmht = 5.823
			curvature_cs = 16.7239
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTCAT':
			curvature_bmht = 10.6389
			curvature_cs = 18.5348
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTCCA':
			curvature_bmht = 9.3463
			curvature_cs = 7.865
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTCCC':
			curvature_bmht = 9.3464
			curvature_cs = 7.865
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTCCG':
			curvature_bmht = 7.8827
			curvature_cs = 9.3289
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTCCT':
			curvature_bmht = 7.7743
			curvature_cs = 9.959
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTCGA':
			curvature_bmht = 6.8381
			curvature_cs = 14.6775
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTCGC':
			curvature_bmht = 4.9078
			curvature_cs = 16.5096
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTCGG':
			curvature_bmht = 3.8391
			curvature_cs = 12.3004
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTCGT':
			curvature_bmht = 4.1575
			curvature_cs = 13.0554
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTCTA':
			curvature_bmht = 4.6051
			curvature_cs = 12.5386
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTCTC':
			curvature_bmht = 1.7013
			curvature_cs = 13.7163
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTCTG':
			curvature_bmht = 7.4428
			curvature_cs = 12.8352
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTCTT':
			curvature_bmht = 5.4212
			curvature_cs = 11.3988
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTGAA':
			curvature_bmht = 18.3311
			curvature_cs = 14.7658
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTGAC':
			curvature_bmht = 19.5915
			curvature_cs = 15.8084
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTGAG':
			curvature_bmht = 19.2222
			curvature_cs = 13.0142
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTGAT':
			curvature_bmht = 19.3413
			curvature_cs = 14.7874
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTGCA':
			curvature_bmht = 14.859
			curvature_cs = 16.2912
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTGCC':
			curvature_bmht = 17.2625
			curvature_cs = 15.3577
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTGCG':
			curvature_bmht = 15.823
			curvature_cs = 16.8508
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTGCT':
			curvature_bmht = 15.6251
			curvature_cs = 16.9519
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTGGA':
			curvature_bmht = 14.5439
			curvature_cs = 9.1559
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTGGC':
			curvature_bmht = 12.6345
			curvature_cs = 11.0963
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTGGG':
			curvature_bmht = 11.1003
			curvature_cs = 6.7996
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTGGT':
			curvature_bmht = 11.7614
			curvature_cs = 7.5074
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTGTA':
			curvature_bmht = 13.822
			curvature_cs = 12.2974
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTGTC':
			curvature_bmht = 12.0689
			curvature_cs = 13.882
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTGTG':
			curvature_bmht = 12.2247
			curvature_cs = 10.2268
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTGTT':
			curvature_bmht = 16.3437
			curvature_cs = 10.8826
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTTAA':
			curvature_bmht = 12.7864
			curvature_cs = 9.9589
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTTAC':
			curvature_bmht = 14.1723
			curvature_cs = 11.0099
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTTAG':
			curvature_bmht = 14.3703
			curvature_cs = 8.2133
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTTAT':
			curvature_bmht = 13.869
			curvature_cs = 9.9788
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTTCA':
			curvature_bmht = 10.6171
			curvature_cs = 15.9973
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTTCC':
			curvature_bmht = 12.4751
			curvature_cs = 11.3648
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTTCG':
			curvature_bmht = 10.8406
			curvature_cs = 12.8542
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTTCT':
			curvature_bmht = 10.6145
			curvature_cs = 12.9121
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTTGA':
			curvature_bmht = 22.5266
			curvature_cs = 11.623
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTTGC':
			curvature_bmht = 20.8945
			curvature_cs = 13.8859
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTTGG':
			curvature_bmht = 18.8219
			curvature_cs = 8.5441
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTTGT':
			curvature_bmht = 19.6943
			curvature_cs = 9.6821
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTTTA':
			curvature_bmht = 19.7473
			curvature_cs = 9.4901
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTTTC':
			curvature_bmht = 18.2809
			curvature_cs = 11.1389
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTTTG':
			curvature_bmht = 22.5831
			curvature_cs = 8.0576
			list_curvature_bmht.append(curvature_bmht)
			list_curvature_cs.append(curvature_cs)

		if item.upper()[pos:pos+5] == 'TTTTT':
			curvature_bmht = 22.5831
			curvature_cs = 8.0576
			list_curvature_bmht.append(curvature_bmht)			
			list_curvature_cs.append(curvature_cs)



for item in list_curvature_bmht:
	out.write(str(item) + "\n")

for item in list_curvature_cs:
	out2.write(str(item) + "\n")


