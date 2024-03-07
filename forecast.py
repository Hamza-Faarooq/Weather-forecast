import requests
import tkinter as tk
from tkinter import ttk, messagebox

# Function to fetch weather data from the OpenWeatherMap API
def get_weather(city_name, api_key):
    try:
        # Construct the API URL with the city name and API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        # Send a GET request to the API
        response = requests.get(url)
        # Convert the response to JSON format
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        # Display an error message if there's a network issue
        messagebox.showerror("Error", f"Failed to fetch data: {e}")
        return None

# Function to display weather data in the GUI
def show_weather():
    # Get the city name from the entry field
    city_name = city_entry.get()
    # Fetch weather data for the specified city
    weather_data = get_weather(city_name, api_key)

    if weather_data:
        if weather_data["cod"] == 200:
            # Update the labels with weather information
            result_label.config(text=f"Weather in {city_name}:")
            temp_label.config(text=f"Temperature: {weather_data['main']['temp']}°C")
            weather_label.config(text=f"Weather: {weather_data['weather'][0]['description']}")
            humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
            wind_label.config(text=f"Wind Speed: {weather_data['wind']['speed']} m/s")
            pressure_label.config(text=f"Pressure: {weather_data['main']['pressure']} hPa")
            visibility_label.config(text=f"Visibility: {weather_data['visibility']} meters")
        else:
            # Display an error message if the city name is invalid
            messagebox.showerror("Error", "City not found. Please enter a valid city name.")

# Main function to create the GUI
def main():
    global city_entry, result_label, temp_label, weather_label, humidity_label, wind_label, pressure_label, visibility_label

    # Create the main window
    window = tk.Tk()
    window.title("Weather Forecast App")
    window.geometry("400x300")  # Set the window size

    # Set the GUI theme
    style = ttk.Style(window)
    style.theme_use("clam")

    # Create and place GUI elements
    tk.Label(window, text="Enter city name:").pack(pady=5)
    city_entry = tk.Entry(window)
    city_entry.pack(pady=5)
    ttk.Button(window, text="Get Weather", command=show_weather).pack(pady=5)

    # Initialize labels to display weather information
    result_label = tk.Label(window, text="")
    result_label.pack(pady=5)

    temp_label = tk.Label(window, text="")
    temp_label.pack(pady=5)

    weather_label = tk.Label(window, text="")
    weather_label.pack(pady=5)

    humidity_label = tk.Label(window, text="")
    humidity_label.pack(pady=5)

    wind_label = tk.Label(window, text="")
    wind_label.pack(pady=5)

    pressure_label = tk.Label(window, text="")
    pressure_label.pack(pady=5)

    visibility_label = tk.Label(window, text="")
    visibility_label.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    # Replace "YOUR_API_KEY" with your OpenWeatherMap API key
    api_key = "YOUR_API_KEY"
    main()
