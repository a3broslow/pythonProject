def get_inits(name):
    inits = [name_part[0] for name_part in name.split()]
    return '.'.join(inits) + '.'

def main():
    people = ['George Washington', 'Anton Pengel', 'Malcolm X', 'Michael A', 'Axel J Foley']
    inits = [get_inits(person) for person in people]
    print(inits)

main()
