import random
when = ['A few years ago ', 'Yesterday', 'Last night']
who = ['a rabbit', 'an elephant', 'a mouse']
name = ['balu', 'subha', 'Muthu']
residence = ['India', 'Barchelona', 'germany']
went =['cinema', 'university', 'seminar']
happened =['made a lot of friends', 'Eats a burger', 'Found a secret key']
print(random.choice(when)+ ', ' + random.choice(who) + 'that lived in ' + random.choice(residence) +  ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))