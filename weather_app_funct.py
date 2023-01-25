def weather_to_emoji():
    weather = input('How is the weather?> ').lower()
    if weather == 'rain':
        return ('You need an ☂')
    elif weather == 'cloudy':
        return ('It might rain, see the ☁')
    elif weather == 'sunny':
        return ('Make sure you drink lots of water because of the sun☀')
    elif weather == 'thunderstorm':
        return ('stay at home see the lighten🌩')
    else:
        return ('I rest my case l😎l')
        
#print(weather_to_emoji())
