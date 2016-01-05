# coding: utf-8
def write_weather_report(degrees, cloudiness):
    if degrees < 20:
        print("It's cold today, only %s° and %s" % (degrees, cloudiness))
    elif cloudiness == "sunny":
        print("What a weather! %s° plus a brilliant sunshine!" % degrees)
    else:
        print("It's %s° and %s" % (degrees, cloudiness))

write_weather_report(20, "cloudy")
write_weather_report(15, "partly cloudy")
write_weather_report(27, "sunny")
write_weather_report(12, "sunny")
