
# Weather Application

## Functionality
The script performs the following tasks:

1. Imports necessary libraries: `requests`, `json`, `time`, `datetime`, `os`, and `pyfiglet`.
2. Defines a `city_info()` function that takes a city name as input and returns the latitude and longitude coordinates of the city using the OpenWeatherMap API.
3. Implements a `main()` function that:
   - Displays an ASCII art banner using the `pyfiglet` library.
   - Prompts the user to enter a city name (or 'q' to quit).
   - Retrieves the latitude and longitude coordinates of the city using the `city_info()` function.
   - Fetches the weather data for the given city using the OpenWeatherMap API.
   - Saves the weather data to a `weather.json` file.
   - Displays the weather information, including weather condition, temperature, humidity, wind speed, and cloud coverage.
   - Allows the user to continue or exit the application.

## Installation
To use this script, you'll need to have the following dependencies installed:

- Python 3.x
- The following Python libraries:
  - `requests`
  - `json`
  - `time`
  - `datetime`
  - `os`
  - `pyfiglet`

You can install these dependencies using `pip`:

```
pip install requests json time datetime os pyfiglet
```

Additionally, you'll need to obtain an API key from OpenWeatherMap. You can sign up for a free account and get an API key at [https://openweathermap.org/](https://openweathermap.org/). Once you have the API key, replace the `KEY` variable in the script with your own key.

## Usage
To run the script, simply execute the Python file:

```
python weather_app.py
```

The script will display the ASCII art banner and prompt the user to enter a city name. After entering the city name, the script will fetch the weather data and display the relevant information.

The user can continue to enter new city names or quit the application by typing 'q'.

## Dependencies
The script relies on the following external libraries:

- `requests`: Used for making HTTP requests to the OpenWeatherMap API.
- `json`: Used for handling JSON data.
- `time`: Used for adding delays and pauses in the script.
- `datetime`: Not used in the provided code, but could be used for handling date and time-related operations.
- `os`: Used for clearing the console screen.
- `pyfiglet`: Used for generating ASCII art banners.

## Example Usage
Here's an example of how the script can be used:

```
$ python weather.py

__        __         _   _                       _   ___
\ \      / /__  __ _| |_| |__   ___ _ __  __   _/ | / _ \
 \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__| \ \ / / || | | |
  \ V  V /  __/ (_| | |_| | | |  __/ |     \ V /| || |_| |
   \_/\_/ \___|\__,_|\__|_| |_|\___|_|      \_/ |_(_)___/

------------------------------------------------------------
Enter the city name (q to quit): London

------------------------------------------------------------
- Weather: Clouds (overcast clouds)
- Temperature: 10.12°C           - Humidity: 76%
- Wind Speed: 5.14 m/s
- Clouds: 100%

------------------------------------------------------------
Do you want to continue? (y/n): n
Goodbye!
```

In this example, the user enters "London" as the city name, and the script retrieves and displays the weather information for London.
