



class Calc:


	def add(self,num1,num2):

		return num1+num2

	def addSo(self,*num):
		return sum(num)


	def prime(self,start,end):
		
		primes = []
		not_primes = []
		for i in range(start,end+1):

			if i == 1:
				not_primes.append(i)

			if i >= 2:

				for j in range(2,i):
					if i%j == 0:
						not_primes.append(i)

						break
				else:
					primes.append(i)

		return primes, not_primes


	def fibbo(self,num):

		first,second = 0, 1

		for i in range(2,num):
			
			temp = first + second
			first = second
			second = temp



		return temp





c1 = Calc()
res = c1.add(2,3)
print(res)

res = c1.prime(1,20)
print(res)

res = c1.addSo(13,2,3,4,5,66)
print(res)
print('************************************')

res = c1.fibbo(9)
print(res)
print('************************************')





