import streamlit as st
import logging
from modules.api_handler import get_weather, get_weekly_forecast
from modules.ui_components import render_weather_card, set_background, render_forecast_chart
from modules.utils import setup_logging, celsius_to_fahrenheit, celsius_to_kelvin

st.set_page_config(page_title="Weather App", page_icon="assets/weather_icon.png", layout="centered")
set_background()
setup_logging()
logging.info("Weather app started.")

st.image("assets/weather_icon.png", width=150)
st.title("Weather App")

city = st.text_input("Enter city name", "New York")
unit = st.selectbox("Select Temperature Unit", ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"])

if st.button("Get Weather"):
    logging.info(f"Fetching weather for: {city}")
    weather = get_weather(city)

    if weather:
        logging.info(f"Weather data retrieved successfully for {city}")

        if unit == "Fahrenheit (°F)":
            weather["temperature"] = celsius_to_fahrenheit(weather["temperature"])
        elif unit == "Kelvin (K)":
            weather["temperature"] = celsius_to_kelvin(weather["temperature"])

        weather["unit"] = unit
        render_weather_card(weather)

        weekly_forecast = get_weekly_forecast(city)
        if weekly_forecast:
            days = [day['date'] for day in weekly_forecast]
            temps = [day['temperature'] for day in weekly_forecast]

            if unit == "Fahrenheit (°F)":
                temps = [celsius_to_fahrenheit(temp) for temp in temps]
            elif unit == "Kelvin (K)":
                temps = [celsius_to_kelvin(temp) for temp in temps]

            render_forecast_chart(days, temps, unit)
        else:
            logging.error(f"Failed to retrieve weekly forecast for {city}")
            st.error("Unable to fetch weekly forecast. Please try again.")
    else:
        logging.error(f"Failed to retrieve weather data for {city}")
        st.error("City not found or API error. Please try again.")
