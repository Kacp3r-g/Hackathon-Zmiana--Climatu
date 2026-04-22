import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random
from PIL import Image
from model import get_class

load_dotenv()
token = os.getenv("TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot is online and ready to help with recycling!")

@bot.tree.command(name="hello", description="Says hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Hello! I'm here to help you with recycling. Ask me anything!"
    )

@bot.tree.command(name="battery", description="how to dispose of batteries")
async def battery(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Batteries should be taken to recycling points in shops. Do not throw them in normal bins."
    )

@bot.tree.command(name="plastic", description="how to dispose of plastic")
async def plastic(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Plastic should be cleaned and placed in the recycling bin."
    )

@bot.tree.command(name="glass", description="how to dispose of glass")
async def glass(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Glass should be cleaned and placed in the recycling bin."
    )

@bot.tree.command(name="paper", description="how to dispose of paper")
async def paper(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Paper should be clean and placed in the recycling bin."
    )

@bot.tree.command(name="food", description="how to dispose of food waste")
async def food(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Food waste should go in compost or food waste bins."
    )

@bot.tree.command(name="help", description="shows commands")
async def help_cmd(interaction: discord.Interaction):
    await interaction.response.send_message(
        "/hello\n/battery\n/plastic\n/glass\n/paper\n/food\n/tip\n/fact\n/scan"
    )

@bot.tree.command(name="fact", description="random recycling fact")
async def fact(interaction: discord.Interaction):
    facts = [
        "Plastic can take over 400 years to decompose.",
        "Glass can be recycled forever.",
        "Recycling saves energy.",
        "Recycling reduces pollution."
    ]
    await interaction.response.send_message(random.choice(facts))

@bot.tree.command(name="tip", description="random recycling tip")
async def tip(interaction: discord.Interaction):
    tips = [
        "Use reusable bags.",
        "Avoid single-use plastics.",
        "Reuse items when possible."
    ]
    await interaction.response.send_message(random.choice(tips))

@bot.tree.command(name="scan", description="scan image to identify waste")
async def scan(interaction: discord.Interaction, image: discord.Attachment):

    file_path = f"./{image.filename}"
    await image.save(file_path)

    img = Image.open(file_path).convert("RGB")

    result = get_class(img, "keras_model.h5", "labels.txt")
    result = result.lower()

    if "battery" in result:
        response = "Batteries should be taken to recycling points. Do not throw them in normal bins."
    elif "plastic" in result:
        response = "Plastic should be cleaned and placed in the recycling bin."
    elif "glass" in result:
        response = "Glass should be cleaned and placed in the recycling bin."
    elif "paper" in result:
        response = "Paper should be clean and placed in the recycling bin."
    elif "food" in result:
        response = "Food waste should go in compost or food waste bins."
    else:
        response = "I could not recognize the item."

    await interaction.response.send_message(f"Detected: {result}\n{response}")

bot.run(token)
