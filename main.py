while True:
    while True:
        eq = input('Apa yang anda mau\n1.Pertambahan\n2.Perkurangan\n3.Perkalian\n4.Pembagian\n')
        try:
            equ = int(eq)
            if equ in [1, 2, 3, 4]:
                break
            else:
                print('Tidak Valid')
        except ValueError :
            print('Tidak Valid')
