#!/usr/bin/env python3
from weather import Weather, LLM
# from visualise import Visualise
import time

WIDTH = 400
HEIGHT = 300
UPDATE_BUFFER = 60
COLOUR = "yellow"
SYSTEM = "assistant" # or "entertainer" or "none"

# visualise = Visualise(WIDTH, HEIGHT)


if __name__ == "__main__":
    run = True
    while run == True:
        # Create dict
        output = {}

        # Get forecast data from Met Office API
        weather = Weather()
        weather_report = weather.generate_report()
        print(weather_report)

        images = weather.weather_to_images()
        print(images)

        grid = weather.create_image_grid(images)
        print(grid)
        
        weather.test_make_cold()
        weather.test_add_grass()
        weather.test_add_new()
        grid = weather.new_full_run_through(weather)
        # print("WEATHER REPORT:", weather_report)

        # # Summarise forecast with ChatGPT
        # LLM = LLM()
        # forecast = LLM.summarise_forecast(weather_report)
        # output["forecast"] = forecast

        # # Default result = forecast
        # stylecast = forecast
        # style_name = "Weather Reporter"

        # if SYSTEM == "assistant":
        #     # Change style of forecast with ChatGPT to advise on what to wear
        #     style_name = "Inky Weather"
        #     output["style"] = "Inky Weather"
        #     stylecast = LLM.advice_style(forecast)
        #     output["stylecast"] = stylecast
        
        # if SYSTEM == "entertainer":
        #     # Change style of forecast reporting with ChatGPT
        #     style = weather.random_style()
        #     style_name, style_desc = style[0], style[1]
        #     output["style"] = style_name
        #     stylecast = LLM.change_style(forecast, style_desc)
        #     output["stylecast"] = stylecast

        # print("SYSTEM:", SYSTEM, "OUTPUT:", output)

        # result = style_name + ": \n" + stylecast

        # Render on e-ink display
        # visualise.draw(stylecast, style_name)
        # visualise.display(COLOUR)

        run = False