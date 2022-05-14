#librarys

import time

#while

while True:

#main-menu options

    time.sleep(1)
    print ('========================================== \nBem Vindo ao Conversor de Temperaturas \n1. Converter Celsius para Fahrenheit \n2. Converter Celsius para Kelvin \n3. Converter Fahrenheit para Celsius \n4. Converter Fahrenheit para Kelvin \n5. Converter Kelvin para Celsius \n6. Converter Kelvin para Fahrenheit \n7. Fechar Programa \n==========================================')
    time.sleep(1)
    resposta = input('Qual você deseja? ')
    if resposta == '1':
        cel_fahr = int(input('Digite a temperatura em Celsius: '))
        f_c = (cel_fahr * 9/5) + 32
        time.sleep(1)
        print('A conversão de {}°C para Fahrenheit é {}F°'.format(cel_fahr, f_c))
    elif resposta == '2':
        time.sleep(1)
        cel_kel = int(input('Digite a temperatura em Celsius: '))
        k_c = cel_kel + 273
        time.sleep(1)
        print('A conversão de {}°C para Kelvin é {}K'.format(cel_kel, k_c))

    elif resposta == '3':
        time.sleep(1)
        fahr_cel = int(input('Digite a temperatura em Fahrenheits: '))
        c_f = (fahr_cel - 32) * 5/9
        time.sleep(1)
        print('A conversão de {}°F para Celsius é {:.3}°C'.format(fahr_cel, c_f))

    elif resposta == '4':
        fahr_kel = int(input('Digite a temperatura em Fahrenheits: '))
        k_f = (fahr_kel - 32) * 5/9 + 273
        time.sleep(1)
        print('A conversão de {}°F para Kelvin é {:.4}°K'.format(fahr_kel, k_f))

    elif resposta == '5':
        kel_cel = int(input('Digite a temperatura em Kelvin: '))
        k_c = kel_cel - 273 
        time.sleep(1)
        print('A conversão de {}K para Kelvin é {}°C'.format(kel_cel, k_c))

    elif resposta == '6':
        kel_fahr = int(input('Digite a temperatura em Kelvin: '))
        k_f = (kel_fahr - 273) * 9/5 + 32
        time.sleep(1)
        print('A conversão de {}K para Kelvin é {:.4}°F'.format(kel_fahr, k_f))

    elif resposta == '7':
        time.sleep(0.5)
        print('Saindo...')
        time.sleep(1)
        break
    else:
        time.sleep(1)
        print('ERRO! Digite uma opção válida. ')
