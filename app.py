from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

weather_data = {}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', weather_data=weather_data)

@app.route('/get_weather', methods=['POST'])
def get_weather():
    location = request.form['location']
    
    if location:
        api_key = '0d85b95ac61d4d4bb379f63800f5b3c6'
        base_url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': location, 'appid': api_key}

        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_info = {
                'location': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
            weather_data.clear()
            weather_data.update(weather_info)

    return redirect(url_for('index'))

@app.route('/update_weather/<location>', methods=['POST'])
def update_weather(location):
    if location:
        api_key = '0d85b95ac61d4d4bb379f63800f5b3c6'
        base_url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': location, 'appid': api_key}

        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_info = {
                'location': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
            weather_data.clear()
            weather_data.update(weather_info)

    return redirect(url_for('index'))

@app.route('/delete_weather', methods=['POST'])
def delete_weather():
    weather_data.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)