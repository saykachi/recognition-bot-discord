import discord
from discord.ext import commands
import asyncio
import speech_recognition as sr

client = commands.Bot(command_prefix = '.')

# Russian Swear Words
russian_swear_words = ["блять", "сука", "хуй", "ебать"]

# Speech Recognition
r = sr.Recognizer()

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_voice_state_update(member, before, after):
    if after.channel:
        if after.channel.id == <voice_channel_id>: # replace <voice_channel_id> with your voice channel id
            vc = await after.channel.connect()
            while vc.is_connected():
                try:
                    with sr.AudioFile("user_audio.wav") as source:
                        audio = r.record(source)
                        text = r.recognize_google(audio, language='ru-RU')
                        for word in russian_swear_words:
                            if word in text:
                                await vc.disconnect()
                                await asyncio.sleep(1)
                                await vc.connect()
                                break
                except:
                    pass

client.run('<your_bot_token>') # replace <your_bot_token> with your Discord bot token
