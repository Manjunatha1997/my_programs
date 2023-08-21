


lst = [10,20,30,40,50,60,70,80,90]

n = 8


def split_list(lst,n):

	out = []
	n1 = n
	c = 0
	if len(lst) %2 == 0:
		for i in range(len(lst)//n):
			x = lst[c:n]
			out.append(x)
			c = n
			n += n1
	else:
		for i in range((len(lst)//n)+1):
			x = lst[c:n]
			
			out.append(x)
			c = n
			n += n1

			if not out[-1]:
				del out[-1]


	# print(out)
	return out
		

res = split_list(lst,n)
print(res)

