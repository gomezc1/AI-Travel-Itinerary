#import requests
#from rich import print
#from rich.markdown import Markdown
#from pyscript import Element, display
from js import document 
from pyodide.http import pyfetch
import markdown 
import sys


def display_current_weather(location):
  """ Get the real time temperature and condition in a location """
  api_key = "133dfa996a9f3f03de4ad12bobb44eat"
  api_url = f"https://api.shecodes.io/weather/v1/current?query={location}&key={api_key}&units=metric"

  response = pyfetch.get(api_url)
  response_data = response.json()

  temperature = round(response_data['temperature']['current'])
  condition = response_data['condition']['description']

  print(f"The current temperature in [bold]{location}[/bold] is [bold]{temperature}°C[/bold], {condition}.\n")

async def generate_itinerary(event):
  origin = document.getElementById("origin").value
  destination = document.getElementById("destination").value
  duration = document.getElementById("duration").value
  """ Generate travel itinerary between 2 places using AI """
  print(f"\n\nGenerating itinerary from {origin} to {destination}..\n")
  prompt = f"Generate a travel itinerary from {origin} to {destination} in {duration} days. This is a road trip, keep it short, less than 15 lines, add some emojis (not more than 5) to make it readable. Add an estimated price of each day in US dollars."


  context = "You a travel specialist and know the best tourist spots around the world"
  api_key = "133dfa996a9f3f03de4ad12bobb44eat"
  api_url = f"https://api.shecodes.io/ai/v1/generate?prompt={prompt}&context={context}&key={api_key}"

  response = await pyfetch(api_url)
  response_data = await response.json()

  keys_to_hide = {'prompt', 'context'}

  clean_data =  {
    key: value
    for key, value in response_data.items()
    if key not in keys_to_hide
  }


  html_content = "<h2>Trip Details</h2><ul>"

  for key, value in clean_data.items():
    if isinstance(value,list):
      
      items = "<br>".join(str(v) for v in value)
      html_content += f"<li><b>{key.title()}:</b><br><br>{items}</li>"
    else:
      html_content += f"<li><b>{key.title()}:</b> {value}</li>"

  html_content += "</ul>"


  #itinerary = markdown.markdown(str(response_data))

  #print(itinerary)
  document.getElementById("result_output").innerHTML = html_content



def welcome():
  """ Welcome message """
  print("[bold yellow]Welcome to my AI Travel Itinerary Planner[/bold yellow]")


def credit():
  """ Credit message """
  print("[yellow]The AI Travel Itinerary Planner was built by [bold]Crystal Gomez[/bold], thank you for using it 💖[/yellow]")


welcome()

# User inputs
origin = document.getElementById("origin").value
destination = document.getElementById("destination").value
duration = document.getElementById("duration").value

if origin and destination and duration.isdigit():
  display_current_weather(origin)
  display_current_weather(destination)
  generate_itinerary(origin, destination, duration)
  credit()
else:
  print("Please try again. Make sure you enter valid information")
