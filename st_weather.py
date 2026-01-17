import streamlit as st
import os
import requests
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

api_key = os.getenv("API_KEY")

# set the Streamlit page info
st.set_page_config(
    page_title="Weather Info",
    page_icon="🌦️",
    layout="centered",
)

if not api_key:
    st.error("API_KEY not configured. Please set it in your .env file.")
    st.stop()


@st.cache_data(ttl=300)
def get_weather_data(city: str, units: str = 'metric') -> dict | None:
    """Retrieve weather data from OpenWeatherMap API."""
    url = f'https://api.openweathermap.org/data/2.5/weather?q={quote(city)}&appid={api_key}&units={units}'

    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException:
        return None

    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'conditions': data['weather'][0]['description'],
            'icon': f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
        }
    else:
        return None


def format_temperature(units: str) -> str:
    """Format the temperature display unit."""
    return '°C' if units == 'metric' else '°F'


st.title("☀️ Current Weather Info 🌧️")

city = st.text_input("Enter city name:")
units = st.selectbox("Select units:", ['metric', 'imperial'])

if st.button("Get Weather"):
    if not city.strip():
        st.warning("Please enter a city name.")
    else:
        with st.spinner("Fetching weather data..."):
            weather_data = get_weather_data(city, units)

        if weather_data is not None:
            temp_unit = format_temperature(units)
            temperature = round(weather_data['temperature'])
            feels_like = round(weather_data['feels_like'])
            conditions = weather_data['conditions'].title()
            st.markdown(f"#### Current temperature in {city}: {temperature}{temp_unit}")

            st.markdown(
                f"""
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="font-size: 1.3rem; font-weight: bold; margin: 0;">{conditions}</span>
                        <img src="{weather_data['icon']}" width="50" />
                    </div>
                    """,
                    unsafe_allow_html=True
            )

            st.markdown(f"#### Feels like: {feels_like}{temp_unit}")
        else:
            st.error("City not found or network error. Please check the city name and try again.")
