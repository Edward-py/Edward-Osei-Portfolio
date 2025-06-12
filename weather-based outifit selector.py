 #define function
def get_outfit_suggestion(temperature, weather_condition, wind_speed, custom_outfit):
    if temperature < 10:
        outfit = "Coat, scarf, and gloves"
    elif 10 <= temperature <= 20:
        outfit = "Light jacket and jeans"
    else:
        outfit = ("T-shirt and shorts")

    if weather_condition == "rainy":
        outfit += ", Raincoat and waterproof boots"
    elif weather_condition == "windy":
        outfit += ", Windbreaker and long pants"
    
    if wind_speed > 30:
        outfit += ", extra layers due to high wind"

    if custom_outfit:
        outfit += f", {custom_outfit}"

    return outfit

#Main
while True:
    # List to store outfit suggestions for each day 
    outfit_suggestions = []

    # the number of days to suggest outfits
    days = int(input("For how many days would you like outfit suggestions? "))

    # Looping through each day to get inputs and suggest outfits
    for day in range(1, days + 1):
        print(f"\nDay {day}:")
        #variables
        temperature = int(input("Enter the temperature (°C): "))
        weather_condition = input("Enter the weather condition (sunny, rainy, windy): ")
        wind_speed = int(input("Enter the wind speed (km/h): "))
        custom_outfit = input("Enter any custom outfit preferences (optional): ")
        
        # Getting the outfit suggestion for the day
        suggestion = get_outfit_suggestion(temperature, weather_condition, wind_speed, custom_outfit)
        
        # Adding the suggestion to the list
        outfit_suggestions.append(suggestion)

    # Displaying all outfit suggestions
    print("\nOutfit suggestions:")
    for suggestion in outfit_suggestions:
      print(suggestion)


