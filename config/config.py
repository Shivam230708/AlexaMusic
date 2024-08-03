# Copyright (C) 2021-2022 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
Alexa is a Telegram Audio and video streaming bot 
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want.
"""

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "26050479"))
API_HASH = getenv("API_HASH", "d26cd1ad64530cfb5f90bab8717182a9"))

BOT_TOKEN = getenv("BOT_TOKEN", "7219265344:AAG40AeW2r_YEwnwyOclezL67JgkIu774EI"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://shiv230708:shivam@23@cluster0.0awjqhr.mongodb.net"))

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_CHANNEL_ID = int(getenv("LOG_CHANNEL_ID", "-1002236169695"))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "˹ Rᴏʏᴀʟ ✘ Mᴜsɪᴄ ˼")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5337517666").split()))

ASSISTANT_ID = int(getenv("ASSISTANT_ID", "7462156709"))

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

BOT_ID = getenv("BOT_ID")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://google.com/search/xhamster.com")

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Life_Changing_Movies")

SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+cOFKKAr4_DVjMjE9")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "11500"))

AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "False")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://google.com/search/xhamster.com")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1281122466184cafa5c42259671f77ae")

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "367311c34d5a4e8998ed5874b3fac0b8")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "2"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "7"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION1", "BQGNf68Al31IuZZlCCnIEUJJdz9BBSP4XGdYudUw5B7EWb9VsQ1kETRI45UZUBgGE6ASoDLSBHO-s5qsSxOEiDCfzxLeezHgdyDQz7aSJe8Fcn48EiPmNDtqAR7AeM9m5bJh9oEbRWQ-j3wzQpjkZtLlcJsNMbmicW7Rj3nYm7Me78RMP4nGTdgOP3mp2f0ghIrYDrOePQ-j6-GK4sL_auTzVkdflhXBVGDsD0HOyCR_oudX20vGVe0XdmJ676i0JfbgRubNLmle2-ii8HiJcGD_4kcZRQBLzsbneUrG_Ipj5dpOyDlKESWz042wH4FjkdHNMg9sBcf-SIHef-Y1YqHdJ2PgWwAAAAG8x3mlAA"))
STRING2 = getenv("STRING_SESSION2", "BQGNf68AjTR2t0M0B162qu758gC9cdsQhP9JoFDPywMdrpSRN-cqoBSvHzivsRxrlnr6o7vsxD2ZXDQfnNGYbO6fEOEvWtHn-mla5lBS9ZJD4jRm8YffbCcSoN4fuzcClfq7dlgrbf4rx8KdBDvSg58jYnBruwoKIEmGW8BOBlPK_R_0ro0tw0ilesL2JJXqkKuJaAqW_fb5icTkmli7HU5Oktshu9WV8AO88CAwyRCQJ5k9H8I8XqCzh0kiyuaQyzWl41NhyKoXzwaZx4hbJd90YUTvbIokSIE24SOcw4esccQOEX4Do2e3sFJsyuoi6KveD57fu16CiJd1Elzake9Zjd1l9AAAAAG8x3mlAA"))
STRING3 = getenv("STRING_SESSION3", "BQGNf68AE5gsSghONu-BXAUViNGPTcxFCCaMu6cRsfJc_BMS33ZhnQ87w7YYN7O15i0_34GUOT38q1_Ycon-v0eudAMzHDHnRE-Q4T8t_yXQdMtwpKPZdrgb_KI1qYfxbD1CYdXNmdCic7tAM0pr0arlCdroo3dRZYBTRn6p5QYiEPw8DpZiqz8aFQgs52efO9R_PXtUMKJNCfJk2St3M4iQRqiqbpKwFM4IUvNFlO8OQTeVHtsVT7TZKbpqtH81OrdZP4lWeBicFZ-vlQ5pCqXYiRnxIfjLA-B5svS00tWiFcolayys3a2u5RugOOMJb0NE9XrtaGsSblTHqMaFGmZdwZLIjgAAAAG8x3mlAA"))
STRING4 = getenv("STRING_SESSION4", "BQGNf68AKFIvzJyfq7aaovF397hG-SgtXPLwWDsZbl08bjulIKXhv0U8Ko3lbPe9L-uKaF2W9AbaonsG1ToaFGcMlhDParK8iRZlnTj_ge8e-C8dFNIauTioPL2My-HNFzN_ArtBO0ffisZ4HTyB-BjGbNdrSDfuQyBHFaUizW0JonlBg4wLD0Wf35difBtVzZVTIL29ITn6MXS7U9TGEAG0dX5RXjU_K9IAILdOIxCEo6Xf-QxR5rfmXPwRI-xPUE8RbbAvmNlHFLITc8Qsjy-l7X443i7KIdwk-caP2BeEuPM4llDr2MOo2foVmSQiteOvI6BUxN6URrZR8HqQCIs9V-jBbgAAAAG8x3mlAA"))
STRING5 = getenv("STRING_SESSION5", "BQGNf68As1rDOh6C5hv1UospjpH6N4UR1j9QUq8e0WJjN8htMfTYt5YY6H0x9juWpOr9XB8sFlxP6s4kib4IxS3b5yJQUZCZC2k_0E7qCrpejL0xf92iNuxAjj2E-b9HnVBTuyOQzaGJubwKz8XyVwp_Om4c5gPlzovAPcb0ildk4laXTlHuQkMhqFTmJ1nc95aJoRDTwzTYKK2gL3pQGRlzJqVyj1BrpM-tb6vD8McuTKNZueuUTNr5PwRMxMXmuRcN9kFzPhytCkAJWo_3FKLnuzgIeawEAMpr_Zokb-S51OQ8-_RZCGWUFCU-f_3mvVfHo6doHlOQng_YsuPgjLSXnnab3AAAAAG8x3mlAA"))

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/d593c6064ff7657d0c714.jpg"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "assets/Ping.jpeg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "assets/Global.jpeg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "assets/Stats.jpeg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "assets/Audio.jpeg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "assets/Video.jpeg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "assets/Stream.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )


if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()
