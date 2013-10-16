def pluralize(word): # pass a word in into the fnction
	
	""" This is a way to create a "Docstring" inside your funtion 
		to talk about your funciton specs 
		as well as to giv documention for someone to read 
		your code...
	"""


	if word[-1] =='y': #check the last letter for y
		return word[0:-1] + "ies"
	elif word[-1] == 's' or word[-1] == 'o':
		return word + "es"
	else:
		return word + "s"

print pluralize('clock')
print pluralize('Kehontas')
print pluralize('pony')

#Think about abstraction, think about what the function does, not how 
#What are the functions specs?
#When shoud you call this function (precondition)
#What return values are valid?
#How is the world different? (postcondition)
