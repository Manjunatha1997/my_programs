

RH = ["RH"]
SS = ["2SSA","1SSA","2SSP"]
BC = ["3BCP","5BCA","5BCP"]
Felt = ["2FP","1FA","2FA"]
Clip = ["1CP","2CP","3CP","4CP","5CP","5CA"]

	

lst = []
lst1 = []

for rh in RH:
	for ss in SS:
		for bc in BC:
			for felt in Felt:
				for clip in Clip:
						print(rh+'_'+bc+'_'+felt+'_'+clip+'_'+ss)
						# lst1.append(rh+'_'+bc+'_'+felt+'_'+clip+'_'+ss)

# print(len(lst))

