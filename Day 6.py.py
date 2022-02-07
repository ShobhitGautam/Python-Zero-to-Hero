# Day 6 Assignment 

def decorators(fun):
	def deno(nbr1, nbr2):
		if nbr1 < nbr2 :
			nbr1, nbr2 = nbr2, nbr1
		return fun(nbr1, nbr2)
	return deno
	
@decorators
def div(nbr1, nbr2):
	return  nbr1 // nbr2

nbr1 =int(input("Enter the nbr: "))
nbr2 =int(input("Enter the nbr: "))
print(nbr1,nbr2)


print(div(nbr1, nbr2))
