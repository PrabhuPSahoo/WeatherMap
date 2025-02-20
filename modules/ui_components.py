import streamlit as st
import base64
import matplotlib.pyplot as plt

def render_weather_card(weather):
    unit_symbol = "°C"
    if weather["unit"] == "Fahrenheit (°F)":
        unit_symbol = "°F"
    elif weather["unit"] == "Kelvin (K)":
        unit_symbol = "K"

    st.markdown(f"""
        <div style='background: white; padding: 20px; border-radius: 10px; 
                    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); text-align: center;'>
            <h2>{weather['city']}</h2>
            <img src='{weather['icon']}' width='80'>
            <h3>{weather['condition']}</h3>
            <p><strong>Temperature:</strong> {weather['temperature']:.2f}{unit_symbol}</p>
            <p><strong>Humidity:</strong> {weather['humidity']}%</p>
            <p><strong>Wind Speed:</strong> {weather['wind_speed']} m/s</p>
            <small>Last Updated: {weather['time']}</small>
        </div>
    """, unsafe_allow_html=True)


def render_forecast_chart(days, temps, unit):
    if unit == "Fahrenheit (°F)":
        ylabel = "Temperature (°F)"
    elif unit == "Kelvin (K)":
        ylabel = "Temperature (K)"
    else:
        ylabel = "Temperature (°C)"

    fig, ax = plt.subplots(figsize=(8, 5), facecolor='none')
    ax.plot(days, temps, marker='o', linestyle='-', color='b')
    ax.set_xlabel("Date")
    ax.set_ylabel(ylabel)
    ax.set_title("7-Day Forecast")
    plt.xticks(rotation=45)
    
    st.pyplot(fig)


def set_background(image_path="assets/img.jpg"):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
