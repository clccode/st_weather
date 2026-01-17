## ☀️ Current Weather Info 🌧️

This app checks the temperature in the city you select and also returns:
* The current weather conditions
* The "feels like" (or "real feel") temperature

It's written in Python and uses:
* The Streamlit library for the UI
* The OpenWeather API (https://openweathermap.org)

## Setup

1. Install dependencies:
   ```bash
   pip install streamlit requests python-dotenv
   ```

2. Get an API key from [OpenWeatherMap](https://openweathermap.org/api)

3. Create a `.env` file in the project root:
   ```
   API_KEY=your_openweathermap_api_key
   ```

## Usage

Run the app:
```bash
streamlit run st_weather.py
```

Enter a city name, select your preferred units (metric or imperial), and click "Get Weather" to see current conditions.

See a live version of the app at https://st-weather.streamlit.app/
