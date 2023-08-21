


class MyList:

	def __init__(self,lst):
		l = []
		for i in lst:
			if isinstance(i,int):
				l.append(i)

		self.lst = l

	def show(self):
		return self.lst

	def append(self,num):
		if isinstance(num,int):
			self.lst.append(num)
		else:
			print ('Invalid argument "',num,'"')




m1 = MyList([1,2,3,'a'])
res = m1.show()
print(res)
print('**********************')

m1.append('e')
res = m1.show()
print(res)
print('**********************')




x = [1,2,2]

print(max(x))
