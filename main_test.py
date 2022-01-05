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

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='-', description="wat", intents=intents)
bot.remove_command('help')
bot.version = "Version 1.4 Beta"

@bot.command()
async def help(ctx):
    help = discord.Embed(title = "❔ **Help**", color = 0xFF9600)
    help.add_field(name="🖼️ Image Processing", value="`%help_image`")
    help.add_field(name="🎵 เพลง", value="`%help_music`")
    help.add_field(name="⬇ Downloader", value="`%help_dl`")
    help.add_field(name="⏲️ นับถอยหลัง", value="`%countdown [เวลา]`")
    help.add_field(name="⏏ นับถอยหลังและตัดการเชื่อมต่อ", value="`%countdis [เวลา]`")
    help.add_field(name="🔇 ปิดเสียงสมาชิก", value="`%mute [@USER] [เวลา]`")
    help.add_field(name="🔊 ยกเลิกการปิดเสียง", value="`%unmute [@USER]`")
    help.add_field(name="📄➡🖼️ แปลง PDF เป็นรูปภาพ", value="`%pdf2png`\n`%pdf2png_zip`")
    help.add_field(name="❎ ยกเลิกคำสั่ง", value="`%c_[ชื่อคำสั่ง]`")
    await ctx.send(embed = help)


@bot.command()
async def help_music(ctx):
    music = discord.Embed(title = "🎵 **Music**", color = 0xFF9600)
    music.add_field(name="📶 เรียกบอท", value="`%summon`")
    music.add_field(name="⏏️ เตะบอท", value="`%dis`")
    music.add_field(name="▶️ เปิดเพลง", value="`%p [URL]`")
    music.add_field(name="▶️ 🖥 เปิดเพลงแนบไฟล์", value="`%plocal` + แนบไฟล์เสียง")
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
    image.add_field(name="↔ ยืดภาพ", value="`%wide`")
    image.add_field(name="↔↔ ยืดดดดดภาพ", value="`%ultrawide`")
    image.add_field(name="↗ ปรับสเกลภาพ", value="`%resize [PERCENT%]`\n`%resize [Width]x[Height]`\n\n**Ex:**\n`%resize 50`\n`%resize 50%`\n`%resize 1280x720`\n`%resize 1280 720`")
    image.add_field(name="✏ เขียนข้อความบนภาพ", value="`%text [ข้อความ] | [สี] | [ขนาด] | [ตำแหน่ง] | [ความหนา]`\n(ไม่จำเป็นต้องกรอกข้อมูลทั้งหมด)\n\n**Ex:**\n`%text HELLO | น้ำเงิน | 5 | ล่าง | 3`")
    await ctx.send(embed = image)

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
    update.add_field(name="1️⃣ V 1.0 | 07/11/2021", value="`• Add: Countdown\n• Add: PrivateKey\n• Add: Mute\n• Add: YT Downloader\n• Add: Music Player\n• Add: Image Processing`")
    update.add_field(name="2️⃣ V 1.1 | 12/11/2021", value="`• Add: Audio and Video Downloader`")
    update.add_field(name="3️⃣ V 1.2 | 29/11/2021", value="`• Add: Image Processing\n• Add: Countdown and Disconnect\n• Add: PDF To PNG Converter\n• Add: Play Audio (Local)\n• Fix: Prefix`")
    update.add_field(name="4️⃣ V 1.3 | 17/12/2021", value="`• Add: Remove Background\n• Add: AutoSave Attachment\n• Add: Resize (width x height)\n• Add: Read Last Attachment\n• Fix: Alpha Channel for Image Processing`")
    update.add_field(name="5️⃣ V 1.4 | 20/12/2021", value="`• Add: Text on Image\n• Add: Grayscale to Color\n• Add: Deep Fryer\n• Fix: Countdown Style\n• Fix: Cancel Command\n• Delete: PrivateKey`")
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

    while int(voice.is_playing()) == 0: # ถ้าเพลงไม่ได้เล่นก็ให้เล่น
        # เล่นเพลง
        voice.play(discord.FFmpegPCMAudio(source=URL, **FFMPEG_OPTIONS))
        # ส่งข้อความกลับ
        await ctx.send(f"🎶 **Playing** `{bot.queue_notdel[0]}`")
        bot.queue.pop(0)

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
        voice.play(discord.FFmpegPCMAudio(source=URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('⏩ **Skipped**')
        bot.queue.pop(0)
        bot.queue_notdel.pop(0)
    except:
        await ctx.send("ℹ️ **Can't find the song in the queue**")
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
        try:
            os.rename("miura_autosave",Name)
        except:
            os.remove(Name)
            os.rename("miura_autosave",Name)

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
        try:
            os.rename("miura_autosave",Name)        
        except:
            os.remove(Name)
            os.rename("miura_autosave",Name)

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
        try:
            os.rename("miura_autosave",Name)
        except:
            os.remove(Name)
            os.rename("miura_autosave",Name)
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
        try:
            os.rename("miura_autosave",Name)
        except:
            os.remove(Name)
            os.rename("miura_autosave",Name)
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
        try:
            os.rename("miura_autosave",Name)
        except:
            os.remove(Name)
            os.rename("miura_autosave",Name)
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
async def pdf2png(ctx):
    async with ctx.typing():
        try:
            url = ctx.message.attachments[0].url            # check for an pdf, call exception if none found
        except IndexError:
            print("Error: No attachments")
            await ctx.send("❎ **No attachments detected**")
        else:
            if url[0:26] == "https://cdn.discordapp.com":   # look to see if url is from discord
                r = requests.get(url, stream=True)
                pdfName = str(uuid.uuid4()) + '.pdf'      # uuid creates random unique id to use for pdf names
                with open(pdfName, 'wb') as out_file:
                    print('Saving PDF: ' + pdfName)
                    shutil.copyfileobj(r.raw, out_file)     # save pdf (goes to project directory)

                    pages = pdf2image.convert_from_path(pdfName, 200, poppler_path=r'A:/Documents/GitHub/Miura-Tester/poppler-21.11.0/Library/bin')

                    for i in range(len(pages)):
                        pages[i].save(f'A:/Documents/GitHub/Miura-Tester/pdf2image_output/page{i+1}.png', 'PNG')
                        file = discord.File(f"A:/Documents/GitHub/Miura-Tester/pdf2image_output/page{i+1}.png")
                        await ctx.send(file=file)

                for i in range(len(pages)):
                    os.remove(f"A:/Documents/GitHub/Miura-Tester/pdf2image_output/page{i+1}.png")
                os.remove(f"A:/Documents/GitHub/Miura-Tester/{pdfName}")
                await asyncio.sleep(2)
                await ctx.send(f"✅ **The document was successfully converted\nℹ Number of pages: **{i+1}")

@bot.command()
async def pdf2png_zip(ctx):
    async with ctx.typing():
        author = str(ctx.message.author)
        try:
            url = ctx.message.attachments[0].url            # check for an pdf, call exception if none found
        except IndexError:
            print("Error: No attachments")
            await ctx.send("❎ **No attachments detected**")
        else:
            if url[0:26] == "https://cdn.discordapp.com":   # look to see if url is from discord
                r = requests.get(url, stream=True)
                pdfName = str(uuid.uuid4()) + '.pdf'      # uuid creates random unique id to use for pdf names
                with open(pdfName, 'wb') as out_file:
                    print('Saving PDF: ' + pdfName)
                    shutil.copyfileobj(r.raw, out_file)     # save pdf (goes to project directory)

                    pages = pdf2image.convert_from_path(pdfName, 200, poppler_path=r'A:/Documents/GitHub/Miura-Tester/poppler-21.11.0/Library/bin')

                    for i in range(len(pages)):
                        pages[i].save(f'A:/Documents/GitHub/Miura-Tester/pdf2image_output/page{i+1}.png', 'PNG')
                    
                    shutil.make_archive(f'{author}_{i+1}pages', 'zip', 'A:/Documents/GitHub/Miura-Tester/pdf2image_output')
                    file = discord.File(f"{author}_{i+1}pages.zip")
                    await ctx.send(file=file)

                for i in range(len(pages)):
                    os.remove(f"A:/Documents/GitHub/Miura-Tester/pdf2image_output/page{i+1}.png")
                os.remove(f"A:/Documents/GitHub/Miura-Tester/{pdfName}")
                os.remove(f"A:/Documents/GitHub/Miura-Tester/{author}_{i+1}pages.zip")
                await asyncio.sleep(2)
                await ctx.send(f"✅ **The document was successfully converted\nℹ Number of pages: **{i+1}")

@bot.command()
async def removebg(ctx):
    async with ctx.typing():
        Name = "miura_removedbg.png"
        try:
            os.rename("miura_autosave",Name)
        except:
            os.remove(Name)
            os.rename("miura_autosave",Name)

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
        try:
            os.rename("miura_autosave",Name)
        except:
            os.remove(Name)
            os.rename("miura_autosave",Name)

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
        try:
            os.rename("miura_autosave",Name)
        except:
            os.remove(Name)
            os.rename("miura_autosave",Name)

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
        try:
            os.rename("miura_autosave",Name)
            shutil.move(Name,f"deepfryer_input/{Name}")
        except:
            os.remove(Name)
            os.rename("miura_autosave",Name)
            shutil.move(Name,f"deepfryer_input/{Name}")

        imageNormal = cv2.imread(Name)
        deepfryer.printFolders("deepfryer_input", "deepfryer_output")
        deepfryer.processArgs()
        deepfryer.fryImage(f"deepfryer_input/{Name}")
        deepfryer.badPosterize(imageNormal)
        deepfryer.folderCheck("deepfryer_input", "deepfryer_output")

        file = discord.File("deepfryer_output/miura_autosave-fry.png")
        await ctx.send(file=file)

# Role Selection
#@bot.command()
#async def role(ctx, name: str):
    #await member.add_roles(role)

@bot.listen()
async def on_message(message):
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


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=bot.version))
    print('Miura Tester Started')

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"⚠ **Error:** `{error}`")
    raise error

Token = os.environ["MiuraTesterToken"]
bot.run(Token)