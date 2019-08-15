from audio import weather
from flower import flower
from text import text81
# weather.weather_analyse("auto_ip")
path = r"C:\Users\15845\Pictures\Untitled Diagram (1).png"
print(text81.detect(path))

result = text81.detect(path)
for i in result:
    for value in i.values ():
        print ( value )