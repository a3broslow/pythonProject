def main():
    words = ['woodstock', 'Gary', 'Tucker', 'Gopher', 'Spike', 'Ed',
    'Faline', 'Willy', 'Rex', 'Rhino', 'Roo', 'Littlefoot',
    'Bagheera', 'Remy', 'Pongo', 'Kaa', 'Rudolph', 'Banzai',
    'Courage', 'Nemo', 'Nala', 'Alvin', 'Sebastiaan', 'Iago']
    three_letter_words = [w for w in words if len(w) == 3]
    print(three_letter_words)

main()
