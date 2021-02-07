#   from typing import List, Any, Union


def main():
    words = ['woodstock', 'Gary', 'Tucker', 'Gopher', 'Spike', 'Ed',
    'Faline', 'Willy', 'Rex', 'Rhino', 'Roo', 'Littlefoot',
    'Bagheera', 'Remy', 'Pongo', 'Kaa', 'Rudolph', 'Banzai',
    'Courage', 'Nemo', 'Nala', 'Alvin', 'Sebastiaan', 'Iago']
    three_letter_words = [w for w in words if len(w) == 3]
    print(three_letter_words)

main()

def get_inits(name):
#   Create list from first letter of each name part
inits = [name_part[0] for name_part in name.split()]
#   Join inits list on "." and append "." to end
return '.'.join(inits) + '.'

def main():
people = ['George Washington', 'John Adams',
              'Thomas Hefferson', 'John Quincy Adams']

#   Create list by mapping person elements to get_inits()
inits = [get_inits(person) for person in people]
print(inits)

main()
