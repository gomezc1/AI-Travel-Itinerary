import requests
from rich import print
from rich.markdown import Markdown

def display_current_weather(location):
  """ Get the real time temperature and condition in a location """
  api_key = "133dfa996a9f3f03de4ad12bobb44eat"
  api_url = f"https://api.shecodes.io/weather/v1/current?query={location}&key={api_key}&units=metric"

  response = requests.get(api_url)
  response_data = response.json()

  temperature = round(response_data['temperature']['current'])
  condition = response_data['condition']['description']

  print(f"The current temperature in [bold]{location}[/bold] is [bold]{temperature}°C[/bold], {condition}.\n")

def generate_itinerary(origin, destination, duration):
  """ Generate travel itinerary between 2 places using AI """
  print(f"\n\nGenerating itinerary from {origin} to {destination}..\n")
  prompt = f"Generate a travel itinerary from {origin} to {destination} in {duration} days. This is a road trip, keep it short, less than 15 lines, add some emojis (not more than 5) to make it readable. Add an estimated price of each day in US dollars."


  context = "You a travel specialist and know the best tourist spots around the world"
  api_key = "133dfa996a9f3f03de4ad12bobb44eat"
  api_url = f"https://api.shecodes.io/ai/v1/generate?prompt={prompt}&context={context}&key={api_key}"

  response = requests.get(api_url)
  response_data = response.json()
  itinerary = Markdown(response_data['answer'])

  print(itinerary)


def welcome():
  """ Welcome message """
  print("[bold yellow]Welcome to my AI Travel Itinerary Planner[/bold yellow]")


def credit():
  """ Credit message """
  print("[yellow]The AI Travel Itinerary Planner was built by [bold]Crystal Gomez[/bold], thank you for using it 💖[/yellow]")


welcome()

# User inputs
origin = input("What city does your trip start from? ")
destination = input("What city is your trip going to? ")
duration = input("How many days will your trip last? (enter a number only, i.e 5) ")

if origin and destination and duration.isdigit():
  display_current_weather(origin)
  display_current_weather(destination)
  generate_itinerary(origin, destination, duration)
  credit()
else:
  print("Please try again. Make sure you enter valid information")
