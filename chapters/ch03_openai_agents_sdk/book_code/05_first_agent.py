import os
from dotenv import load_dotenv
from openai import OpenAI
from agents import Agent, Runner, function_tool
load_dotenv()

# define a tool for temperature conversion [don’t worry about the syntax specifics right now]
@function_tool
def convert_temperature(value:float)->str:
    """Convert temperature from Fahrenheit to Celsius."""
    celsius = (value - 32) * 5/9
    return f"{value}°F = {celsius}°C"

agent = Agent(name= "Temperature Assistant", instructions = "You help convert temperatures between units.", model= "gpt-5-nano", 
              tools = [convert_temperature])

result = Runner.run_sync(agent, input = "Convert 350°F to Celsius")

print(result.final_output)