print("welcome to the hangman")
word=' p y t h o n'
target=' _ _ t h _ n'
print(target)
p=False
y=False
o=False
c=3
while c>0:
	guess = input('guess the word')
	if guess=='p':
		p=True
		if o and y:
			print(' p y t h o n ')
			print('you won')
			break
		elif o:
			print(' p _ t h o n ')
		elif y:
			print(' p y t h _ n ')
	elif guess=='y':
		y=True
		if o and p:
			print(' p y t h o n ')
			print('you won')
			break
		elif o:
			print(' _ y t h o n ')
		elif p:
			print(' p y t h _ n ')
	elif guess=='o':
		o=True
		if p and y:
			print(' p y t h o n ')
			print('you won')
			break
		elif p:
			print(' p _t h o n ')
		elif y:
			print(' _  y t h _ n ')
	else:
		c=c-1
		print('mauka remaining ',c)
						
