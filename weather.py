import pyowm
 
owm = pyowm.OWM('043a1b2fb05cc6148a11dd3ae6a46033')
observation = owm.weather_at_place('Ghana,koforidua')
w = observation.get_weather()
 
w.get_wind()
w.get_humidity()
print(w.get_wind())
print(w.get_humidity())
