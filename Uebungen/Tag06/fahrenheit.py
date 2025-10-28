# Umrechnung Celsius Fahrenheit
# Vom Nutzer Temperatur in Celsius einlesen
# Daraus die Temperatur in Fahrenheit berechnen und ausgeben

print('Was möchtest du tun?')
print('[F]ahrenheit in Celsius')
print('[C]elsius in Fahrenheit')

auswahl = input()

if auswahl == 'C':
    celsius = float(input('Welche Temperatur in Celsius? '))
    fahrenheit = celsius * 9 / 5 + 32
    print(f'{fahrenheit} °F')
else:
    fahrenheit = float(input('Welche Temperatur in Fahrenheit? '))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f'{celsius} °C')
