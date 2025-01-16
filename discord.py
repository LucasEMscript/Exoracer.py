import discord
import os
from discord.ext import commands
import requests
from io import BytesIO
from PIL import Image

# Get the Discord Token from environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Function to process the uploaded image
async def process_image(image_url):
    # Download the image
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    # Here you would add your ExoRacer scripting logic, 
    # such as analyzing the image or generating code based on it.
    img.show()  # Display the image (for example purposes)
    return "Processed Image"

# Command to upload image with prompt
@bot.command()
async def upload(ctx, prompt: str):
    if len(ctx.message.attachments) > 0:
        image_url = ctx.message.attachments[0].url
        await ctx.send(f"Received prompt: {prompt}")
        result = await process_image(image_url)
        await ctx.send(f"Result: {result}")
    else:
        await ctx.send("Please upload an image along with the prompt.")

# Run the bot with your token from GitHub Secrets
bot.run(DISCORD_TOKEN)