from flask import Flask, render_template, request, jsonify, url_for
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('FLASK_SECRET_KEY')
API_KEY = os.getenv('OPENWEATHER_API_KEY')
PEXELS_API_KEY = os.getenv('PEXELS_API_KEY')

def get_moon_phase():
    current_date = datetime.now().date()
    day = current_date.day
    if day < 7:
        return "New Moon"
    elif 7 <= day < 14:
        return "First Quarter"
    elif 14 <= day < 21:
        return "Full Moon"
    else:
        return "Last Quarter"

def get_background_image(description):
    description = description.lower()
    if "clear" in description:
        return url_for('static', filename='images/sunny.jpg')
    elif "rain" in description:
        return url_for('static', filename='images/rainy.jpg')
    elif "snow" in description:
        return url_for('static', filename='images/snowy.jpg')
    elif "cloud" in description:
        return url_for('static', filename='images/cloudy.jpg')
    elif "storm" in description:
        return url_for('static', filename='images/stormy.jpg')
    elif "mist" in description or "fog" in description:
        return url_for('static', filename='images/mist.jpg')
    else:
        return url_for('static', filename='images/default.jpg')

def get_hourly_temperature_data(city_name):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        hourly_data = [
            {
                "hour": datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S").strftime("%H:%M"),
                "temperature": entry["main"]["temp"]
            }
            for entry in data["list"][:8]
        ]
        return hourly_data
    return []

def get_pexels_image(query):
    url = f'https://api.pexels.com/v1/search?query={query}&per_page=1'
    headers = {
        'Authorization': PEXELS_API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data['photos']:
            return data['photos'][0]['src']['original']
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = {}
    moon_phase = get_moon_phase()
    is_night = False
    current_time = datetime.now().hour

    if current_time >= 18 or current_time < 6:
        is_night = True

    default_bg_url = url_for('static', filename='images/default.jpg')

    if request.method == 'POST':
        city_name = request.form.get('city')
        if city_name:
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                description = data['weather'][0]['description']
                lat = data['coord']['lat']
                lon = data['coord']['lon']
                pexels_image_url = get_pexels_image(city_name)

                hourly_data = get_hourly_temperature_data(city_name)

                hourly_temperatures = [entry['temperature'] for entry in hourly_data]
                hourly_labels = [entry['hour'] for entry in hourly_data]

                bg_url = get_background_image(description)

                weather_data = {
                    'city_name': data['name'],
                    'description': description,
                    'temperature': data['main']['temp'],
                    'feels_like': data['main']['feels_like'],
                    'icon_url': f'http://openweathermap.org/img/wn/{data["weather"][0]["icon"]}.png',
                    'moon_phase': moon_phase,
                    'hourly_temperature_data': hourly_data,
                    'hourly_temperatures': hourly_temperatures,
                    'hourly_labels': hourly_labels,
                    'bg_url': bg_url,
                    'pexels_image_url': pexels_image_url,
                    'lat': lat,
                    'lon': lon,
                    'is_night': is_night,
                }

    return render_template('index.html', weather=weather_data)

@app.route('/about_moon')
def about_moon():
    return render_template('about_moon.html', bg_url=url_for('static', filename='images/moon.jpg'))

@app.route('/get_hourly_data', methods=['POST'])
def get_hourly_data():
    city_name = request.json.get('city_name')
    hourly_data = get_hourly_temperature_data(city_name)
    hourly_temperatures = [entry['temperature'] for entry in hourly_data]
    hourly_labels = [entry['hour'] for entry in hourly_data]
    return jsonify({'hourly_temperatures': hourly_temperatures, 'hourly_labels': hourly_labels})

if __name__ == '__main__':
    app.run(debug=True)
