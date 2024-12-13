 # Weather_app_using_flask 🌦️🌙
Weather_app_using_flask


Welcome to the Weather App, where you can check the current weather and its hourly forecast, explore moon phases, and even view images related to your city!

This app integrates with OpenWeather API to provide accurate and live weather updates, and the Pexels API to show beautiful images related to your location.

## Features 🌟
- **Current Weather Information**: View live data about the temperature, weather description, and more!
- **Hourly Temperature Forecast**: See how the temperature changes throughout the day in an easy-to-read chart.
- **Moon Phases**: Get to know which phase the moon is in and explore its significance.
- **City Images**: Enjoy beautiful images sourced from Pexels related to the city you're checking the weather for.
- **Map**: View your city on an interactive map with OpenStreetMap integration.

## Technologies Used ⚙️
- **Python (Flask)**: The backend of the app is built with Flask, a lightweight web framework for Python.
- **OpenWeather API**: Provides live weather data and forecasts.
- **Pexels API**: Fetches beautiful images of your selected city.
- **JavaScript & Chart.js**: To display hourly weather data on a dynamic line chart.
- **HTML/CSS**: To make the interface clean and responsive.

## Installation 🛠️
To run this project locally, you’ll need to follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

### 2. Set Up Environment Variables
Create a `.env` file in the root directory and add your personal API keys:

```env
FLASK_SECRET_KEY=your_flask_secret_key
OPENWEATHER_API_KEY=your_openweather_api_key
PEXELS_API_KEY=your_pexels_api_key
```
### 3. Install Dependencies
Install the necessary Python dependencies by running:

```bash
pip install -r requirements.txt
```

### 4. Run the App
Start the Flask development server by running the following command:

```bash
python app.py
```

Once the server starts, open http://127.0.0.1:5000/ in your web browser to access the Weather App!



Screenshots 📸
Below are some screenshots of the app:

Example of the weather data and moon phase on the home page.

The moon phases page explaining the different moon phases.


Contributing 🤝
Welcome contributions to this project! To contribute:

-Fork the repository.
-Clone your forked repository to your local machine.
-Create a new branch for your feature or bug fix.
-Make changes and commit them.
-Push your changes to your forked repository.
-Open a pull request.
