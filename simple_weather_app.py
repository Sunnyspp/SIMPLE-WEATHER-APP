# BOOLEAN True or False
# simple Weather App
weather = input('How is the weather? ').lower()
if weather == 'rain':
    print('☂')
elif weather == 'cloudy':
    print('☁')
elif weather == 'sunny':
    print('☀')
elif weather == 'thunderstorm':
    print('🌩')
else:
    print('😎')
