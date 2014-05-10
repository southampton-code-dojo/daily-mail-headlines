import random

blame = [ 'Chavs', 'Lib Dems', 'Gays', 'Homosexuals', 'Kate Middleton', 'Romanians', 'Immigrants', 'Poles', 'Labour', 'Bankers', 'Somalians', 'Bulgarians', 'The French', 'Lord Alan Sugar', 'Single mothers', 'Benefit frauds', 'Gypsies', 'The Green Party', 'The BBC', 'Rupert Murdock', 'Drone Attacks', 'Terrorists', 'Max Clifford', 'Katie Price', 'The Poor', 'The Taliban', 'Al Qaeda', 'Cyclists' ]
verbs = [ 'Destroys', 'Devalues', 'Crushes', 'Damages', 'Ends', 'Eradicates', 'Wipes Out', 'Defiles', 'Debases', 'Desecrates', 'Smears', 'Abuses', ' Tarnishes' ]
values = [ 'The NHS', 'Your Taxes', 'Your Home', 'The Freedom of the Press', 'The Queen', 'The British Way of Life', 'Your Pensions', 'Your Children', 'Traditional Family Values', 'The Hard-Working Public', 'The Working Classes', 'The War on Terror' ]
threats = [ 'Cancer', 'War', 'Poverty', 'Loss of Patriotism', 'Loss of Patriotism', 'Multiculteralism', 'Crime', 'Lower Wages', 'Higher Taxes', 'Diabetes', 'Bird-Flu', 'AIDS', 'Heart Attacks' ] 

def c(wordList):
	return random.choice(wordList)

n = random.randrange(5)



if n == 0:
	w = c(blame) +' ' +c(verbs) +' ' +c(values)
elif n == 1:
	w = c(blame) +' causes ' +c(threats)
elif n == 2:
	w = 'Could ' +c(blame) +' Cause ' +c(threats) +'?'
elif n == 3:
	w = c(threats) +'! Are ' +c(blame) +' Responsible?'
elif n == 4:
	w = 'Stop ' +c(blame) + ' For The Sake Of ' +c(values)

print w

f1 = open('template', 'r')
f2 = open('headline.html', 'w')
for line in f1:
	f2.write(line.replace('HEADLINE', w))
f1.close()
f2.close()
