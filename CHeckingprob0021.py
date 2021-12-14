from logging import info
from typing import Text
import discord
import random
from discord import colour
from discord import embeds
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from playsound import playsound
from discord import channel
from discord import message
import urllib.request
import re
import webbrowser
import pyautogui
import google_auth_oauthlib
import time 

import Truth_oR_Dare_Dict



TOKEN = 'ODYyOTYwNzM4ODQyMDUwNTgw.YOf80Q.YSEmPrDXmhhHbeLoF2pkymWCLJk'

client = discord.Client()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshPyold = 1
        audio = r.listen(source)
    
    try:
        print('recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f'users said : {query}\n')
    
    except Exception as e:
        print(e)

        print('say that again plz...')
        return 'None'
    return query





@client.event
async def on_ready():
    speak("Hello Bro,my name is {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == message.channel.name:
        if user_message.lower().startswith('play'):
            user_message = user_message.replace('play','')
            user_message = user_message.replace(' ','+')
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + user_message)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            url = 'https://youtube.com/watch?v=' + str(video_ids[0])
            webbrowser.open_new(url)
            speak('its working')
        if user_message.lower() == "help":
            my_Embed = discord.Embed(title="I am Your Moma's gF",description="My Commands list",colour=0x00f00)
            my_Embed.add_field(name="my Command",value="I dont have any specific commands",inline=False)
            my_Embed.add_field(name="hello",value="will greet you with GIF",inline=False)


            await message.channel.send(embed = my_Embed)




        if user_message.lower() == 'invite':
            my_Embed = discord.Embed(title = "I am Botttt ",colour=0x00f00)
            link = "https://discord.com/api/oauth2/authorize?client_id=862960738842050580&permissions=8&scope=bot"
            my_Embed.add_field(name="here is my invite link",value=f"{link}",inline=False)

            await message.channel.send(embed = my_Embed)


        if user_message.lower() == 't':
            my_Embed = discord.Embed(title = f"{Truth_oR_Dare_Dict.Truth[ random.randint(0,len(Truth_oR_Dare_Dict.Truth))]}",description="If you HaVe Guts anSwer thIs Question",colour=0x00f00)

            await message.channel.send(embed = my_Embed)
        
        if user_message.lower() == 'd':
            my_Embed = discord.Embed(title = f"{Truth_oR_Dare_Dict.dare[ random.randint(0,len(Truth_oR_Dare_Dict.dare))]}",description="If you HaVe Guts anSwer thIs Question",colour=0x00f00)
            await message.channel.send(embed = my_Embed)
        
        if user_message.lower() == 't/d':
            my_Embed = discord.Embed(title = f"{Truth_oR_Dare_Dict.TorD[ random.randint(0,len(Truth_oR_Dare_Dict.TorD))]}",description="If you HaVe Guts anSwer thIs Question",colour=0x00f00)
            await message.channel.send(embed = my_Embed)



        elif 'switch the window' in user_message:
            user_message = user_message.replace('switch the window ','')
            if user_message == 'one time':
                pyautogui.keyDown('alt')
                pyautogui.press("tab")
                time.sleep(0.1)
                pyautogui.keyUp("alt")
            elif user_message == 'to time':
                pyautogui.keyDown('alt')
                pyautogui.press("tab")
                pyautogui.press("tab")
                time.sleep(0.2)
                pyautogui.keyUp("alt")
            elif user_message == 'three time':
                pyautogui.keyDown('alt')
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                time.sleep(0.2)
                pyautogui.keyUp("alt")           


        elif "close" in user_message.lower() :
            user_message = user_message.replace('close','')
            user_message = user_message.replace(' ','')
            user_message = user_message.title()   
            await message.channel.send(f"okey sir closing {user_message}...")
            os.system(f'taskkill/f /im {user_message}.exe')

        elif '!' in user_message:
            await message.channel.send('searching wikipedia...')
            query = user_message.replace('wikipedia', '')
            results = wikipedia.summary(query,sentences=2)
            await message.channel.send('according to wikipedia ')
            await message.channel.send(f"**{results}**")
            return

        elif user_message.lower().startswith('hello'):
            c = random.randint(1,3)
            if c == 1:
                c = "https://tenor.com/view/burak-deniz-burak-mara%C5%9Fl%C4%B1-wait-stop-gif-20116585"
            elif c == 2:
                c = "https://tenor.com/view/hello-gif-19947459"
            elif c == 3:
                c = "https://tenor.com/view/viola-davis-over-it-girl-bye-done-sassy-gif-9072347"

            await message.channel.send(f'{c}')
            return
        elif user_message.lower() == 'hello':
            url = 'https://www.youtube.com/watch?v=YBcdt6DsLQA'
            webbrowser.register('chrome',
            None,
            webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open_new(url)
        elif user_message.lower() == 'it aint me':
            url = 'https://www.youtube.com/watch?v=j6sSQq7a_Po'
            webbrowser.register('chrome',
            None,
            webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open_new(url)

        elif user_message.lower() == 'bye':
            await message.channel.send(f'https://tenor.com/view/viola-davis-over-it-girl-bye-done-sassy-gif-9072347')
            return
        elif user_message.lower() == '$random':
            response = f'This is your random number : {random.randrange(1000000)}'
            await message.channel.send(response)
            return
        if user_message.lower() == 'how r u?':
            await message.channel.send(f'https://discord.com/api/webhooks/885119380411785257/WL4vEcZcOraejG7_4YuvoXwyGmf0gcl9ePmDTZmv3lcaJkpId7TMRQuf1TBCcJMqyLlz')
            return
        if user_message.lower() == 'happy or sad?':
           await message.channel.send(f'https://tenor.com/view/katkat-gif-19412421')
           return
        if user_message.lower() == 'best chemist':
            await message.channel.send(f'https://tenor.com/view/yougotthis-breaking-bad-goddamnright-bryan-cranston-walter-white-gif-3558786')
            return
        if user_message.lower() == 'spam':              
                await message.channel.send(f"hu hoooo hu hooooo  hu hoooooo hu hoooooooooo hu hooooooooooooooo")
        if user_message.lower() == 'hey':
            await message.channel.send("Hey NubOob Ahan Did you miss me????")
            return
                            

    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used in anywhere!')
        return


client.run(TOKEN)