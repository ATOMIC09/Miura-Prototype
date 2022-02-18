from unittest import async_case
import discord
from discord.ext import commands
from math import factorial
import datetime
import urllib.parse, urllib.request, re
import requests
from time import sleep
import os
import asyncio
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL
from dotenv import load_dotenv
from discord.utils import get
import shutil
import uuid
import cv2
import ffmpy
from videoprops import get_video_properties
import math
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import pdf2image
import deepfryer
from time import sleep
from discord.ext import tasks, commands
import serial
import gdrive_dl
import audio2video
import moviepy
import earrape_warning
import red_eye
from petpetgif import petpet
import gtts
import json

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='-', description="wat", intents=intents)
bot.remove_command('help')
bot.version = "Version 2.7 Beta"

@bot.command()
async def help(ctx):
    help = discord.Embed(title = "❔ **Help**", color = 0xFF9600)
    help.add_field(name="🖼️ Image Processing", value="`%help_image`")
    help.add_field(name="🎬 Video Processing", value="`%help_video`")
    help.add_field(name="🎵 เพลง", value="`%help_music`")
    help.add_field(name="⬇ Downloader", value="`%help_dl`")
    help.add_field(name="⏲️ นับถอยหลัง", value="`%countdown [เวลา]`")
    help.add_field(name="⏏ นับถอยหลังและตัดการเชื่อมต่อ", value="`%countdis [เวลา]`")
    help.add_field(name="🔇 ปิดเสียงสมาชิก", value="`%mute [@USER] [เวลา]`")
    help.add_field(name="🔊 ยกเลิกการปิดเสียง", value="`%unmute [@USER]`")
    help.add_field(name="📄 แปลง PDF เป็นรูปภาพ", value="`%pdf2png`\n`%pdf2png_zip`")
    help.add_field(name="📰 ดูคุณสมบัติรูปภาพ", value="`%imginfo`")
    help.add_field(name="🔍 ค้นหารูปภาพ", value="`%imgser`")
    help.add_field(name="👄 สังเคราะห์เสียง", value="`%tts [ตัวย่อภาษา] [ข้อความ]`")
    help.add_field(name="❎ ยกเลิกคำสั่ง", value="`%c_[ชื่อคำสั่ง]`")
    await ctx.send(embed = help)


@bot.command()
async def help_music(ctx):
    music = discord.Embed(title = "🎵 **Music**", color = 0xFF9600)
    music.add_field(name="📶 เรียกบอท", value="`%summon`")
    music.add_field(name="⏏️ เตะบอท", value="`%dis`")
    music.add_field(name="▶️ เปิดเพลง", value="`%p [URL]`")
    music.add_field(name="🖥 เปิดเพลงแบบแนบไฟล์", value="`%plocal` + แนบไฟล์เสียง")
    music.add_field(name="⏭️ ข้าม", value="`%s`")
    music.add_field(name="⏸️ พัก", value="`%pause`")
    music.add_field(name="⏯️ เล่นต่อ", value="`%resume`")
    music.add_field(name="⏹️ หยุด", value="`%stop`")
    music.add_field(name="🔢 ดูคิว", value="`%q`")
    music.add_field(name="🆑 ล้างคิวทั้งหมด", value="`%c`")
    await ctx.send(embed = music)

@bot.command()
async def help_image(ctx):
    image = discord.Embed(title = "🖼️ **Image Processing**", color = 0xFF9600)
    image.add_field(name="⬜ แปลงภาพสีเป็นภาพขาวดำ", value="`%grayscale`")
    image.add_field(name="🎨 แปลงภาพขาวดำเป็นภาพสี", value="`%color`")
    image.add_field(name="🧹 ลบพื้นหลัง", value="`%removebg`")
    image.add_field(name="👺 Deep Fryer", value="`%deepfry`")
    image.add_field(name="🤚🏻🐶 Petpet Meme", value="`%pet`")
    image.add_field(name="👁 ตาแดง", value="`%redeye`")
    image.add_field(name="↔ ยืดภาพ", value="`%wide`")
    image.add_field(name="↔↔ ยืดดดดดภาพ", value="`%ultrawide`")
    image.add_field(name="↗ ปรับสเกลภาพ", value="`%resize [PERCENT%]`\n`%resize [Width]x[Height]`\n\n**Ex:**\n`%resize 50`\n`%resize 50%`\n`%resize 1280x720`\n`%resize 1280 720`")
    image.add_field(name="✏ เขียนข้อความบนภาพ", value="`%text [ข้อความ] | [สี] | [ขนาด] | [ตำแหน่ง] | [ความหนา]`\n*(ไม่จำเป็นต้องกรอกข้อมูลทั้งหมด)*\n\n**Ex:**\n`%text HELLO | น้ำเงิน | 5 | ล่าง | 3`")
    await ctx.send(embed = image)

@bot.command()
async def help_video(ctx):
    video = discord.Embed(title = "🎬 **Video Processing**", color = 0xFF9600)
    video.add_field(name="🔨 สร้างวิดีโอจากไฟล์ภาพและไฟล์เสียง", value="`%imgaudio`\n*(ต้องส่ง**ภาพ**ก่อนใช้คำสั่ง)*")
    video.add_field(name="⚒ สร้างวิดีโอจากไฟล์ภาพและเสียงจาก Youtube", value="`%imgyt [URL]`\n*(ต้องส่ง**ภาพ**ก่อนใช้คำสั่ง)*")
    video.add_field(name="🧲 นำคลิปวิดีโอมาต่อกัน", value="`%videomix`\n*(ต้องส่ง**วิดีโอ**ก่อนใช้คำสั่ง)*")
    await ctx.send(embed = video)
    

@bot.command()
async def help_dl(ctx):
    dl = discord.Embed(title = "⬇ **Downloader**", color = 0xFF9600)
    dl.add_field(name="📺 Youtube Downloader", value="`%yt [URL]`")
    dl.add_field(name="🔊 Audio Downloader", value="`%audio [URL]`")
    dl.add_field(name="🎥 Video Downloader", value="`%video [URL]`")
    dl.add_field(name="🗜 Resolution Only", value="`%video_res [URL]`")
    dl.add_field(name="🗜 FPS Only", value="`%video_fps [URL]`")
    await ctx.send(embed = dl)

@bot.command()
async def update(ctx):
    update = discord.Embed(title = "📌 **Update**", color = 0xFF9600)
    update.add_field(name="1️⃣ V 2.0 | 07/11/2021", value="`• Add: Countdown\n• Add: PrivateKey\n• Add: Mute\n• Add: YT Downloader\n• Add: Music Player\n• Add: Image Processing`")
    update.add_field(name="2️⃣ V 2.1 | 12/11/2021", value="`• Add: Audio and Video Downloader`")
    update.add_field(name="3️⃣ V 2.2 | 29/11/2021", value="`• Add: Image Processing\n• Add: Countdown and Disconnect\n• Add: PDF To PNG Converter\n• Add: Play Audio (Local)\n• Fix: Prefix`")
    update.add_field(name="4️⃣ V 2.3 | 17/12/2021", value="`• Add: Remove Background\n• Add: AutoSave Attachment\n• Add: Resize (width x height)\n• Add: Read Last Attachment\n• Fix: Alpha Channel for Image Processing`")
    update.add_field(name="5️⃣ V 2.4 | 20/12/2021", value="`• Add: Text on Image\n• Add: Grayscale to Color\n• Add: Deep Fryer\n• Fix: Countdown Style\n• Fix: Cancel Command\n• Delete: PrivateKey`")
    update.add_field(name="6️⃣ V 2.5 | 12/01/2022", value="`• Add: Scamming Protection\n• Add: Role Selector\n• Fix: มี Model ของ %color แล้ว`")
    update.add_field(name="7️⃣ V 2.6 | 21/01/2022", value="`• Add: Earrape Warning\n• Add: Video Processing`")
    update.add_field(name="8️⃣ V 2.7 | 09/02/2022", value="`• Add: Red Eye Meme\n• Add: Text to Speech\n• Add: Image Properties\n• Add: Image Processing\n• Add: Video Processing`")
    await ctx.send(embed = update)


# Countdown
bot.timer = 0

@bot.command()
async def countdown(ctx, timer: int):
    bot.timer = timer
    if bot.timer < 0:
        await ctx.send("**Invalid Timer ⚠️**")
        return

    year = int(bot.timer / 31556926)
    sade1 = int(bot.timer % 31556926)
    month = int(sade1 / 2629744)
    sade2 = int(sade1 % 2629744)
    day = int(sade2 / 86400)
    sade3 = int(sade2 % 86400)
    hour = int(sade3 / 3600)
    sade4 = int(sade3 % 3600)
    minute = int(sade4 / 60)
    second = int(sade4 % 60)

    # ปรับขนาดตัวอักษร
    year_str = str(year)
    month_str = str(month)
    day_str = str(day)
    hour_str = str(hour)
    minute_str = str(minute)
    second_str = str(second)

    # เริ่มนับ
    if bot.timer >= 0 and bot.timer < 10:
        message = await ctx.send(f"Time remaining: **{second_str} secs**")

    elif bot.timer >= 10 and bot.timer < 60:
        message = await ctx.send(f"Time remaining: **{second_str} secs**")

    elif bot.timer >= 60 and bot.timer < 3600:
        message = await ctx.send(f"Time remaining: **{minute_str} mins {second_str} secs**")

    elif bot.timer >= 3600 and bot.timer < 86400:
        message = await ctx.send(f"Time remaining: **{hour_str} hours {minute_str} mins {second_str} secs**")

    elif bot.timer >= 86400 and bot.timer < 2629744:
        message = await ctx.send(f"Time remaining: **{day_str} days {hour_str} hours {minute_str} mins {second_str} secs**")

    elif bot.timer >= 2629744 and bot.timer < 31556926:
        message = await ctx.send(f"Time remaining: **{month_str} months {day_str} days {hour_str} hours {minute_str} mins {second_str} secs**")

    elif bot.timer >= 31556926:
        message = await ctx.send(f"Time remaining: **{year_str} years {month_str} months {day_str} days {hour_str} hours {minute_str} mins {second_str} secs**")

    while bot.timer >= 0:
        year = int(bot.timer / 31556926)
        sade1 = int(bot.timer % 31556926)
        month = int(sade1 / 2629744)
        sade2 = int(sade1 % 2629744)
        day = int(sade2 / 86400)
        sade3 = int(sade2 % 86400)
        hour = int(sade3 / 3600)
        sade4 = int(sade3 % 3600)
        minute = int(sade4 / 60)
        second = int(sade4 % 60)

        # ปรับขนาดตัวอักษร
        year_str = str(year)
        month_str = str(month)
        day_str = str(day)
        hour_str = str(hour)
        minute_str = str(minute)
        second_str = str(second)
        
        if bot.timer >= 0 and bot.timer < 10:
            await message.edit(content=f"Time remaining: **{second_str} secs **")

        elif bot.timer >= 10 and bot.timer < 60:
            await message.edit(content=f"Time remaining: **{second_str} secs**")

        elif bot.timer >= 60 and bot.timer < 3600:
            await message.edit(content=f"Time remaining: **{minute_str} mins {second_str} secs**")

        elif bot.timer >= 3600 and bot.timer < 86400:
            await message.edit(content=f"Time remaining: **{hour_str} hours {minute_str} mins {second_str} secs**")

        elif bot.timer >= 86400 and bot.timer < 2629744:
            await message.edit(content=f"Time remaining: **{day_str} days {hour_str} hours {minute_str} mins {second_str} secs**")

        elif bot.timer >= 2629744 and bot.timer < 31556926:
            await message.edit(content=f"Time remaining: **{month_str} months {day_str} days {hour_str} hours {minute_str} mins {second_str} secs**")

        elif bot.timer >= 31556926:
            await message.edit(content=f"Time remaining: **{year_str} years {month_str} months {day_str} days {hour_str} hours {minute_str} mins {second_str} secs**")

        await asyncio.sleep(1)
        bot.timer -= 1

    if bot.timer >= -3 and bot.timer <= 1:
        await message.edit(content="Time remaining: **Time Up !!**")

    elif bot.timer < -5:
        await message.edit(content="Time remaining: **CANCELED !!**")


@bot.command()
async def c_countdown(ctx):
    bot.timer = -6
    await ctx.send("⏹ **Canceled**")

# Countdown Disconnect
bot.timer_dis = 0

@bot.command()
async def countdis(ctx, timer: int):
    channel = ctx.message.author.voice.channel
    members = channel.members
    people_counter = 0
    bot.timer_dis = timer
    if bot.timer_dis < 0:
        await ctx.send("**Invalid Timer ⚠️**")
        return

    year = int(bot.timer_dis / 31556926)
    sade1 = int(bot.timer_dis % 31556926)
    month = int(sade1 / 2629744)
    sade2 = int(sade1 % 2629744)
    day = int(sade2 / 86400)
    sade3 = int(sade2 % 86400)
    hour = int(sade3 / 3600)
    sade4 = int(sade3 % 3600)
    minute = int(sade4 / 60)
    second = int(sade4 % 60)

    # ปรับขนาดตัวอักษร
    year_str = str(year)
    month_str = str(month)
    day_str = str(day)
    hour_str = str(hour)
    minute_str = str(minute)
    second_str = str(second)

    # เริ่มนับ
    if bot.timer_dis >= 0 and bot.timer_dis < 10:
        message = await ctx.send(f"Time remaining: **{second_str} secs**")

    elif bot.timer_dis >= 10 and bot.timer_dis < 60:
        message = await ctx.send(f"Time remaining: **{second_str} secs**")

    elif bot.timer_dis >= 60 and bot.timer_dis < 3600:
        message = await ctx.send(f"Time remaining: **{minute_str} mins {second_str} secs**")

    elif bot.timer_dis >= 3600 and bot.timer_dis < 86400:
        message = await ctx.send(f"Time remaining: **{hour_str} hours {minute_str} mins {second_str} secs**")

    elif bot.timer_dis >= 86400 and bot.timer_dis < 2629744:
        message = await ctx.send(f"Time remaining: **{day_str} days {hour_str} hours {minute_str} mins {second_str} secs**")

    elif bot.timer_dis >= 2629744 and bot.timer_dis < 31556926:
        message = await ctx.send(f"Time remaining: **{month_str} months {day_str} days {hour_str} hours {minute_str} mins {second_str} secs**")

    elif bot.timer_dis >= 31556926:
        message = await ctx.send(f"Time remaining: **{year_str} years {month_str} months {day_str} days {hour_str} hours {minute_str} mins {second_str} secs**")

    while bot.timer_dis >= 0:
        year = int(bot.timer_dis / 31556926)
        sade1 = int(bot.timer_dis % 31556926)
        month = int(sade1 / 2629744)
        sade2 = int(sade1 % 2629744)
        day = int(sade2 / 86400)
        sade3 = int(sade2 % 86400)
        hour = int(sade3 / 3600)
        sade4 = int(sade3 % 3600)
        minute = int(sade4 / 60)
        second = int(sade4 % 60)

        # ปรับขนาดตัวอักษร
        year_str = str(year)
        month_str = str(month)
        day_str = str(day)
        hour_str = str(hour)
        minute_str = str(minute)
        second_str = str(second)
                
        if bot.timer_dis >= 0 and bot.timer_dis < 10:
            await message.edit(content=f"Time remaining: **{second_str} secs **")

        elif bot.timer_dis >= 10 and bot.timer_dis < 60:
            await message.edit(content=f"Time remaining: **{second_str} secs**")

        elif bot.timer_dis >= 60 and bot.timer_dis < 3600:
            await message.edit(content=f"Time remaining: **{minute_str} mins {second_str} secs**")

        elif bot.timer_dis >= 3600 and bot.timer_dis < 86400:
            await message.edit(content=f"Time remaining: **{hour_str} hours {minute_str} mins {second_str} secs**")

        elif bot.timer_dis >= 86400 and bot.timer_dis < 2629744:
            await message.edit(content=f"Time remaining: **{day_str} days {hour_str} hours {minute_str} mins {second_str} secs**")

        elif bot.timer_dis >= 2629744 and bot.timer_dis < 31556926:
            await message.edit(content=f"Time remaining: **{month_str} months {day_str} days {hour_str} hours {minute_str} mins {second_str} secs**")

        elif bot.timer_dis >= 31556926:
            await message.edit(content=f"Time remaining: **{year_str} years {month_str} months {day_str} days {hour_str} hours {minute_str} mins {second_str} secs**")

        await asyncio.sleep(1)
        bot.timer_dis -= 1

    if bot.timer_dis >= -3 and bot.timer_dis <= 1:
        await message.edit(content="Time remaining: **Time Up !!**")
        members = channel.members
        for member in members:
            await member.move_to(None)
            people_counter += 1
        await ctx.send(f"ℹ **Disconnected {people_counter} users from `{channel}` successfully**")

    elif bot.timer_dis < -5:
        await message.edit(content="Time remaining: **CANCELED !!**")


@bot.command()
async def c_countdis(ctx):
    bot.timer_dis = -6
    await ctx.send("⏹ **Canceled**")

@bot.command()
async def send(ctx, id, *, text):
    if 269000561255383040 == ctx.message.author.id :
        channel = ctx.bot.get_channel(int(id))
        await channel.send(text)


# Mute
bot.mute_cancel_code = 0
@bot.command()
async def mute(ctx, user: discord.Member, time: int):
    role_mute = discord.utils.get(user.guild.roles, name="Muted")
    
    await user.add_roles(role_mute)
    await ctx.send(f"**{user}** has been muted for {time} second ⛔")
    bot.mute_cancel_code == 0
    await asyncio.sleep(time)

    if bot.mute_cancel_code == 0:
        await user.remove_roles(role_mute)
        await ctx.send(f"**{user}** has been unmuted ✅")
    else:
        bot.mute_cancel_code = 0
        return

@bot.command()
async def unmute(ctx, user: discord.Member):
    role_mute = discord.utils.get(user.guild.roles, name="Muted")
    try:
        await user.remove_roles(role_mute)
        bot.mute_cancel_code = 1
        await ctx.send(f"**{user}** has been unmuted ✅")
    except:
        await ctx.send(f"**{user}** is not muted ⚠️")


# Youtube Downloader
@bot.command()
async def yt(ctx, url: str):
    AUDIO_YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    VIDEO_YDL_OPTIONS = {'format': 'best'}

    with YoutubeDL(AUDIO_YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
    AUDIO_DOWNLOAD = info['url']

    with YoutubeDL(VIDEO_YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
    VIDEO_DOWNLOAD = info['url']

    d = discord.Embed(title = "**Youtube Downloader**", color = 0xFF9600)
    d.add_field(name=f"**Audio** :musical_note:", value=f"[🔽]({AUDIO_DOWNLOAD})")
    d.add_field(name=f"**Video** :film_frames:", value=f"[🔽]({VIDEO_DOWNLOAD})")
    await ctx.send(embed = d)


# Music Player
@bot.command()
async def summon(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

@bot.command()
async def dis(ctx):
    voice_client = ctx.guild.voice_client
    await voice_client.disconnect()

bot.queue = []
bot.queue_name = []
bot.queue_notdel = []

@bot.command()
async def p(ctx, url: str):
    # ประกาศสิ่งที่จำเป็น
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True', 'outtmpl': '%(title)s'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    # เช็คว่าอยู่ใน Voice Channel ไหม
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    bot.queue.append(url) # เก็บทุกเพลงไว้ในคิว

    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(bot.queue[0], download=False)
        filename = ydl.prepare_filename(info)
    URL = info['url']
    bot.queue_notdel.append(filename)
    bot.queue_name.append(filename)

    while int(voice.is_playing()) == 0: # ถ้าเพลงไม่ได้เล่นก็ให้เล่น
        # เล่นเพลง
        voice.play(discord.FFmpegPCMAudio(executable="A:/Documents/GitHub/Miura-Prototype/ffmpeg.exe", source=URL, **FFMPEG_OPTIONS))
        # ส่งข้อความกลับ
        await ctx.send(f"🎶 **Playing** `{bot.queue_name[0]}`")
        bot.queue.pop(0)
        bot.queue_name.pop(0)

@bot.command()
async def s(ctx):
    try:
        voice = get(bot.voice_clients, guild=ctx.guild)
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True', 'outtmpl': '%(title)s'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        voice.stop()
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(bot.queue[0], download=False)
        URL = info['url']
        voice.play(discord.FFmpegPCMAudio(executable="A:/Documents/GitHub/Miura-Prototype/ffmpeg.exe", source=URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('⏩ **Skipped**')
        bot.queue.pop(0)
        bot.queue_name.pop(0)
        bot.queue_notdel.pop(0)
    except:
        await ctx.send("ℹ️ **Can't find the song in the queue**")
        bot.queue_name.clear()
        bot.queue_notdel.clear()

@bot.command()
async def q(ctx):
    number_emoji = [":one:",":two:",":three:",":four:",":five:",":six:",":seven:",":eight:",":nine:",":keycap_ten:"]

    data = ""
    if len(bot.queue_notdel) != 0:
        for i in range(len(bot.queue_notdel)):
            try:
                number_title = number_emoji[i]
            except: 
                bot.queue_notdel.clear()
                number_title = number_emoji[i]
            music_name = bot.queue_notdel[i]
            data += f"{number_title} {music_name}\n"
            
        q = discord.Embed(title = "🔢 **Queue**", color = 0xFF9600)
        q.description = data
        await ctx.send(embed = q)
    else:
        await ctx.send("ℹ **Empty**")

@bot.command()
async def c(ctx):
    bot.queue.clear()
    bot.queue_name.clear()
    bot.queue_notdel.clear()
    await ctx.send("✅ **Queue Cleared**")

@bot.command()
async def resume(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('▶️ **Resumed**')

@bot.command()
async def pause(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('⏸ **Paused**')

@bot.command()
async def stop(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('⏹ **Stopped**')

@bot.command()
async def plocal(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    channel = ctx.message.author.voice.channel

    audioName = "miura_autosave.mp3"
    try: 
        await asyncio.sleep(3)
        os.rename("miura_autosave",audioName)
    except:
        voice.stop()
        await asyncio.sleep(1)
        os.remove(audioName)
        os.rename("miura_autosave",audioName)
        
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    try: 
        voice.play(discord.FFmpegPCMAudio(source=audioName,executable="A:/Documents/GitHub/Miura-Tester/ffmpeg.exe"))
        await ctx.send("✅ **Now Playing**")
    except:
        voice.stop()
        voice.play(discord.FFmpegPCMAudio(source=audioName,executable="A:/Documents/GitHub/Miura-Tester/ffmpeg.exe"))
        await ctx.send("✅ **Now Playing**")

# Audio Downloader
@bot.command()
async def audio(ctx, url: str):
    async with ctx.typing():
        await ctx.send("⬇ **Starting to download...**")
        YDL_OPTIONS = {'format': 'bestaudio[ext=m4a]', 'noplaylist': 'True', 'outtmpl': '%(title)s.%(ext)s'}
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
        await ctx.send(file=discord.File(f"{filename}"))
        os.remove(f"{filename}")


# Video Downloader
@bot.command()
async def video(ctx, url: str):
    async with ctx.typing():
        dont = 0
        fail = 0
        number = 0
        number_new = 1
        
        await ctx.send(f"\ndont = {dont}\nfail = {fail}\nnumber = {number}\nnumber_new = {number_new}")

        try:
            await ctx.send("⬇ **Starting to download...**")
            YDL_OPTIONS = {'format': 'worst', 'noplaylist': 'True', 'outtmpl': f'video_compressed_lv0.mp4'}
            with YoutubeDL(YDL_OPTIONS) as ydl:
                ydl.extract_info(url, download=True)
            await ctx.send(file=discord.File(f'video_compressed_lv0.mp4'))
            os.remove(f"video_compressed_lv0.mp4")

        except:         # ส่งไม่ได้ จึงบีบอัด
            await ctx.send("ℹ **Compression Mode: **`Automatic`")

            # อ่านค่าวิดิโอต้นฉบับ
            await ctx.send("กำลังอ่านค่าวิดิโอต้นฉบับ")
            video_data = get_video_properties(f'video_compressed_lv0.mp4')
            width = video_data['width']
            height = video_data['height']
            fps_raw = video_data['avg_frame_rate']
            frame_str,time_str = fps_raw.split("/")
            frame = int(frame_str)
            time = int(time_str)
            fps = math.ceil(frame/time)

            await ctx.send("เข้า for")
            for i in range(3):              # ลองแค่ 3 ครั้ง (ได้ 6 ไฟล์)
                if dont == 0:
                    # ลด Resolution
                    await ctx.send("**=== ลด Resolution ===**")
                    await ctx.send(f"dont = {dont}\nfail = {fail}\nnumber = {number}\nnumber_new = {number_new}\ni = {i}")

                    width = math.ceil(width/1.5)
                    height = math.ceil(height/1.5)

                    # ถ้า Resolution หาร 2 ไม่ลงตัวก็จะปรับค่า
                    if width % 2 == 1: 
                        width -= 1
                    if height % 2 == 1:
                        height -= 1


                    ff = ffmpy.FFmpeg(
                    inputs={f'video_compressed_lv{number}.mp4': None},
                    outputs={f'video_compressed_lv{number_new}.mp4': f'-vf scale={width}:{height} -y'}
                    )
                    ff.run()

                    # เก็บค่าวิดีโอใหม่
                    await ctx.send("เก็บค่าวิดีโอใหม่")
                    video_data = get_video_properties(f'video_compressed_lv{number_new}.mp4')
                    width = video_data['width']
                    height = video_data['height']
                    fps_raw = video_data['avg_frame_rate']
                    frame_str,time_str = fps_raw.split("/")
                    frame = int(frame_str)
                    time = int(time_str)
                    fps = math.ceil(frame/time)
                            
                    # ลองส่ง
                    try:
                        await ctx.send("ลองส่ง")
                        await ctx.send(file=discord.File(f'video_compressed_lv{number_new}.mp4'))
                        dont = 1   # ถ้าได้ให้หยุด
                        for i in range(number_new+1):
                            os.remove(f"video_compressed_lv{i}.mp4")

                    # ส่งไม่ได้ ลด Fps
                    except:
                        await ctx.send("**=== ส่งไม่ได้ ลด Fps ===**")
                        number += 1
                        number_new += 1

                        await ctx.send(f"dont = {dont}\nfail = {fail}\nnumber = {number}\nnumber_new = {number_new}")

                        # ลด Fps
                        await ctx.send("fps หาร 2")
                        fps /= 2
                        
                        ff = ffmpy.FFmpeg(
                        inputs={f'video_compressed_lv{number}.mp4': None},
                        outputs={f'video_compressed_lv{number_new}.mp4': f' -filter:v fps={fps} -y'}
                        )
                        ff.run()

                        # เก็บค่าวิดีโอใหม่
                        await ctx.send("เก็บค่าวิดีโอใหม่ 2")
                        video_data = get_video_properties(f'video_compressed_lv{number_new}.mp4')
                        width = video_data['width']
                        height = video_data['height']
                        fps_raw = video_data['avg_frame_rate']
                        frame_str,time_str = fps_raw.split("/")
                        frame = int(frame_str)
                        time = int(time_str)
                        fps = math.ceil(frame/time)

                        # ลองส่งอีกรอบ
                        try:
                            await ctx.send("ลองส่ง2")
                            await ctx.send(file=discord.File(f'video_compressed_lv{number_new}.mp4'))
                            dont = 1   # ถ้าได้ให้หยุด
                            for i in range(number_new+1):
                                os.remove(f"video_compressed_lv{i}.mp4")
                        except:
                            fail += 1
                            await ctx.send("ส่งไม่ได้2")
                            if fail == 3:
                                await ctx.send("⚠ **File too large**")
                                for i in range(number_new+1):
                                    os.remove(f"video_compressed_lv{i}.mp4")
                            number += 1
                            number_new += 1
                            await ctx.send(f"number = {number}\nnumber_new = {number_new}")
                            await ctx.send("===============================")
                            continue
                            

# Resolution Only
@bot.command()
async def video_res(ctx, url: str):
    async with ctx.typing():
        dont = 0
        fail = 0
        number = 0
        number_new = 1
        
        await ctx.send(f"dont = {dont}\nfail = {fail}\nnumber = {number}\nnumber_new = {number_new}")

        try:
            await ctx.send("⬇ **Starting to download...**")
            YDL_OPTIONS = {'format': 'worst', 'noplaylist': 'True', 'outtmpl': f'video_res_compressed_lv0.mp4'}
            with YoutubeDL(YDL_OPTIONS) as ydl:
                ydl.extract_info(url, download=True)
            await ctx.send(file=discord.File(f'video_res_compressed_lv0.mp4'))
            os.remove(f"video_res_compressed_lv0.mp4")

        except:         # ส่งไม่ได้ จึงบีบอัด
            await ctx.send("ℹ **Compression Mode: **`Resolution Only`")

            # อ่านค่าวิดิโอต้นฉบับ
            await ctx.send("กำลังอ่านค่าวิดิโอต้นฉบับ")
            video_data = get_video_properties(f'video_res_compressed_lv0.mp4')
            width = video_data['width']
            height = video_data['height']

            await ctx.send("เข้า for")
            for i in range(3):              # ลองแค่ 3 ครั้ง (ได้ 6 ไฟล์)
                if dont == 0:
                    # ลด Resolution
                    await ctx.send("**=== ลด Resolution ===**")
                    await ctx.send(f"dont = {dont}\nfail = {fail}\nnumber = {number}\nnumber_new = {number_new}\ni = {i}")

                    width = math.ceil(width/1.5)
                    height = math.ceil(height/1.5)

                    # ถ้า Resolution หาร 2 ไม่ลงตัวก็จะปรับค่า
                    if width % 2 == 1: 
                        width -= 1
                    if height % 2 == 1:
                        height -= 1


                    ff = ffmpy.FFmpeg(
                    inputs={f'video_res_compressed_lv{number}.mp4': None},
                    outputs={f'video_res_compressed_lv{number_new}.mp4': f'-vf scale={width}:{height} -y'}
                    )
                    ff.run()

                    # เก็บค่าวิดีโอใหม่
                    await ctx.send("เก็บค่าวิดีโอใหม่")
                    video_data = get_video_properties(f'video_res_compressed_lv{number_new}.mp4')
                    width = video_data['width']
                    height = video_data['height']
                            
                    # ลองส่ง
                    try:
                        await ctx.send("ลองส่ง")
                        await ctx.send(file=discord.File(f'video_res_compressed_lv{number_new}.mp4'))
                        dont = 1   # ถ้าได้ให้หยุด
                        for i in range(number_new+1):
                            os.remove(f"video_res_compressed_lv{i}.mp4")

                    except:
                        fail += 1
                        if fail == 3:
                            await ctx.send("⚠ **File too large**")
                            for i in range(number_new+1):
                                os.remove(f"video_res_compressed_lv{i}.mp4")
                        number += 1
                        number_new += 1
                        await ctx.send(f"number = {number}\nnumber_new = {number_new}")
                        await ctx.send("===============================")
                        continue

# FPS Only
@bot.command()
async def video_fps(ctx, url: str):
    async with ctx.typing():
        dont = 0
        fail = 0
        number = 0
        number_new = 1
        
        await ctx.send(f"dont = {dont}\nfail = {fail}\nnumber = {number}\nnumber_new = {number_new}")

        try:
            await ctx.send("⬇ **Starting to download...**")
            YDL_OPTIONS = {'format': 'worst', 'noplaylist': 'True', 'outtmpl': f'video_fps_compressed_lv0.mp4'}
            with YoutubeDL(YDL_OPTIONS) as ydl:
                ydl.extract_info(url, download=True)
            await ctx.send(file=discord.File(f'video_fps_compressed_lv0.mp4'))
            os.remove(f"video_fps_compressed_lv0.mp4")

        except:         # ส่งไม่ได้ จึงบีบอัด
            await ctx.send("ℹ **Compression Mode: **`FPS Only`")

            # อ่านค่าวิดิโอต้นฉบับ
            await ctx.send("กำลังอ่านค่าวิดิโอต้นฉบับ")
            video_data = get_video_properties(f'video_fps_compressed_lv0.mp4')
            fps_raw = video_data['avg_frame_rate']
            frame_str,time_str = fps_raw.split("/")
            frame = int(frame_str)
            time = int(time_str)
            fps = math.ceil(frame/time)

            await ctx.send("เข้า for")
            for i in range(3):              # ลองแค่ 3 ครั้ง (ได้ 6 ไฟล์)
                if dont == 0:
                    # ลด Fps
                    await ctx.send("fps หาร 2")
                    fps /= 2
                    
                    ff = ffmpy.FFmpeg(
                    inputs={f'video_fps_compressed_lv{number}.mp4': None},
                    outputs={f'video_fps_compressed_lv{number_new}.mp4': f' -filter:v fps={fps} -y'}
                    )
                    ff.run()

                    # เก็บค่าวิดีโอใหม่
                    await ctx.send("เก็บค่าวิดีโอใหม่")
                    video_data = get_video_properties(f'video_fps_compressed_lv{number_new}.mp4')
                    fps_raw = video_data['avg_frame_rate']
                    frame_str,time_str = fps_raw.split("/")
                    frame = int(frame_str)
                    time = int(time_str)
                    fps = math.ceil(frame/time)
                            
                    # ลองส่ง
                    try:
                        await ctx.send("ลองส่ง")
                        await ctx.send(file=discord.File(f'video_fps_compressed_lv{number_new}.mp4'))
                        dont = 1   # ถ้าได้ให้หยุด
                        for i in range(number_new+1):
                            os.remove(f"video_fps_compressed_lv{i}.mp4")

                    except:
                        fail += 1
                        if fail == 3:
                            await ctx.send("⚠ **File too large**")
                            for i in range(number_new+1):
                                os.remove(f"video_fps_compressed_lv{i}.mp4")
                        number += 1
                        number_new += 1
                        await ctx.send(f"number = {number}\nnumber_new = {number_new}")
                        await ctx.send("===============================")
                        continue
# Image Processing
@bot.command()
async def grayscale(ctx):
    async with ctx.typing():
        Name = "miura_autosave.png"
        src="miura_autosave"
        dst="miura_autosave2"
        try:
            shutil.copy(src,dst)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")
        except:
            shutil.copy(src,dst)
            os.remove(Name)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")

        img = cv2.imread(Name,cv2.IMREAD_UNCHANGED)

        # Save the transparency channel alpha
        *_, alpha = cv2.split(img)

        gray_layer = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Duplicate the grayscale image to mimic the BGR image and finally add the transparency
        img = cv2.merge((gray_layer, gray_layer, gray_layer, alpha))
        
        cv2.imwrite(Name,img)
        file = discord.File(Name)
        await ctx.send(file=file)
        #os.remove(f"A:/Documents/GitHub/Miura-Tester/{Name}")

@bot.command()
async def text(ctx,* , input: str):
    async with ctx.typing():
        # กำหนดค่ากรณีไม่ใส่ Argument ให้ครบ
        text = "untitled"
        fontScale = 3
        thickness = 3
        color = (255, 255, 255)
        font = cv2.FONT_HERSHEY_DUPLEX
        position = "lower"

        if input.count('|') == 0: # กรณีไม่กำหนด
            text = input

        elif input.count('|') == 1: # กรณีมีกำหนดสี
            text,color = input.split("|")

        elif input.count('|') == 2 : # กรณีมีกำหนดสี ขนาด
            text,color,fontScale = input.split("|")

        elif input.count('|') == 3 : # กรณีมีกำหนดสี ขนาด ตำแหน่ง
            text,color,fontScale,position = input.split("|")

        elif input.count('|') == 4 : # กรณีมีกำหนดสี ขนาด ตำแหน่ง และความหนา
            text,color,fontScale,position,thickness = input.split("|")

        # กำหนดสี
        if "red" in color or "Red" in color or "RED" in color  or "แดง" in color :
            color = (0, 0, 255)

        elif "green" in color or "Green" in color or "GREEN" in color or "เขียว" in color:
            color = (0, 255, 0)

        elif "blue" in color or "Blue" in color or "BLUE" in color or "น้ำเงิน" in color:
            color = (255, 0, 0)

        elif "white" in color or "White" in color or "WHITE" in color or "ขาว" in color:
            color = (255, 255, 255)

        elif "cyan" in color or "Cyan" in color or "CYAN" in color or "เขียวแกมน้ำเงิน" in color or "น้ำเงินแกมเขียว" in color or "เขียวน้ำเงิน" in color or "น้ำเงินเขียว" in color or "ฟ้า" in color:
            color = (255, 255, 0)

        elif "yellow" in color or "Yellow" in color or "YELLOW" in color or "เหลือง" in color :
            color = (255, 0, 255)

        elif "black" in color or "Black" in color or "BLACK" in color or "ดำ" in color :
            color = (0, 0, 0)

        elif "purple" in color or "Purple" in color or "PURPLE" in color or "ม่วง" in color :
            color = (128, 0, 128)

        elif "gray" in color or "Gray" in color or "GRAY" in color or "เทา" in color :
            color = (128, 128, 128)

        elif "orange" in color or "Orange" in color or "ORANGE" in color or "ส้ม" in color :
            color = (0, 128, 255)

        elif "pink" in color or "Pink" in color or "PINK" in color or "ชมพู" in color :
            color = (255, 128, 255)

        elif "brown" in color or "Brown" in color or "BROWN" in color or "น้ำตาล" in color :
            color = (0, 75, 150)

        # กำหนดตำแหน่ง
        if "head" in position or "upper" in position or "up" in position or "top" in position or "บน" in position:
            position = 6

        elif "center" in position or "medium" in position or "middle" in position or "between" in position or "กลาง" in position:
            position = 2

        elif "bottom" in position or "lower" in position or "floor" in position or "under" in position or "ล่าง" in position:
            position = 1.2

        # แปลง str เป็น int
        fontScale = int(fontScale)
        thickness = int(thickness)


        Name = "miura_autosave.jpg"
        src="miura_autosave"
        dst="miura_autosave2"
        try:
            shutil.copy(src,dst)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")
        except:
            shutil.copy(src,dst)
            os.remove(Name)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")

        image = cv2.imread(Name,cv2.IMREAD_UNCHANGED)

        # กำหนดตำแหน่งให้อยู่ตรงกลาง
        textsize = (cv2.getTextSize(text, font, fontScale, thickness)[0])
        textX = int((image.shape[1] - textsize[0]) / 2)
        textY = int((image.shape[0] + textsize[1]) / position)

        # เขียน
        result = cv2.putText(image, text, (textX, textY ), font, fontScale, color, thickness, cv2.LINE_AA)

        cv2.imwrite(Name,result)
        file = discord.File(Name)
        await ctx.send(file=file)

@bot.command()
async def wide(ctx):
    async with ctx.typing():
        Name = "miura_autosave.png"
        src="miura_autosave"
        dst="miura_autosave2"
        try:
            shutil.copy(src,dst)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")
        except:
            shutil.copy(src,dst)
            os.remove(Name)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")
        image = cv2.imread(Name,cv2.IMREAD_UNCHANGED)

        try:
            # Save the transparency channel alpha
            b_channel, g_channel, r_channel , alpha = cv2.split(image)
            img_RGBA = cv2.merge((b_channel, g_channel, r_channel, alpha))
        except:
            # If have no alpha channel
            b_channel, g_channel, r_channel = cv2.split(image)
            img_RGBA = cv2.merge((b_channel, g_channel, r_channel))

        height, width, channels = img_RGBA.shape
        size = (math.ceil(width*2), math.ceil(height/2))

        res = cv2.resize(img_RGBA, size)
        cv2.imwrite(Name,res)
        file = discord.File(Name)
        await ctx.send(file=file)
        #os.remove(f"A:/Documents/GitHub/Miura-Tester/{Name}")

@bot.command()
async def ultrawide(ctx):
    async with ctx.typing():
        Name = "miura_autosave.png"
        src="miura_autosave"
        dst="miura_autosave2"
        try:
            shutil.copy(src,dst)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")
        except:
            shutil.copy(src,dst)
            os.remove(Name)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")
        image = cv2.imread(Name,cv2.IMREAD_UNCHANGED)

        try:
            # Save the transparency channel alpha
            b_channel, g_channel, r_channel , alpha = cv2.split(image)
            img_RGBA = cv2.merge((b_channel, g_channel, r_channel, alpha))
        except:
            # If have no alpha channel
            b_channel, g_channel, r_channel = cv2.split(image)
            img_RGBA = cv2.merge((b_channel, g_channel, r_channel))

        height, width, channels = img_RGBA.shape
        size = (math.ceil(width*4), math.ceil(height/4))

        res = cv2.resize(img_RGBA, size)
        cv2.imwrite(Name,res)
        file = discord.File(Name)
        await ctx.send(file=file)
        #os.remove(f"A:/Documents/GitHub/Miura-Tester/{Name}")

@bot.command()
async def resize(ctx,* , new_size: str):
    async with ctx.typing():
        Name = "miura_autosave.png"
        src="miura_autosave"
        dst="miura_autosave2"
        try:
            shutil.copy(src,dst)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")
        except:
            shutil.copy(src,dst)
            os.remove(Name)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")
        image = cv2.imread(Name,cv2.IMREAD_UNCHANGED)

        try:
            # Save the transparency channel alpha
            b_channel, g_channel, r_channel , alpha = cv2.split(image)
            img_RGBA = cv2.merge((b_channel, g_channel, r_channel, alpha))
        except:
            # If have no alpha channel
            b_channel, g_channel, r_channel = cv2.split(image)
            img_RGBA = cv2.merge((b_channel, g_channel, r_channel))

        height, width, channels = img_RGBA.shape
        if "x" in new_size:
            width_new,height_new = new_size.split("x")
            width_new = int(width_new)
            height_new = int(height_new)
            
        elif "%" in new_size:
            new_size = int(new_size.replace("%", ""))
            width_new = int(math.ceil(width*new_size/100))
            height_new = int(math.ceil(height*new_size/100))

        else:
            width_new,height_new = new_size.split(" ")
            width_new = int(width_new)
            height_new = int(height_new)

        size = (width_new, height_new)
        new_img = cv2.resize(img_RGBA, size)
        cv2.imwrite(Name,new_img)

        file = discord.File(Name)
        await ctx.send(f"`{width} x {height}` => `{width_new} x {height_new}`")
        await ctx.send(file=file)
        #os.remove(f"A:/Documents/GitHub/Miura-Tester/{Name}")

@bot.command()
async def imginfo(ctx):
    Name = "miura_autosave.png"
    src="miura_autosave"
    dst="miura_autosave2"
    try:
        shutil.copy(src,dst)
        os.rename("miura_autosave",Name)
        os.rename("miura_autosave2","miura_autosave")
    except:
        shutil.copy(src,dst)
        os.remove(Name)
        os.rename("miura_autosave",Name)
        os.rename("miura_autosave2","miura_autosave")
    image = cv2.imread(Name,cv2.IMREAD_UNCHANGED)

    try:
        # Save the transparency channel alpha
        b_channel, g_channel, r_channel , alpha = cv2.split(image)
        img_RGBA = cv2.merge((b_channel, g_channel, r_channel, alpha))
    except:
        # If have no alpha channel
        b_channel, g_channel, r_channel = cv2.split(image)
        img_RGBA = cv2.merge((b_channel, g_channel, r_channel))

    height, width, channels = img_RGBA.shape
    if channels == 1:
        channels_out = "Grayscale"
    elif channels == 2:
        channels_out = "Grayscale Alpha"
    elif channels == 3:
        channels_out = "RGB"
    elif channels == 4:
        channels_out = "RGBA"
    await ctx.send(f"↔ **Width :** `{width}`\n↕ **Height :** `{height}`\n<:apple_loading:940842814030360626> **Channel :** `{channels_out}`")

@bot.command()
async def pdf2png(ctx):
    async with ctx.typing():
        Name = "miura_autosave.pdf"
        src="miura_autosave"
        dst="miura_autosave2"
        try:
            shutil.copy(src,dst)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")
        except:
            shutil.copy(src,dst)
            os.remove(Name)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")

        pages = pdf2image.convert_from_path(Name, 200, poppler_path=r'A:/Documents/GitHub/Miura-Tester/poppler-21.11.0/Library/bin')

        for i in range(len(pages)):
            pages[i].save(f'A:/Documents/GitHub/Miura-Tester/pdf2image_output/page{i+1}.png', 'PNG')
            file = discord.File(f"A:/Documents/GitHub/Miura-Tester/pdf2image_output/page{i+1}.png")
            await ctx.send(file=file)

    for i in range(len(pages)):
        os.remove(f"A:/Documents/GitHub/Miura-Tester/pdf2image_output/page{i+1}.png")
    os.remove(f"A:/Documents/GitHub/Miura-Tester/{Name}")
    await asyncio.sleep(2)
    await ctx.send(f"✅ **The document was successfully converted\nℹ Number of pages: **{i+1}")

@bot.command()
async def pdf2png_zip(ctx):
    async with ctx.typing():
        author = str(ctx.message.author)
        Name = "miura_autosave.pdf"
        src="miura_autosave"
        dst="miura_autosave2"
        try:
            shutil.copy(src,dst)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")
        except:
            shutil.copy(src,dst)
            os.remove(Name)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")

        pages = pdf2image.convert_from_path(Name, 200, poppler_path=r'A:/Documents/GitHub/Miura-Tester/poppler-21.11.0/Library/bin')

        for i in range(len(pages)):
            pages[i].save(f'A:/Documents/GitHub/Miura-Tester/pdf2image_output/page{i+1}.png', 'PNG')
        
        shutil.make_archive(f'{author}_{i+1}pages', 'zip', 'A:/Documents/GitHub/Miura-Tester/pdf2image_output')
        file = discord.File(f"{author}_{i+1}pages.zip")
        await ctx.send(file=file)

    for i in range(len(pages)):
        os.remove(f"A:/Documents/GitHub/Miura-Tester/pdf2image_output/page{i+1}.png")
    os.remove(f"A:/Documents/GitHub/Miura-Tester/{Name}")
    os.remove(f"A:/Documents/GitHub/Miura-Tester/{author}_{i+1}pages.zip")
    await asyncio.sleep(2)
    await ctx.send(f"✅ **The document was successfully converted\nℹ Number of pages: **{i+1}")

@bot.command()
async def removebg(ctx):
    async with ctx.typing():
        Name = "miura_autosave.png"
        src="miura_autosave"
        dst="miura_autosave2"
        try:
            shutil.copy(src,dst)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")
        except:
            shutil.copy(src,dst)
            os.remove(Name)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")

        # load image
        img = cv2.imread(Name)

        # convert to graky
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # threshold input image as mask
        mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)[1]

        # negate mask
        mask = 255 - mask

        # apply morphology to remove isolated extraneous noise
        # use borderconstant of black since foreground touches the edges
        kernel = np.ones((3,3), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # anti-alias the mask -- blur then stretch
        # blur alpha channel
        mask = cv2.GaussianBlur(mask, (0,0), sigmaX=2, sigmaY=2, borderType = cv2.BORDER_DEFAULT)

        # linear stretch so that 127.5 goes to 0, but 255 stays 255
        mask = (2*(mask.astype(np.float32))-255.0).clip(0,255).astype(np.uint8)

        # put mask into alpha channel
        result = img.copy()
        result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
        result[:, :, 3] = mask

        # save resulting masked image
        cv2.imwrite('miura_removedbg.png', result)
        file = discord.File("miura_removedbg.png")
        await ctx.send(file=file)
        #os.remove(f"A:/Documents/GitHub/Miura-Tester/miura_removedbg.png")
        #os.remove(f"A:/Documents/GitHub/Miura-Tester/miura_autosave.png")

# IN DEV
@bot.command()
async def removebg2(ctx):
    async with ctx.typing():
        Name = "miura_autosave.png"
        src="miura_autosave"
        dst="miura_autosave2"
        try:
            shutil.copy(src,dst)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")
        except:
            shutil.copy(src,dst)
            os.remove(Name)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")

        # Read image
        img = cv2.imread(Name)
        hh, ww = img.shape[:2]

        # threshold on white
        # Define lower and uppper limits
        lower = np.array([200, 200, 200])
        upper = np.array([255, 255, 255])

        # Create mask to only select black
        thresh = cv2.inRange(img, lower, upper)

        # apply morphology
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20,20))
        morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        # get contours
        contours = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]

        # draw white contours on black background as mask
        mask = np.zeros((hh,ww), dtype=np.uint8)
        for cntr in contours:
            cv2.drawContours(mask, [cntr], 0, (255,255,255), -1)

        # get convex hull
        points = np.column_stack(np.where(thresh.transpose() > 0))
        hullpts = cv2.convexHull(points)
        ((centx,centy), (width,height), angle) = cv2.fitEllipse(hullpts)
        print("center x,y:",centx,centy)
        print("diameters:",width,height)
        print("orientation angle:",angle)

        # draw convex hull on image
        hull = img.copy()
        cv2.polylines(hull, [hullpts], True, (0,0,255), 1)

        # create new circle mask from ellipse 
        circle = np.zeros((hh,ww), dtype=np.uint8)
        cx = int(centx)
        cy = int(centy)
        radius = (width+height)/4
        cv2.circle(circle, (cx,cy), int(radius), 255, -1)

        # erode circle a bit to avoid a white ring
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (6,6))
        circle = cv2.morphologyEx(circle, cv2.MORPH_ERODE, kernel)

        # combine inverted morph and circle
        mask2 = cv2.bitwise_and(255-morph, 255-morph, mask=circle)

        # apply mask to image
        result = cv2.bitwise_and(img, img, mask=mask2)

        # save results
        cv2.imwrite('thresh.png', thresh)
        cv2.imwrite('morph.png', morph)
        cv2.imwrite('mask.png', mask)
        cv2.imwrite('hull.png', hull)
        cv2.imwrite('circle.png', circle)
        cv2.imwrite('result.png', result)

        file1 = discord.File("thresh.png")
        file2 = discord.File("morph.png")
        file3 = discord.File("mask.png")
        file4 = discord.File("hull.png")
        file5 = discord.File("circle.png")
        file6 = discord.File("result.png")
        await ctx.send(file=file1)
        await ctx.send(file=file2)
        await ctx.send(file=file3)
        await ctx.send(file=file4)
        await ctx.send(file=file5)
        await ctx.send(file=file6)


@bot.command()
async def color(ctx):
    async with ctx.typing():
        Name = "miura_autosave.png"
        src="miura_autosave"
        dst="miura_autosave2"
        try:
            shutil.copy(src,dst)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")
        except:
            shutil.copy(src,dst)
            os.remove(Name)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")

        net = cv2.dnn.readNet("model/colorization_deploy_v2.prototxt", "model/colorization_release_v2.caffemodel")
        pts = np.load("model/pts_in_hull.npy")

        class8 = net.getLayerId("class8_ab")
        conv8 = net.getLayerId("conv8_313_rh")
        pts = pts.transpose().reshape(2, 313, 1, 1)
        net.getLayer(class8).blobs = [pts.astype("float32")]
        net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

        image = cv2.imread(Name)
        scaled = image.astype("float32") / 255.0
        lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

        resized = cv2.resize(lab, (224, 224))
        L = cv2.split(resized)[0]
        L -= 50

        net.setInput(cv2.dnn.blobFromImage(L))
        ab = net.forward()[0, :, :, :].transpose((1, 2, 0))

        ab = cv2.resize(ab, (image.shape[1], image.shape[0]))

        L = cv2.split(lab)[0]
        colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)

        colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
        colorized = np.clip(colorized, 0, 1)

        colorized = (255 * colorized).astype("uint8")

        cv2.imwrite(Name, colorized)
        file = discord.File(Name)
        await ctx.send(file=file)

@bot.command()
async def deepfry(ctx):
    async with ctx.typing():
        Name = "miura_autosave.png"
        src="miura_autosave"
        dst="miura_autosave2"
        try:
            shutil.copy(src,dst)
            os.rename("miura_autosave",Name)
            shutil.move(Name,f"deepfryer_input/{Name}")
            os.rename("miura_autosave2","miura_autosave")
        except:
            os.remove(Name)
            os.rename("miura_autosave",Name)
            shutil.move(Name,f"deepfryer_input/{Name}")
            os.rename("miura_autosave2","miura_autosave")

        imageNormal = cv2.imread(Name)
        deepfryer.printFolders("deepfryer_input", "deepfryer_output")
        deepfryer.processArgs()
        deepfryer.fryImage(f"deepfryer_input/{Name}")
        deepfryer.badPosterize(imageNormal)
        deepfryer.folderCheck("deepfryer_input", "deepfryer_output")

        file = discord.File("deepfryer_output/miura_autosave-fry.png")
        await ctx.send(file=file)

@bot.command()
async def imgaudio(ctx):
    async with ctx.typing():
        # Image
        Name = "audio2video_image.png"
        src="miura_autosave"
        dst="miura_autosave2"
        try:
            shutil.copy(src,dst)
            os.rename("miura_autosave",Name)
            shutil.move(Name,f"audio2video_image_input/{Name}")
            os.rename("miura_autosave2","miura_autosave")
        except:
            os.remove(Name)
            os.rename("miura_autosave",Name)
            shutil.move(Name,f"audio2video_image_input/{Name}")
            os.rename("miura_autosave2","miura_autosave")

        await ctx.send("🔊 **Waiting for audio file**")
        await asyncio.sleep(15)

        try:
            # Audio
            mp3Name = "audio2video_audio.mp3"
            src="miura_autosave"
            dst="miura_autosave2"
            try:
                shutil.copy(src,dst)
                os.rename("miura_autosave",mp3Name)
                shutil.move(mp3Name,f"audio2video_audio_input/{mp3Name}")
                os.rename("miura_autosave2","miura_autosave")
            except:
                os.remove(mp3Name)
                os.rename("miura_autosave",mp3Name)
                shutil.move(mp3Name,f"audio2video_audio_input/{mp3Name}")
                os.rename("miura_autosave2","miura_autosave")


            image_path = "A:/Documents/GitHub/Miura-Prototype/audio2video_image_input/audio2video_image.png"
            audio_path = "A:/Documents/GitHub/Miura-Prototype/audio2video_audio_input/audio2video_audio.mp3"
            output_path = "A:/Documents/GitHub/Miura-Prototype/audio2video_video_output/audio2video_output.mp4"
            audio2video.add_static_image_to_audio(image_path, audio_path, output_path)

            file = discord.File(output_path)
            await ctx.send(file=file)
            os.remove(image_path)
            os.remove(audio_path)
            os.remove(output_path)
        except:
            await ctx.send("<:Deny:921703523111022642> **Send audio too late**")

@bot.command()
async def videomix(ctx):
    async with ctx.typing():
        FirstName = "videomix1.mp4"
        src="miura_autosave"
        dst="miura_autosave2"
        try:
            shutil.copy(src,dst)
            os.rename("miura_autosave",FirstName)
            os.rename("miura_autosave2","miura_autosave")
        except:
            os.remove(FirstName)
            os.rename("miura_autosave",FirstName)
            os.rename("miura_autosave2","miura_autosave")

        await ctx.send("📹 **Waiting for video file**")
        await asyncio.sleep(20)
        try:
            SecondName = "videomix2.mp4"
            src="miura_autosave"
            dst="miura_autosave2"
            try:
                shutil.copy(src,dst)
                os.rename("miura_autosave",SecondName)
                os.rename("miura_autosave2","miura_autosave")
            except:
                os.remove(SecondName)
                os.rename("miura_autosave",SecondName)
                os.rename("miura_autosave2","miura_autosave")

            clip1 = moviepy.editor.VideoFileClip("videomix1.mp4")
            clip2 = moviepy.editor.VideoFileClip("videomix2.mp4")

            output = moviepy.editor.concatenate_videoclips([clip1, clip2])
            output.write_videofile("videomixed.mp4")

            file = discord.File("A:/Documents/GitHub/Miura-Prototype/videomixed.mp4")
            await ctx.send(file=file)
            os.remove("videomix1.mp4")
            os.remove("videomix2.mp4")
            os.remove("videomixed.mp4")
        except:
            await ctx.send("<:Deny:921703523111022642> **Send video too late**")
    
@bot.command()
async def imgyt(ctx, url):
    async with ctx.typing():
        # Image
        Name = "audio2video_image.png"
        src="miura_autosave"
        dst="miura_autosave2"
        try:
            shutil.copy(src,dst)
            os.rename("miura_autosave",Name)
            shutil.move(Name,f"audio2video_image_input/{Name}")
            os.rename("miura_autosave2","miura_autosave")
        except:
            os.remove(Name)
            os.rename("miura_autosave",Name)
            shutil.move(Name,f"audio2video_image_input/{Name}")
            os.rename("miura_autosave2","miura_autosave")
        
        # Audio
        YDL_OPTIONS = {'format': 'bestaudio[ext=m4a]', 'noplaylist': 'True', 'outtmpl': '%(title)s.%(ext)s'}
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        shutil.move(filename,f"audio2video_audio_input/{filename}")

        image_path = "A:/Documents/GitHub/Miura-Prototype/audio2video_image_input/audio2video_image.png"
        audio_path = f"A:/Documents/GitHub/Miura-Prototype/audio2video_audio_input/{filename}"
        output_path = "A:/Documents/GitHub/Miura-Prototype/audio2video_video_output/audio2video_output.mp4"
        audio2video.add_static_image_to_audio(image_path, audio_path, output_path)

        file = discord.File(output_path)
        await ctx.send(file=file)
        os.remove(image_path)
        os.remove(audio_path)
        os.remove(output_path)

@bot.command()
async def redeye(ctx):
    async with ctx.typing():
        # Image
        imgName = "miura_red_eye.jpg"
        src="miura_autosave"
        dst="miura_autosave2"
        try:
            shutil.copy(src,dst)
            os.rename("miura_autosave",imgName)
            shutil.move(imgName,f"source_img/{imgName}")
            os.rename("miura_autosave2","miura_autosave")
        except:
            os.remove(imgName)
            os.rename("miura_autosave",imgName)
            shutil.move(imgName,f"source_img/{imgName}")
            os.rename("miura_autosave2","miura_autosave")
        
        try:
            red_eye.imagecov(imgName)
            output_path = "static/miura_red_eye.png"

            file = discord.File(output_path)
            await ctx.send(file=file)
            os.remove(output_path)
        except:
            await ctx.send("<:Deny:921703523111022642> **Something went wrong**")

@bot.command()
async def pet(ctx):
    async with ctx.typing():
        Name = "miura_petpet.png"
        src="miura_autosave"
        dst="miura_autosave2"
        try:
            shutil.copy(src,dst)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")
        except:
            os.remove(Name)
            os.rename("miura_autosave",Name)
            os.rename("miura_autosave2","miura_autosave")

        petpet.make(Name, 'miura_petpet.gif')

        file = discord.File('miura_petpet.gif')
        await ctx.send(file=file)
        os.remove('miura_petpet.gif')
        os.remove(Name)

@bot.command()
async def read(ctx,language: str,*, text: str):
        channel = ctx.message.author.voice.channel
        voice = get(bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        voice = get(bot.voice_clients, guild=ctx.guild)
        tts = gtts.gTTS(text=text,lang=language)
        tts.save('speak.mp3')
        voice.play(discord.FFmpegPCMAudio(executable="A:/Documents/GitHub/Miura-Prototype/ffmpeg.exe",source='speak.mp3'))
        os.remove('speak.mp3')

@bot.command()
async def tts(ctx,language: str,*, text: str):
        tts = gtts.gTTS(text=text,lang=language)
        tts.save('miura_tts.mp3')

        file = discord.File('miura_tts.mp3')
        await ctx.send(file=file)
        os.remove('miura_tts.mp3')

@bot.command()
async def imgser(ctx):
    Name = "miura_search.png"
    src="miura_autosave"
    dst="miura_autosave2"
    try:
        shutil.copy(src,dst)
        os.rename("miura_autosave",Name)
        os.rename("miura_autosave2","miura_autosave")
    except:
        os.remove(Name)
        os.rename("miura_autosave",Name)
        os.rename("miura_autosave2","miura_autosave")
    
    filePath = Name
    searchUrl = 'https://yandex.com/images/search'
    files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
    params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
    response = requests.post(searchUrl, params=params, files=files)
    query_string = json.loads(response.content)['blocks'][0]['params']['url']
    img_search_url= searchUrl + '?' + query_string
    await ctx.send(img_search_url)


# Minecraft ESP32 Server Log
#async def background_task():
#    await bot.wait_until_ready()
#    channel = bot.get_channel(928285429260779541)
#    ser = serial.Serial('com5',115200)
    # Read data out of the buffer until a carraige return / new line is found
#    serialString = ser.readline()

    # Print the contents of the serial data
#    print(serialString.decode('Ascii'))

    #try :
    #    data = []                        # empty list to store the data
    #    for i in range(1):
    #        b = ser.readline()            # read a byte string
    #        string_n = b.decode()        # decode byte string into Unicode  
    #        string = string_n.rstrip()    # remove \n and \r
    #        data.append(string)            # add to the end of data list
    #    ser.close()
    #    await channel.send(string)
    #except :
    #    return "⚠ **ไม่พบการเชื่อมต่อของเซ็นเซอร์**"

######################################### Automatic System ##########################################
decisionFunctionMark = lambda loudness, maxamp: maxamp > min(110, ((loudness + 1) ** 2 * 0.1 + 3) / 0.5 * -(loudness + 1))
decisionFunctionDelete = lambda loudness, maxamp: maxamp > min(110, ((loudness - 1) ** 2 * 0.1 + 2) / 0.3 * -(loudness - 1) + 25)

check_files = ("mp4", "mov", "mp3", "flac", "wav", "ogg")

@bot.listen()
async def on_message(message):
    # Scamming Protection
    if message.author.id != bot.user.id:
        keyword = ""
        channel_admin = bot.get_channel(929670988092825630)
        member = message.author
        role = discord.utils.get(message.guild.roles, name="⚠️ HACKED ⚠️")

        if "http" in message.content.lower():
            keyword += "`http` "

        if "free" in message.content.lower():
            keyword += "`Free` "

        if "nitro" in message.content.lower():
            keyword += "`Nitro` "
            
        if "@everyone" in message.content.lower():
            keyword += "`@everyone` "

        if "@here" in message.content.lower():
            keyword += "`@here` "

        if "nitro" in message.content.lower() and "free" in message.content.lower() and "http" in message.content.lower():
            await member.add_roles(role)
            await message.delete()
            
            p2 = discord.Embed(title = "⚠ **Security Alert**", color = 0xFF3C3C)
            p2.add_field(name=f"🔑 **Keyword detected**", value=keyword)
            p2.add_field(name=f"<:windows_user_white:931065351301656626> **Sent by**", value=f"<@{message.author.id}>")
            p2.add_field(name=f"ℹ **Status**", value=f"*`Deleted`*")
            await channel_admin.send(embed = p2)

            user = discord.Embed(title = "⚠️ **Scamming Detected** ⚠️", color = 0xFF0000)
            user.description = "Free Discord Nitro Scamming"
            user.add_field(name=f"<:windows_user_white:931065351301656626> **Sent by**", value=f"<@{member.id}>")
            await message.channel.send(embed = user)

        elif "free" in message.content.lower() and "@everyone" in message.content.lower() or "@here" in message.content.lower():
            p2 = discord.Embed(title = "⚠ **Security Alert**", color = 0xFF3C3C)
            p2.add_field(name=f"🔑 **Keyword detected**", value=keyword)
            p2.add_field(name=f"<:windows_user_white:931065351301656626> **Sent by**", value=f"<@{message.author.id}>")
            p2.add_field(name=f"ℹ **Status**", value=f"*`Not yet deleted`*")
            p2.description = f"**[Go to message](https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id})**"
            await channel_admin.send(embed = p2)

        elif "nitro" in message.content.lower() and "@everyone" in message.content.lower() or "@here" in message.content.lower():
            await message.add_reaction("⚠")

            p2 = discord.Embed(title = "⚠ **Security Alert**", color = 0xFF3C3C)
            p2.add_field(name=f"🔑 **Keyword detected**", value=keyword)
            p2.add_field(name=f"<:windows_user_white:931065351301656626> **Sent by**", value=f"<@{message.author.id}>")
            p2.add_field(name=f"ℹ **Status**", value=f"*`Not yet deleted`*")
            p2.description = f"**[Go to message](https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id})**"
            await channel_admin.send(embed = p2)

        elif "nitro" in message.content.lower() and "free" in message.content.lower():
            await message.add_reaction("⚠")
            
            p2 = discord.Embed(title = "⚠ **Security Alert**", color = 0xFF3C3C)
            p2.add_field(name=f"🔑 **Keyword detected**", value=keyword)
            p2.add_field(name=f"<:windows_user_white:931065351301656626> **Sent by**", value=f"<@{message.author.id}>")
            p2.add_field(name=f"ℹ **Status**", value=f"*`Not yet deleted`*")
            p2.description = f"**[Go to message](https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id})**"
            await channel_admin.send(embed = p2)

        elif "http" in message.content.lower() and "free" in message.content.lower():    
            p2 = discord.Embed(title = "⚠ **Security Alert**", color = 0xFF3C3C)
            p2.add_field(name=f"🔑 **Keyword detected**", value=keyword)
            p2.add_field(name=f"<:windows_user_white:931065351301656626> **Sent by**", value=f"<@{message.author.id}>")
            p2.add_field(name=f"ℹ **Status**", value=f"*`Not yet deleted`*")
            p2.description = f"**[Go to message](https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id})**"
            await channel_admin.send(embed = p2)


    
    # Attachments Detection
    try:
        url = message.attachments[0].url
        no1,no2,no3,no4,no5,no6,no7 = url.split("/")
        
    except IndexError:
        print("Error: No attachments")

    else:
        Name = "miura_autosave" 
        if url[0:26] == "https://cdn.discordapp.com":
            r = requests.get(url, stream=True)
            with open(Name, 'wb') as out_file:
                print('Saving : ' + Name)
                shutil.copyfileobj(r.raw, out_file)

    # Earrape Warning
    if len(message.attachments) > 0:
        for attachment in message.attachments:
            if attachment.filename.endswith(check_files):
                data = await attachment.read()
                #filename = "earrape.mp3"
                #with open(filename, "wb") as file:
                    #file.write(data)

                try:
                    loudness, maxamp, time = earrape_warning.check_audio(data)
                except Exception as error:
                    print(f"Error occured while processing file {attachment.filename}")
                    print(f"Error: {error}")
                else:
                    if decisionFunctionDelete(loudness, maxamp):
                        print(f"Loudness : {loudness}")
                        print(f"Maxamp : {maxamp}")
                        await message.add_reaction("🔊")
                        await message.add_reaction("⚠️")
                        #os.remove("earrape.mp3")
                        #os.remove("earrape_out.mp3")

                    elif decisionFunctionMark(loudness, maxamp):
                        await message.add_reaction("🔊")
                        await message.add_reaction("⚡")
                        #os.remove("earrape.mp3")
                        #os.remove("earrape_out.mp3")


# List of Role & Emoji
original_num_list = ['1️⃣',
            '2️⃣',
            '3️⃣',
            '4️⃣',
            '5️⃣',
            '6️⃣',
            '7️⃣',
            '8️⃣',
            '9️⃣']
num_emoji_list = ['🔟',
            '<:num11:907198109937979422>',
            '<:num12:907198121556181013>',
            '<:num13:907198214464229377>',
            '<:num14:907198222974480384>',
            '<:num15:907198235108605972>',
            '<:num16:907198248530362368>',
            '<:num17:907198257996918836>',
            '<:num18:907198267819958313>',
            '<:num19:907198278846795786>',
            '<:num20:907198291555520543>',
            '<:num21:907198302787883008>',
            '<:num22:929804129344311316>',
            '<:num23:929804142824796190>',
            '<:num24:929804157391613982>',
            '<:num25:929804168460386385>',
            '<:num26:929804179889877064>']

emoji_list = ['keycap_ten',
            'num11',
            'num12',
            'num13',
            'num14',
            'num15',
            'num16',
            'num17',
            'num18',
            'num19',
            'num20',
            'num21',
            'num22',
            'num23',
            'num24',
            'num25',
            'num26']

role_list = ['PrivateChatKey',
            'President',
            'Streamer',
            'SKR#24ㅣ603',
            'SKR#24ㅣ604',
            'SKR#24ㅣ605',
            'SKR#24ㅣ609',
            'SKR#24ㅣ610',
            'SKR#24ㅣ611',
            'Order of the First',
            'นักตัดงานคุณภาพ',
            'Bot Developer',
            'เสพกาววีทูบเบอร์',
            'Programmer',
            'Sportsman',
            "PlayerUnknown's Battlegrounds",
            'Microsoft Flight Simulator',
            'League of Legends',
            'Rainbow Six Siege',
            'Dead by Daylight',
            'Genshin Impact',
            'Forza Player',
            'Minecraft',
            'Valorant',
            'คณะล่าผี',
            'Roblox']

bot.addrole_message = "nothing"
bot.rolereq_message = "nothing"
bot.role = "nothing"
bot.loading = False
bot.msg_id = ""
bot.msg_au_id = ""
bot.member_request = ""

# Send Role List
@bot.command()
async def addrole(ctx):
    a = discord.Embed(title = "📝 **React me to assign the role**", color = 0x00FF00)
    a.add_field(name="**🔧 Management**", value=f":one: `{role_list[0]}`\n:two: `{role_list[1]}`\n:three: `{role_list[2]}`\n(กดเลือกทีละอันและต้องรอการยืนยัน)")
    a.add_field(name="**🏫 School**", value=f":four: `{role_list[3]}`\n:five: `{role_list[4]}`\n:six: `{role_list[5]}`\n:seven: `{role_list[6]}`\n:eight: `{role_list[7]}`\n:nine: `{role_list[8]}`")
    a.add_field(name="**💡 Other**", value=f"{num_emoji_list[0]} `{role_list[9]}`\n{num_emoji_list[1]} `{role_list[10]}`\n{num_emoji_list[2]} `{role_list[11]}`\n{num_emoji_list[3]} `{role_list[12]}`\n{num_emoji_list[4]} `{role_list[13]}`\n{num_emoji_list[5]} `{role_list[14]}`")
    a.add_field(name="**🎮 Game**", value=f"{num_emoji_list[6]} `{role_list[15]}`\n{num_emoji_list[7]} `{role_list[16]}`\n{num_emoji_list[8]} `{role_list[17]}`\n{num_emoji_list[9]} `{role_list[18]}`\n{num_emoji_list[10]} `{role_list[19]}`\n{num_emoji_list[11]} `{role_list[20]}`\n{num_emoji_list[12]} `{role_list[21]}`\n{num_emoji_list[13]} `{role_list[22]}`\n{num_emoji_list[14]} `{role_list[23]}`\n{num_emoji_list[15]} `{role_list[24]}`\n{num_emoji_list[16]} `{role_list[25]}`")
    a.description = '1 - 10 must add Reaction by yourself'

    if 269000561255383040 == ctx.message.author.id :
        channel = ctx.bot.get_channel(929955422922747906)
        bot.addrole_message = await channel.send(embed = a)
        
        bot.loading = True
        for x in range(1,len(emoji_list)):
            await bot.addrole_message.add_reaction(num_emoji_list[x])
        bot.loading = False

# Role Selector
@bot.event
async def on_raw_reaction_add(payload):
    if payload.user_id != 907247505346035752:
        if bot.loading == False:
            auth = False
            message_id = payload.message_id
            check_channel = 929670988092825630
            try:
                msg_id = bot.addrole_message.id
            except:
                msg_id = 000000000000000000

            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
            
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if message_id == msg_id:
                if payload.emoji.name == '1️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'PrivateChatKey')
                    auth = True
                elif payload.emoji.name == '2️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'President')
                    auth = True
                elif payload.emoji.name == '3️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'Streamer')
                    auth = True
                elif payload.emoji.name == '4️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'SKR#24ㅣ603')
                elif payload.emoji.name == '5️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'SKR#24ㅣ604')
                elif payload.emoji.name == '6️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'SKR#24ㅣ605')
                elif payload.emoji.name == '7️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'SKR#24ㅣ609')
                elif payload.emoji.name == '8️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'SKR#24ㅣ610')
                elif payload.emoji.name == '9️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'SKR#24ㅣ611')
                elif payload.emoji.name == emoji_list[0]:
                    bot.role = discord.utils.get(guild.roles, name = 'Order of the First')
                elif payload.emoji.name == emoji_list[1]:
                    bot.role = discord.utils.get(guild.roles, name = 'นักตัดงานคุณภาพ')
                elif payload.emoji.name == emoji_list[2]:
                    bot.role = discord.utils.get(guild.roles, name = 'Bot Developer')
                elif payload.emoji.name == emoji_list[3]:
                    bot.role = discord.utils.get(guild.roles, name = 'เสพกาววีทูบเบอร์')
                elif payload.emoji.name == emoji_list[4]:
                    bot.role = discord.utils.get(guild.roles, name = 'Programmer')
                elif payload.emoji.name == emoji_list[5]:
                    bot.role = discord.utils.get(guild.roles, name = 'Sportsman')
                elif payload.emoji.name == emoji_list[6]:
                    bot.role = discord.utils.get(guild.roles, name = "PlayerUnknown's Battlegrounds")
                elif payload.emoji.name == emoji_list[7]:
                    bot.role = discord.utils.get(guild.roles, name = 'Microsoft Flight Simulator')
                elif payload.emoji.name == emoji_list[8]:
                    bot.role = discord.utils.get(guild.roles, name = 'League of Legends')
                elif payload.emoji.name == emoji_list[9]:
                    bot.role = discord.utils.get(guild.roles, name = 'Rainbow Six Siege')
                elif payload.emoji.name == emoji_list[10]:
                    bot.role = discord.utils.get(guild.roles, name = 'Dead by Daylight')
                elif payload.emoji.name == emoji_list[11]:
                    bot.role = discord.utils.get(guild.roles, name = 'Genshin Impact')
                elif payload.emoji.name == emoji_list[12]:
                    bot.role = discord.utils.get(guild.roles, name = 'Forza Player')
                elif payload.emoji.name == emoji_list[13]:
                    bot.role = discord.utils.get(guild.roles, name = 'Minecraft')
                elif payload.emoji.name == emoji_list[14]:
                    bot.role = discord.utils.get(guild.roles, name = 'Valorant')
                elif payload.emoji.name == emoji_list[15]:
                    bot.role = discord.utils.get(guild.roles, name = 'คณะล่าผี')
                elif payload.emoji.name == emoji_list[16]:
                    bot.role = discord.utils.get(guild.roles, name = 'Roblox')
                else:
                    bot.role = discord.utils.get(guild.roles, name = payload.emoji.name)

                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                print(f"Member ID : {member.id}")
                if member.id != 907247505346035752:
                    if bot.role is not None:
                        if member is not None:
                            if auth == False:
                                await member.add_roles(bot.role)
                                print("Role Add Done")
                            else:
                                bot.member_request = member
                                await member.add_roles(discord.utils.get(guild.roles, name = 'Pending Role Approval'))
                                # ส่งคำขอ
                                channel = bot.get_channel(929670988092825630)
                                h = discord.Embed(title = "🔧 **Role Request**", color = 0x80FF81)
                                h.add_field(name=f"🎩 **Requested role**", value=f"`{bot.role}`")
                                h.add_field(name=f"🧑 **Requested by**", value=f"<@{member.id}>")
                                h.add_field(name=f"❔ **Status**", value="*`Unconfirmed`*")
                                message = await channel.send(embed = h)
                                print(f"ROLE : {bot.role}")
                                bot.rolereq_message = message
                                
                                # เพิ่ม Reaction
                                approve_emoji = "<:Approve:921703512382009354>"
                                deny_emoji = "<:Deny:921703523111022642>"
                                await channel.fetch_message(message.id)
                                await message.add_reaction(approve_emoji)
                                await message.add_reaction(deny_emoji)
                                print(f"bot.rolereq_message.id : {bot.rolereq_message.id}")
                                print(f"payload.message_id : {payload.message_id}")
                                payload.message_id = bot.rolereq_message.id

                                msg = await bot.get_channel(929670988092825630).fetch_message(payload.message_id)
                                bot.msg_id = msg.id # ไอดีข้อความ
                                bot.msg_au_id = msg.author.id # ไอดีคนเขียนข้อความ
                                print(f"------------------------- 1 -------------------------")
                                print(f"ROLE : {bot.role}")
                                print(f"msg_id : {msg.id}")
                                print(f"msg.author.id : {msg.author.id}")
                                print(f"-----------------------------------------------------\n")
                        else:
                            print("Member not found")
                    else:
                        print("Role not found")
                
                print(f"------------------------- 2 ----------------------------")
                print(f"ROLE : {bot.role}")
                print(f"msg_id : {bot.msg_id}")
                print(f"TRACK_MSG_ID2 : {payload.message_id}")
                print(f"message_author_id : {bot.msg_au_id}")
                print(f"--------------------------------------------------------\n")

                print(f"check_channel : {check_channel}")
                print(f"payload.channel.id : {payload.channel_id}")

            
            elif bot.rolereq_message.id == payload.message_id and member.id != 907247505346035752:
                print(f"member elif : {member.id}")
                print("================== REQUESTED ==================")
                print(f"ROLE : {bot.role}")
                print(f"TRACK_MSG_ID3 : {payload.message_id}")

                msg = await bot.get_channel(929670988092825630).fetch_message(payload.message_id)
                bot.msg_id = msg.id # ไอดีข้อความ
                bot.msg_au_id = msg.author.id # ไอดีคนเขียนข้อความ
                user_react = payload.message_id # ไอดีคนรีแอ็ค

                print(f"bot.msg_au_id : {bot.msg_au_id}")
                print(f"user_react : {bot.msg_au_id}") #user_react
                #if bot.msg_au_id != 907247505346035752:
                approve_emoji = "<:Approve:921703512382009354>"
                deny_emoji = "<:Deny:921703523111022642>"

                if payload.emoji.name == 'Approve':
                    member = bot.member_request
                    await member.add_roles(bot.role)
                    await member.remove_roles(discord.utils.get(guild.roles, name = 'Pending Role Approval'))
                    print("Role Add Done")
                    print("Approved")
                    msg = await bot.get_channel(929670988092825630).fetch_message(bot.rolereq_message.id)
                    #await msg.remove_reaction(approve_emoji, payload.member)
                    await msg.clear_reaction(approve_emoji)
                    await msg.clear_reaction(deny_emoji)

                    h = discord.Embed(title = "🔧 **Role Request**", color = 0x80FF81)
                    h.add_field(name=f"🎩 **Requested role**", value=f"`{bot.role}`")
                    h.add_field(name=f"🧑 **Requested by**", value=f"<@{member.id}>")
                    h.add_field(name=f"{approve_emoji} **Approved by**", value=f"<@{payload.member.id}>")
                    await bot.rolereq_message.edit(embed=h)

                elif payload.emoji.name == 'Deny':
                    print("Denied")
                    member = bot.member_request
                    await member.remove_roles(bot.role)
                    await member.remove_roles(discord.utils.get(guild.roles, name = 'Pending Role Approval'))
                    msg = await bot.get_channel(929670988092825630).fetch_message(bot.rolereq_message.id)
                    await msg.clear_reaction(approve_emoji)
                    await msg.clear_reaction(deny_emoji)

                    h = discord.Embed(title = "🔧 **Role Request**", color = 0x80FF81)
                    h.add_field(name=f"🎩 **Requested role**", value=f"`{bot.role}`")
                    h.add_field(name=f"🧑 **Requested by**", value=f"<@{member.id}>")
                    h.add_field(name=f"{deny_emoji} **Rejected by**", value=f"<@{payload.member.id}>")
                    await bot.rolereq_message.edit(embed=h)


@bot.event
async def on_raw_reaction_remove(payload):
    if payload.user_id != 907247505346035752:
        if bot.loading == False:
            auth = False
            message_id = payload.message_id
            channel = 929955422922747906
            try:
                msg_id = bot.addrole_message.id
            except:
                msg_id = 000000000000000000

            if message_id == msg_id:
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

                if payload.emoji.name == '1️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'PrivateChatKey')
                    auth = True
                elif payload.emoji.name == '2️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'President')
                    auth = True
                elif payload.emoji.name == '3️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'Streamer')
                    auth = True
                elif payload.emoji.name == '4️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'SKR#24ㅣ603')
                elif payload.emoji.name == '5️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'SKR#24ㅣ604')
                elif payload.emoji.name == '6️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'SKR#24ㅣ605')
                elif payload.emoji.name == '7️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'SKR#24ㅣ609')
                elif payload.emoji.name == '8️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'SKR#24ㅣ610')
                elif payload.emoji.name == '9️⃣':
                    bot.role = discord.utils.get(guild.roles, name = 'SKR#24ㅣ611')
                elif payload.emoji.name == emoji_list[0]:
                    bot.role = discord.utils.get(guild.roles, name = 'Order of the First')
                elif payload.emoji.name == emoji_list[1]:
                    bot.role = discord.utils.get(guild.roles, name = 'นักตัดงานคุณภาพ')
                elif payload.emoji.name == emoji_list[2]:
                    bot.role = discord.utils.get(guild.roles, name = 'Bot Developer')
                elif payload.emoji.name == emoji_list[3]:
                    bot.role = discord.utils.get(guild.roles, name = 'เสพกาววีทูบเบอร์')
                elif payload.emoji.name == emoji_list[4]:
                    bot.role = discord.utils.get(guild.roles, name = 'Programmer')
                elif payload.emoji.name == emoji_list[5]:
                    bot.role = discord.utils.get(guild.roles, name = 'Sportsman')
                elif payload.emoji.name == emoji_list[6]:
                    bot.role = discord.utils.get(guild.roles, name = "PlayerUnknown's Battlegrounds")
                elif payload.emoji.name == emoji_list[7]:
                    bot.role = discord.utils.get(guild.roles, name = 'Microsoft Flight Simulator')
                elif payload.emoji.name == emoji_list[8]:
                    bot.role = discord.utils.get(guild.roles, name = 'League of Legends')
                elif payload.emoji.name == emoji_list[9]:
                    bot.role = discord.utils.get(guild.roles, name = 'Rainbow Six Siege')
                elif payload.emoji.name == emoji_list[10]:
                    bot.role = discord.utils.get(guild.roles, name = 'Dead by Daylight')
                elif payload.emoji.name == emoji_list[11]:
                    bot.role = discord.utils.get(guild.roles, name = 'Genshin Impact')
                elif payload.emoji.name == emoji_list[12]:
                    bot.role = discord.utils.get(guild.roles, name = 'Forza Player')
                elif payload.emoji.name == emoji_list[13]:
                    bot.role = discord.utils.get(guild.roles, name = 'Minecraft')
                elif payload.emoji.name == emoji_list[14]:
                    bot.role = discord.utils.get(guild.roles, name = 'Valorant')
                elif payload.emoji.name == emoji_list[15]:
                    bot.role = discord.utils.get(guild.roles, name = 'คณะล่าผี')
                elif payload.emoji.name == emoji_list[16]:
                    bot.role = discord.utils.get(guild.roles, name = 'Roblox')
                else:
                    bot.role = discord.utils.get(guild.roles, name = payload.emoji.name)

                if bot.role is not None:
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    if member is not None:
                        if auth == False:
                            await member.remove_roles(bot.role)
                            print("Role Remove Done")
                        else:
                            await member.remove_roles(bot.role)

                            # ใช้กรณีลบ Request
                            #channel = bot.get_channel(929670988092825630)
                            #message_to_del = bot.rolereq_message
                            #await channel.fetch_message(message_to_del.id)
                            #await message_to_del.delete()
                            c = discord.Embed(title = "🔧 **Role Request**", color = 0x80FF81)
                            c.add_field(name=f"🎩 **Requested role**", value=f"`{bot.role}`")
                            c.add_field(name=f"🧑 **Requested by**", value=f"<@{member.id}>")
                            c.add_field(name=f"⛔ **Status**", value="*`Canceled`*")
                            await bot.rolereq_message.edit(embed=c)

                    else:
                        print("Member is not found")
                else:
                    print("Role is not found")

# Add Role on Join
@bot.event
async def on_member_join(person):
    try: 
        new_member = 727555789056639027 # GGWPㅣGΛMΞS ROOM
        dj = 781371092899856404
        await person.add_roles(person.guild.get_role(new_member))
        await person.add_roles(person.guild.get_role(dj))
    except:
        new_member = 851081137093738576 # Bot Datacenter
        await person.add_roles(person.guild.get_role(new_member))



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=bot.version))
    #print("Downloading : colorization_release_v2.caffemodel")
    #gdrive_dl.download_file_from_google_drive("1rVl9NFS21ckBAD7tEYGrZkpHWtPZvtfy", "A:/Documents/GitHub/Miura-Prototype/model/colorization_release_v2.caffemodel")
    #print("Downloading : shape_predictor_68_face_landmarks.dat")
    #gdrive_dl.download_file_from_google_drive("1MycdtBY4bIlfOcIokkEtDft8qaqm3lqI", "A:/Documents/GitHub/Miura-Prototype/gaze_tracking/trained_models/shape_predictor_68_face_landmarks.dat")
    status_change.start()
    print('Miura Tester Started')

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"⚠ **Error:** `{error}`")
    raise error

@tasks.loop(seconds=301)
async def status_change():
    vc = bot.get_channel(942363499777126411)

    try:
        requests.get("https://exynas.myddns.me")
        await vc.edit(name="Exynas : 🟢 ONLINE")
    except:
        await vc.edit(name="Exynas : 🔴 OFFLINE")

#bot.loop.create_task(background_task())
Token = os.environ["MiuraTesterToken"]
bot.run(Token)