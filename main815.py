from audio import weather
from flower import flower
from text import idcard
# weather.weather_analyse("auto_ip")
path = r"C:\Users\15845\Pictures\Camera Roll\1.jpg"
print(idcard.IDCardRecognizer(api_key='xXDugOa8S6GpMHfPK4OrXotZ',
                                     secret_key='yzZps0FwcYVuigpB6SVz8mI6Q0DwZIhs').detect(path))
