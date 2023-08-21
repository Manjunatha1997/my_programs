

s = 'abbcddaaaaaabfgh'

s1 = ''

count = 1
for i in range(len(s)):
	try:
		if s[i] == s[i+1]:
			count+=1
		else:
			s1 = s1+s[i]+str(count)

			count = 1
	except:
		if s[i] == s[-1]:
			s1 += s[i]+str(count)

print(s1)

