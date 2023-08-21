

x = 'abcd'
y = 'dacb'
print('*******************************')
print('Before swaping: x=',x,'y= ',y)
print('*******************************')
swap_count = 0

for i in range(len(x)):
	if x[i] != y[i]:
		swap_count += 1

		n = y.find(x[i])
		temp1,temp2 = y[i],y[n]

		y = list(y)
		y[i],y[n] = temp2,temp1

		y = ''.join(y)
		print('swaping number:',swap_count,y)

print('*****************************')
print('After swaping: x=',x,'y= ',y)
print('*****************************')


print('Total swap count =',swap_count)
print('*****************************')














