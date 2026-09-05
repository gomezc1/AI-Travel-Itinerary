#import requests
#from rich import print
#from rich.markdown import Markdown
#from pyscript import Element, display
from js import document
from pyodide.http import pyfetch
import json
#import markdown 


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

    #result_text = response_data.get('response', str(response_data)) 
   # document.getElementById("result_output").innerHTML = f"<pre>{result_text}</pre>"
        
  #except Exception as e:
    #document.getElementById("result_output").innerHTML = f"Error: {str(e)}"

  keys_to_hide = {'prompt', 'context'}

  clean_data =  {
    key: value
    for key, value in response_data.items()
    if key not in keys_to_hide
  }

  html_content = "<h2>Trip Details</h2><ul>"

  for key, value in clean_data.items():
    if isinstance(value, list):
        # Start nested list for sub-items
        html_content += f"<li><strong>{key.title()}:</strong><ul>"
        
        for item in value:
            # Add each sub-item as a nested <li>
            html_content += f"<li>{item}</li>"
        
        # Close nested list and the main list item
        html_content += "</ul></li>"
    else:
        # Standard single-line item
        html_content += f"<li><strong>{key.title()}:</strong> {value}</li>"

  html_content += "</ul>"

  document.getElementById("result_output").innerHTML = html_content   
