# Weather-forecast
A simple weather forecast app using Python and the OpenWeatherMap API. 
This app takes a city name as input from the user and displays the current weather conditions for that city.
Before running the code, make sure you have signed up for the OpenWeatherMap API and obtained an API key. 
Replace "YOUR_API_KEY" with your actual API key in the code.
This code defines a function get_weather() to fetch weather data for a given city using the OpenWeatherMap API. 
The main() function takes user input for the city name, calls the get_weather() function, and displays the current weather conditions including temperature, weather description, humidity, and wind speed.
More features are:
Error handling for invalid input and network issues.
Displaying additional weather information such as pressure and visibility.
Providing an option for users to see the forecast for the next few days.
Implementing a graphical user interface (GUI) using Tkinter for a user-friendly experience
In this version of the app, I've replaced the command-line interface with a simple Tkinter-based graphical user interface (GUI).
Users can input the city name in a text entry field and click the "Get Weather" button to fetch and display the weather information for that city.
The get_weather() function now includes error handling for network issues and invalid input. If there's an error, it displays an error message box.
I've also added more weather information like pressure and visibility. The show_weather() function fetches the weather data and updates the labels in the GUI accordingly.

To enhance the weather forecast app with icons, styling, historical data, and multiple city forecasts, we can use additional libraries and APIs. 
For icons and styling, we can utilize the ttkthemes library to improve the appearance of the GUI. For historical data and multiple city forecasts, we may need to explore additional weather APIs like Weatherstack or AccuWeather, which provide historical data and forecasts for multiple cities.
GUI Styling: We have used the ttkthemes library to set the GUI theme to "clam", which provides a cleaner and more modern look compared to the default Tkinter theme.
Window Geometry: We have set the window geometry to 400x300 pixels to provide a more compact and aesthetically pleasing layout.



