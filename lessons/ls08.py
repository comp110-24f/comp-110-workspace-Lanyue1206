def get_weather_report() -> str:
    """Display weather instrcutions"""
    weather = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        """Use two boolens for each condition"""
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize the weather.")
    return weather


"""No need to use print, which will only tell you the address the fucntion stored at"""
get_weather_report()
