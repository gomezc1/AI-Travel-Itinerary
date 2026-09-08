from js import document
from pyodide.http import pyfetch
import json
 
async def generate_itinerary(event):
  origin = document.getElementById("origin").value
  destination = document.getElementById("destination").value
  duration = document.getElementById("duration").value
  """ Generate travel itinerary between 2 places using AI """
  print(f"\n\nGenerating itinerary from {origin} to {destination}..\n")
  prompt = f"Generate a travel itinerary from {origin} to {destination} in {duration} days. This is a road trip, keep it short, less than 15 lines, add some emojis (not more than 5) to make it readable. Add an estimated price of each day in US dollars."


  context = "You a travel specialist and know the best tourist spots around the world"
  api_key = ""
  api_url = f""

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
    if isinstance(value, list):
        
        html_content += f"<li><strong>{key.title()}:</strong><ul>"
        
        for item in value:
            
            html_content += f"<li>{item}</li>"
        
      
        html_content += "</ul></li>"
    else:
       
        html_content += f"<li><strong>{key.title()}:</strong> {value}</li>"

  html_content += "</ul>"

  document.getElementById("result_output").innerHTML = html_content 
