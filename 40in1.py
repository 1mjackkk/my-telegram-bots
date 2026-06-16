# ╔══════════════════════════════════════════════════════════════════╗
# ║        𝐆ᴇɴᴏs 𝐁𝐀𝐀𝐏 • 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐒𝐘𝐒𝐓𝐄𝐌 • 𝐕𝐈𝐏 𝐄𝐃𝐈𝐓𝐈𝐎𝐍 🦋          ║
# ║        𝐏𝐎𝐖𝐄𝐑𝐄𝐃 & 𝐏𝐑𝐎𝐓𝐄𝐂𝐓𝐄𝐃 𝐁𝐘 𝐆ᴇɴᴏs 𝐁𝐀𝐀𝐏 👑               ║
# ║        39 FILES → 1 FILE MEGA MERGE COMPLETE ✅                  ║
# ╠══════════════════════════════════════════════════════════════════╣
# ║  FEATURES: 50+ NC Types | 10+ Spam Types | GC PFP | Swipe      ║
# ║  Sticker Spam | Multi-Group | Auto Reply | Slide | Raid         ║
# ║  PREFIXES: ! . / # £ _ - & ~ ? (sabhi kaam karte hain)         ║
# ╚══════════════════════════════════════════════════════════════════╝

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# STANDARD LIBRARY IMPORTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
import asyncio
import json
import os
import io
import random
import signal
import sys
import time
import logging
from collections import deque
from datetime import datetime
from typing import Dict, Set, List, Optional

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# THIRD-PARTY IMPORTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TELEGRAM IMPORTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from telegram.error import RetryAfter, TimedOut, NetworkError, BadRequest, Forbidden
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is Alive!"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Apne main bot code ke theek pehle ise call karein
keep_alive()

# Yahan aapka baki ka Telegram Bot ka code aayega (jaise bot.infinity_polling())


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LOGGING SETUP — minimal noise
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
logging.basicConfig(
    format="%(asctime)s [GENOS] %(levelname)s: %(message)s",
    level=logging.WARNING
)
logger = logging.getLogger("GenosV1")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚙️ CONFIGURATION — apne tokens & owner yahan daalo
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OWNER_ID = int(os.getenv("OWNER_ID", "8817232625"))

BOT_TOKENS = [
    t.strip() for t in os.getenv("BOT_TOKENS", "").split(",") if t.strip()
] or [
    # Yahan apne bot tokens daalo (default list):
    "8829316985:AAGsJkJObl9vM_pj7pFhtpXl3yR1cjT_b5U",
"8896990355:AAFT-vQVRaIwk3GpJfkgFw_1F8if89VWfgs",
"8838813806:AAFbLYRTRa5_ValNbdLvVOihArHgvLbJpXw",
"8987358424:AAHFzls_blmA3_RqfrUlVyuM22xFiULUKN8",
"8847985211:AAE77_P4q0pkg56IrT9H-jWp4rANCHLn9yk",
"8560090942:AAH-HSJPDlcud89JrLdLnY7U8bF1m75vQ8o",
"8976611993:AAHqlNGV-K-CLrpC7acUc2CHofm2khsvDTc",
"8955906866:AAH9c-rNjRFtsjFJj-2xak6nH6UZBpWxAoY",
"8600087311:AAG3qrJBtvaR7Si0Nifeaq9bFMqbQbEq7n0",
"8783234093:AAHmtscIrRbavuWeqhUSyCfvippKb4IYT3o"
]

# Multi-prefix system — ye sabhi prefix kaam karte hain!
PREFIXES = ('!', '.', '/', '#', '£', '_', '-', '&', '~', '?')

# Persistent files
SUDO_FILE = "sudo_users.json"
RIGHTS_FILE = "rights.json"
STICKER_FILE = "stickers.json"
GC_PHOTO_FILE = "gc_photo.jpg"

# Delays
NC_DELAY = 0.05
SPAM_DELAY = 0.1
SWIPE_DELAY = 0.15
RAID_DELAY = 0.15
FLOOD_DELAY = 0.05

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎨 EMOJI LISTS — saari files se merge ki gayi
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MAIN_EMOJIS = ["🖤","💢","♻️","❤️","🪽","🤍","🛸","💛","🌷","🩵","👑","🤎","🌙","🩷","🎀","🕷️","🪐","💚","💨","🩶","😈"]
HEART_EMOJIS = ["(❤️)࿐","(🩷)࿐","(🧡)࿐","(💛)࿐","(💚)࿐","(💙)࿐","(🩵)࿐","(💜)࿐","(🖤)࿐","(🩶)࿐","(🤎)࿐","(🤍)࿐","(💞)࿐","(💕)࿐","(💗)࿐","(💖)࿐","(❤️‍🔥)࿐"]
FLAG_EMOJIS = ["🇮🇳","🇵🇰","🇧🇩","🇺🇸","🇬🇧","🇷🇺","🇨🇳","🇯🇵","🇰🇷","🇩🇪","🇫🇷","🇧🇷","🇦🇺","🇨🇦","🇦🇪","🇸🇦","🇹🇷","🇮🇱","🇮🇹","🇪🇸","🇨🇾","🇦🇨","🇦🇩","🇦🇫","🇦🇬","🇦🇴","🇦🇸","🇧🇦"]
MOON_EMOJIS = ['🌙','🌛','🌜','🌝','🌚','🌕','🌖','🌗','🌘','🌑','🌒','🌓','🌔','✨','⭐','🌟','💫','🌠']
FLOWER_EMOJIS = ["🌹","🌺","🌸","🌼","🌻","🌷","🪷","💐","🥀","🏵️"]
EXONC_TEXTS = ["➛「🌹」","➛「🌼」","➛「🌻」","➛「🪻」","➛「🏵️」","➛「💮」","➛「🌸」","➛「🪷」","➛「🌷」","➛「🌺」","➛「🥀」","➛「💐」","➛「🍁」","➛「☘️」"]
NCEMO_EMOJIS = ["──(🩷)──ᴅᴏɢ","──(🤍)──ᴅᴏɢ","──(🩶)──ᴅᴏɢ","──(🖤)──ᴅᴏɢ","──(🤎)──ᴅᴏɢ","──(💜)──ᴅᴏɢ","──(💙)──ᴅᴏɢ","──(🩵)──ᴅᴏɢ","──(💚)──ᴅᴏɢ","──(💛)──ᴅᴏɢ","──(🧡)──ᴅᴏɢ","──(❤️)──ᴅᴏɢ"]
EMOJI_NC_EMOJIS = ["🐧","🦭","🦈","🫍","🐬","🐋","🐳","🐟","🐠","🐡","🦐","🦞","🦀","🦑","🐙","🪼","🦪","🪸","🫧","🦂"]
NC1_EMOJIS = ["💐","🌹","🥀","🌺","🌷","🪷","🌸","💮","🏵️","🪻","🌻","🌼","🍂","🍁","🌱","🍃","☘️","🍀"]
NC2_EMOJIS = ["🪽","🪶","🐦","🐦‍⬛","🐓","🐔","🐣","🐤","🐥","🦅","🦉","🦜","🕊️","🦤","🦢","🦆","🪿","🦩","🦚","🐦‍🔥","🦃"]
NC3_EMOJIS = ["💠","🇦🇶","🇦🇷","🇦🇸","🇦🇹","🇦🇺","🇦🇼","🇦🇽","🇦🇿","🇧🇦","🇧🇧","🇧🇩","🇧🇪","🇧🇫","🇧🇬","🇧🇭","🇧🇮","🇧🇯","🇧🇱","🇧🇲","🇧🇳","🇧🇴","🇧🇶","🇧🇷"]
NC4_EMOJIS = ["🏔️","🌋","☃️","🏝️","🏖️","🌊","🌬️","❄️","🌀","🌪️","⚡","☔","💧","☁️","🌨️","🌧️","🌩️","⛈️","🌦️","🌥️","⛅","🌤️","☀️","🌞","🌝","🌚","🌜","🌛","🌙","⭐","🌟","✨","🪐"]
NC5_EMOJIS = ["🪔","🪅","🪩","🎐","🎏","🎎","🧨","🎨","💸","💵","💴","💶","💷","💳","💰","🧿","🪬","📿","♥️","🩶","🩵","🩷","🤍","🖤","🤎","❤️","🧡","💛","💚","💙","💜"]
KNC_EMOJIS = ["😆","😂","🤣","🥰","😍","😌","😏","🤤","😋","😛","😝","😜","🤪","🫪","😔","🥺","😬","😑"]
ANC_EMOJIS = ["🌈","☔","⚡","🌪️","🌀","🏖️","🏝️","🌊","🌬️","❄️","💧","🌨️","☁️"]
FNC_EMOJIS = ["❤️","🧡","💛","💚","🩵","💙","💜","🤎","🖤","🩶","🤍","🩷"]
FUCK_HEART_EMOJIS = ["(❤️)࿐","(🩷)࿐","(🧡)࿐","(💛)࿐","(💚)࿐","(💙)࿐","(🩵)࿐","(💜)࿐","(🖤)࿐","(🩶)࿐"]
FUCK_FLAG_EMOJIS = ["🇨🇾࿐","🇦🇨࿐","🇦🇩࿐","🇦🇪࿐","🇦🇫࿐","🇦🇬࿐","🇦🇴࿐","🇦🇸࿐","🇦🇺࿐","🇧🇦࿐","🇧🇩࿐"]
RAINBOW_COLORS = ["🔴","🟠","🟡","🟢","🔵","🟣","⚫","⚪","🟤","🔶","🔷","🔸","🔹"]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📝 NC MESSAGE PATTERNS — sabhi files se collect kiye
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BASIC_NC_MSGS = [
    "{t} ᴛᴍᴋᴄ 💢","{t} ᴛᴍᴋʟ 💢","{t} ᴛʙᴋᴄ 💢","{t} ᴛʙᴋʟ 💢",
    "{t} ɢᴀʀᴇᴇʙ 💢","{t} ʀɴᴅʏ 💢","{t} ᴄʜᴜᴅᴀᴋᴋᴀᴅ 💢","{t} ᴘɪʟʟᴇ 💢",
    "{t} ʙᴄ 💢","{t} ᴍᴋʟ 💢","{t} ʜɪᴊᴅᴇ 💢","{t} ᴍᴄ 💢","{t} ʙꜱᴅᴋ 💢",
    "{t} ꜱʟᴀᴠᴇ 💢","{t} ᴅᴀʟʟɪᴛ 💢","{t} ɢᴜʟᴀᴍ 💢","{t} ʙɪᴛᴄʜ 💢",
    "{t} ʙʜɪᴋᴀʀɪ 💢","{t} ᴋɪɴɴᴇʀ 💢","{t} ᴄʜᴜᴛɪʏᴀ 💢","{t} ɴᴀʟᴀʏᴀᴋ 💢",
    "{t} Cʜᴀᴘᴀʟ Kʜᴀ Mᴄ 🤢🤮","{t} Gᴜʟᴀᴍ Kᴇ ʟᴀᴅᴋᴇ Tᴍᴋᴄ 😂🔥",
    "{t} Sɪʟᴀɪ Wᴀʟʏ Kᴇ ʟᴀᴅᴋᴇ Tᴇʀɪ ᴍᴀᴀ Kᴀ ʙʜᴏsᴅᴀ Sɪʟ Dᴜ 🧵",
    "{t} Tᴇʀɪ Mᴀᴀ Gʏᴍɴᴀsᴛɪᴄs Kʀᴛᴇ Cʜᴜᴅɪ 🤸🏻🔥",
]
HINDI_NC_PATTERNS = [
    "{t} चुडाकड़ ⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖","{t} रैंडी ˖ ࣪ ꉂ🗯˙🫐⃟.꩜‹—",
    "{t} गरीब ⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖","{t} चमार˖ ࣪ ꉂ🗯˙🫐⃟.꩜‹—",
    "{t} भेंगे⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖","{t} रैंडी के बच्चे˖ ࣪ ꉂ🗯˙🫐⃟.꩜‹—",
    "{t} गुलाम⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖","{t} गुलामी कर˖ ࣪ ꉂ🗯˙🫐⃟.꩜‹—",
    "{t} चुदाई केंद्र⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖","{t} नांगा नाच कर˖ ࣪ ꉂ🗯˙🫐⃟.꩜‹—",
    "{t} पापा बोल 𝐆ᴇɴᴏs को⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖","{t} तेरी मां नंगी करू˖ ࣪ ꉂ🗯˙🫐⃟.꩜‹—",
    "{t} छक्के⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖","{t} भोसड़ी के˖ ࣪ ꉂ🗯˙🫐⃟.꩜‹—",
]
URDU_NC_PATTERNS = [
    "{t} ٹی ایم کے بی࣪ ִֶָ☾.ִ ࣪𖤐","{t} تیری ماں رندی࣪ ִֶָ☾.ִ ࣪𖤐",
    "{t} چوداکڑ 𓍢ִႋ🌷͙֒ᰔᩚ","{t} گلام ࣪ ִֶָ☾.ִ ࣪𖤐",
    "{t} رنڈی𓍢ִႋ🌷͙֒ᰔᩚ","{t} گلامی کے آر𓍢ִႋ🌷͙֒ᰔᩚ",
    "{t} رنڈی پوترا 𓍢ִႋ🌷͙֒ᰔᩚ","{t} چکے ִ ࣪𖤐",
]
BENGALI_NC_PATTERNS = [
    "{t} শালা °❀.ೃ࿔*ꫂ❁","{t} গরিবꫂ❁°❀.ೃ࿔*",
    "{t} ককার ꫂ❁°❀.ೃ࿔*","{t} দাসꫂ❁°❀.ೃ࿔*",
    "{t} নগ্নꫂ❁°❀.ೃ࿔*","{t} তুই হারামজাদাꫂ❁°❀.ೃ࿔*",
    "{t} এলোমেলো ꫂ❁°❀.ೃ࿔*","{t} শালা কেন্দ্রꫂ❁°❀.ೃ࿔*",
]
BIHARI_NC_PATTERNS = [
    "{t} भोसड़ी के बा⋆꙳^̩̩͙❅*̩̩͙‧͙","{t} गरीब⋆꙳^̩̩͙❅*̩̩͙‧͙",
    "{t} गुलाम⋆꙳^̩̩͙❅*̩̩͙‧͙","{t} रे हरामी₊˚ʚ ᗢ₊˚✧ ﾟ.",
    "{t} कमबख्त सेंटर के बा₊˚ʚ ᗢ₊˚✧ ﾟ.","{t} नंगा हो गइल बा⋆꙳^̩̩͙❅*̩̩͙‧͙",
]
ENGLISH_NC_PATTERNS = [
    "{t} 🅱🅻🅾🅾🅳🆈 🅷🅴🅻🅻.𖥔 ݁ ˖ִ🛸༄˖°.",
    "{t} 🅼🅾🆃🅷🅴🆁🅵🆄🅲🅺🅴🆁🌊⋆｡ 𖦹°.🐚⋆❀˖°🫧",
    "{t} 🅱🅸🆃🅲🅷 🆂🅾🅽.𖥔 ݁ ˖ִ🛸༄˖°.",
    "{t} 🆂🅻🅰🆅🅴🌊⋆｡ 𖦹°.🐚⋆❀˖°🫧",
    "{t} 🅵🆄🅲🅺🄽🄶 🅲🅴🅽🆃🆁🅴.𖥔 ݁ ˖ִ🛸༄˖°.",
    "{t} 🆂🅾🅽 🅵🆄🅲🅺🅴🅳 🅼🅾🅼🌊⋆｡ 𖦹°.🐚⋆❀˖°🫧",
]
EMOJI_NC_PATTERN = "{t} 𝙏𝙈𝙆𝙁𝘽 <⋆.ೃ࿔*:･{e}⋆.ೃ࿔*:･>"
NC1_PATTERN = "˚⊱{e}⊰˚{t} 𝙍𝙉𝘿𝙔 𝘾𝙃𝙄𝙉𝙉𝘼𝙍 𝙏𝙈𝙆𝘾 𝙈𝙄𝙀 𝙈𝘼𝙂𝙂𝙄𝙀 𝘽𝙉𝘼𝙐𝙂𝘼 𝘽𝙎𝘿𝙆 <˚⊱⊰˚{e}˚⊱⊰˚>"
NC2_PATTERN = "{t} 𝙏𝙈𝙆𝘽 𝙈𝙄𝙀 𝙈𝙐𝙏 𝘿𝙐 ? 𝙏𝘽𝙆𝘾 𝙈𝙄𝙀 𝙇𝘼𝘼𝙏 𝙂𝙐𝙇𝘼𝙈𝙄 𝙆𝙍 ¡! <ִֶָ𓂃 ࣪˖ ִֶָ{e}ִֶָ་༘࿐>"
NC3_PATTERN = "{t} 𝙍𝙉𝘿𝙔𝙆𝙀 𝙇𝘼𝘿𝙆𝙀 𝘽𝘼𝘼𝙋 𝙆𝙀 𝙎𝘼𝙈𝙉𝙀 𝙃𝘼𝙒𝘼𝘽𝘼𝙕𝙄 𝙆𝙍𝙀𝙂𝘼 𝘾𝙃𝙐𝘿 𝘼𝘽 ! <{e}>"
NC4_PATTERN = "{t} तू हिजड़ा रेंडी के बच्चे छिनाल <{e}>"
NC5_PATTERN = "{t} 🩷गुलाबी चूत वाला💘 <𓂃˖˳·˖ ִֶָ ⋆{e}⋆ ִֶָ˖·˳˖𓂃 ִֶָ>"
KNC_PATTERN = "{t} <{e}> 🫯💢🫯💢🫯💢🫯💢🫯💢🫯💢🫯💢🫯💢🫯💢🫯💢🫯💢🫯💢🫯💢🫯💢🫯"
ANC_PATTERN = "{t} <{e}> 🍃🪢📯🍃📯🪢🍃🪢📯🍃🪢📯🍃🪢📯🍃🪢📯🍃🪢📯🍃🪢📯🍃🪢📯🍃"
FNC_PATTERN = "{t} 𝘾𝙃𝙐𝘿𝘼𝙄 𝘼𝙍𝘾 <{e}> જ⁀➴❤️‍🔥જ⁀➴🎀જ⁀➴🤍જ⁀➴💓જ⁀➴❣️જ⁀➴🩵જ⁀➴💚જ⁀➴❤️"
MOON_NC_MSGS = [
    "🌑 {t} 𝘛𝘌𝘙𝘐 मां 𝘋𝘈𝘕𝘐 𝘋𝘈𝘕𝘐𝘌𝘓𝘚><🌑",
    "🌔 {t} 𝘛𝘌𝘙𝘐 मां 𝘓𝘌𝘟𝘐 𝘓𝘜𝘕𝘈><🌔",
    "🌕 {t} 𝘛𝘌𝘙𝘐 मां 𝘗𝘙𝘐𝘠𝘈 𝘉𝘏𝘈𝘉𝘏𝘐><🌕",
    "🌙 {t} 𝘛𝘌𝘙𝘐 मां 𝘋𝘐𝘙𝘛𝘠 𝘛𝘐𝘕𝘈><🌙",
]
FLAG_NC_MSGS = [
    "{t} 🇨🇳𝐌ᴀᴅᴀʀᴄʜᴏ𝐃🇨🇳","{t} 🇨🇦𝐊ᴀɴᴊᴀ𝐑🇨🇦",
    "{t} 🇩🇪𝐑ᴀɴᴅ𝐈🇩🇪","{t} 🇮🇳𝐇ᴀ𝐀ʀᴀᴍᴢᴀᴅᴀ🇮🇳",
    "{t} 🇮🇲𝐓ᴇʀɪᴍᴀᴀᴋɪ𝐂ʜᴜᴛ🇮🇲","{t} 🇰🇵𝐁ɪᴛᴄʜ🇰🇵",
    "{t} 🇺🇸𝐂ʜᴜᴅᴋᴀ𝐃🇺🇸",
]
CURLY_NC_MSGS = [
    "{{ Tᴍᴋᴄ ! {t} Tᴍᴋᴄ ! }}","{{-Tᴍᴋᴄ ! {t} Tᴍᴋᴄ !-}}",
    "{{★Tᴍᴋᴄ ! {t} Tᴍᴋᴄ !★}}","{{🔥Tᴍᴋᴄ ! {t} Tᴍᴋᴄ !🔥}}",
    "{{🔱Tᴍᴋᴄ ! {t} Tᴍᴋᴄ !🔱}}","{{✨Tᴍᴋᴄ ! {t} Tᴍᴋᴄ !✨}}",
    "{{🥀Tᴍᴋᴄ ! {t} Tᴍᴋᴄ !🥀}}",
]
TIME_NC_MSGS = [
    " {t} Tɪᴍᴇ Is Oᴠᴇʀ 12:382:229"," {t} Tᴇʀɪ Mᴀᴀ Kᴀ Bʜᴏsᴅᴀ Sɪʟ Dᴜɴ 12:382:230",
    " {t} Tᴇʀᴀ Bᴀᴀᴘ Nᴀɢᴀsᴀᴋɪ 12:382:231"," {t} Tᴇʀɪ Bᴇʜɴ Kɪ Cʜᴜᴛ Mᴇ Gʜᴀᴅɪ 12:382:232",
    " {t} Tɪᴍᴇ Tᴏ Dɪᴇ Mᴄ 12:382:233","12:382:234 {t} Tᴇʀɪ Mᴀᴀ Cʜᴜᴅ Gᴀʏɪ",
]
TMKC_NC_MSGS = [
    "{{ Tᴍᴋᴄ ! {t} Tᴍᴋᴄ ! }}","{{★Tᴍᴋᴄ ! {t} Tᴍᴋᴄ !★}}",
    "{{🔥Tᴍᴋᴄ ! {t} Tᴍᴋᴄ !🔥}}","{{🔱Tᴍᴋᴄ ! {t} Tᴍᴋᴄ !🔱}}",
]
FLOWER_NC_MSGS = [
    "𝜗𝜚⋆₊🍁˚{t} Sʟᴜᴛ Mᴀᴀ ᴋᴇ Lᴀᴅᴋᴇ ",
    "𝜗𝜚⋆₊🌱˚{t} Sʟᴜᴛ Mᴀᴀ ᴋᴇ Lᴀᴅᴋᴇ ",
    "𝜗𝜚⋆₊🌿˚{t} Sʟᴜᴛ Mᴀᴀ ᴋᴇ Lᴀᴅᴋᴇ ",
    "𝜗𝜚⋆₊🍃˚{t} Sʟᴜᴛ Mᴀᴀ ᴋᴇ Lᴀᴅᴋᴇ ",
    "𝜗𝜚⋆₊☘️˚{t} Sʟᴜᴛ Mᴀᴀ ᴋᴇ Lᴀᴅᴋᴇ ",
]
SPACE_NC_MSGS = [
    "🌀 {t} SON OF BITCH 🌀","🌀 {t} ASS HOLE 🌀","🌀 {t} PIGGY 🌀",
    "🌀 {t} FUCK YOU 🌀","🌀 {t} MOTHER FUCKER 🌀","🌀 {t} SLAVE 🌀",
    "🌀 {t} BLODDY WHORE 🌀","🌀 {t} SON OF HOE 🌀",
]
FUL_NC_MSGS = [
    "𝜗𝜚⋆₊🍁˚{t} 𝙏𝙀𝙍𝙄 𝙈𝘼 𝙆𝙊 𝘾𝙃O𝘿𝙆𝙀 𝘿𝙐𝙎𝙏𝘽𝙄𝙉 𝙈𝙀 𝙁𝙀𝙆𝘿𝙐𝙉𝙂𝘼 ",
    "𝜗𝜚⋆₊🌱˚{t} 𝙏𝙀𝙍𝙄 𝙈𝘼 𝙆𝙊 𝘾𝙃O𝘿𝙆𝙀 𝘿𝙐𝙎𝙏𝘽𝙄𝙉 𝙈𝙀 𝙁𝙀𝙆𝘿𝙐𝙉𝙂𝘼 ",
    "𝜗𝜚⋆₊🌿˚{t} 𝙏𝙀𝙍𝙄 𝙈𝘼 𝙆𝙊 𝘾𝙃O𝘿𝙆𝙀 𝘿𝙐𝙎𝙏𝘽𝙄𝙉 𝙈𝙀 𝙁𝙀𝙆𝘿𝙐𝙉𝙂𝘼 ",
]
GENOSNC_MSGS = [
    "⚡ {t} GENOS BHAGWAN ABU ⚡","🔥 {t} Tᴇʀɪ Mᴀᴀ Kɪ Cʜᴜᴛ Mᴇ Aᴀɢ 🔥",
    "👑 {t} GENOS BHAGWAN Bᴀᴀᴘ Hᴀɪ Tᴇʀᴀ 👑","💀 {t} Kʜᴀᴍᴏsʜɪ Sᴇ Cʜᴜᴅ Jᴀ 💀",
    "💥 {t} GENOS BHAGWAN Sᴇ Pᴀɴɢᴀ Mᴀᴛ Lᴇ 💥","🚀 {t} Tᴇʀɪ Bᴇʜɴ Kɪ Cʜᴜᴛ Mᴇ Rᴏᴄᴋᴇᴛ 🚀",
]
RAID_TEXTS = [
    "𓂃˖˳·˖ ִֶָ ⋆[HIJDA]⋆ ִֶָ˖·˳˖𓂃","𓂃˖˳·˖ ִֶָ ⋆[GAY]⋆ ִֶָ˖·˳˖𓂃",
    "𓂃˖˳·˖ ִֶָ ⋆[R9D]⋆ ִֶָ˖·˳˖𓂃","𓂃˖˳·˖ ִֶָ ⋆[CHAMAR]⋆ ִֶָ˖·˳˖𓂃",
    "𓂃˖˳·˖ ִֶָ ⋆[GAREEB]⋆ ִֶָ˖·˳˖𓂃","𓂃˖˳·˖ ִֶָ ⋆[LND LE]⋆ ִֶָ˖·˳˖𓂃",
    "𓂃˖˳·˖ ִֶָ ⋆[तेरी मा रंडी]⋆ ִֶָ˖·˳˖𓂃","𓂃˖˳·˖ ִֶָ ⋆[TMKC]⋆ ִֶָ˖·˳˖𓂃",
    "𓂃˖˳·˖ ִֶָ ⋆[TBKC]⋆ ִֶָ˖·˳˖𓂃","𓂃˖˳·˖ ִֶָ ⋆[BAUNA]⋆ ִֶָ˖·˳˖𓂃",
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 💬 SPAM/REPLY PATTERNS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPLY_MSGS = [
    "{t} Tᴇʀɪ ᴍᴀᴀ ɢᴜʟᴀᴍ ʜ ʙᴇᴛᴇ🐣","{t} Cᴜᴅ Cᴜᴅ Cᴜᴅ -!🩴🔥",
    "Aʟᴏᴏ Kʜᴀᴋᴇ {t} Tᴇʀɪ ᴍᴏᴍ Cᴏᴍ Qᴜᴇᴇɴ 👑♥️","{t} Hɪᴊᴅᴀ Tᴇʀᴇ Bᴀᴀᴘ ᴋɪ Cʜᴜᴛ🤳🏻",
    "{t} Tᴇʀᴇ Bᴀᴀᴘ Kɪ ʙᴋʙ🔥✨","{t} Tᴜ ᴋʀᴇɢᴀ Sᴘᴀᴍ Hᴀssɪ🔃💠",
    "{t} Tᴇʀɪ Bʜᴇɴ Cʜᴏᴅᴇ Dɪɴᴀsᴀᴜʀ🦖😈","{t} Kᴜᴛɪʏᴀ Kᴇ ʟᴀᴅᴋᴇ🌷😭",
    "{t} Tᴇʀᴀ ʙᴀᴀᴘ Tᴇʀɪ ᴍᴀᴀ ᴄʜᴏᴅᴇ Bʙᴄ Bᴀɴᴋᴇ😨♥️",
    "{t} Sɪʟᴀɪ Wᴀʟʏ ᴋᴇ ʟᴀᴅᴋᴇ Tʀʏ Mᴀᴀ ᴋᴀ ʙʜᴏsᴅᴀ Sɪʟ ᴅᴜ? 💀🥵",
    "{t} Eᴠᴇʀʏᴛʜɪɴɢ Is Tᴇᴍᴘᴏʀᴀʀʏ Bᴜᴛ Tʀɪ Cʜᴜᴅᴀɪ Is ᴘᴇʀᴍᴀɴᴇɴᴛ 🦠",
    "{t} Kᴜᴛɪʏᴀ Kᴇ ʙʜᴏsᴅᴇ Kɪ ᴀᴜʟᴀᴅ😈","{t} ʜɪᴊᴅᴀ ʜ ᴛᴜ ɢʀᴇᴇʙ💮🥀",
]
SPAM_MSGS = [
    "✝ 𝐆ᴇɴᴏs ᴋɪ ᴊᴀɪ ʜᴏ {t} ᴋɪ ᴍᴀᴀ ᴄʜᴜᴅɪ ʙᴀᴅɪ 💗",
    "⚡ {t} ᴛᴇʀɪ ᴍᴀᴀ ᴋɪ ᴄʜᴜᴛ ᴍᴇɪɴ ʙᴏᴍʙ 💣",
    "🔥 {t} ɢᴀɴᴅᴜ ʙᴀᴄʜᴀ ᴛᴇʀɪ ᴍᴀᴀ ᴋɪ ᴄʜᴜᴛ 🍆",
    "💀 {t} ᴛᴇʀɪ ᴍᴀᴀ ʀᴀɴᴅɪ ʙᴀᴢᴀᴀʀ ᴋɪ 🛒",
    "🐶 {t} ᴋᴜᴛᴛᴇ ᴋᴇ ᴘɪʟʟᴇ ᴛᴇʀɪ ᴍᴀᴀ ᴋɪ ᴄʜᴜᴛ 🦴",
    "⚔️ {t} ᴛᴇʀɪ ᴍᴀᴀ ᴋᴏ ꜱᴀʙ ᴄʜᴏᴅᴇɴɢᴇ 🗡️",
]
SPAM1_PATTERN = "🎐𓍼ֶ˖ܓ  ( < {t} > )  की अम्मी-जान का रेपिस्ट हू ˚.🧋>"
SPAM2_PATTERN = ("{t} - 𝑻𝑬𝑹𝑰 𝑴𝑨 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑷𝑬 𝑩𝑳𝑨𝑫𝑬 𝑺𝑬 𝑲𝑨𝑨𝑻 𝑨𝑷𝑵𝑨 𝑵𝑨𝑴𝑬 𝑳𝑰𝑲𝑯𝑼𝑵𝑮𝑨 𓍼🎋𓍼\n") * 8
SPAM3_PATTERN = ("࿐💞➳{t} 𝐓ᴇʀɪ 𝐌∆∆ 𝐂ʜ⭕ᴅ 𝐃∆ʟᴇɴ𝐆ᴇ ࿐\n") * 8
SPAM4_PATTERN = ("𓆩{t}𓆪 𝐈 #𝗙ꪊᴄᴋ ʏᴏᴜʀ 𝐌ᴏᴍᴍʏ ⃟🌷꙰⃟𓆩\n\n") * 8
FUCK_TEXTS = {
    1: "──(😈)──нιנ∂є", 2: "──(🥶)──ƒυ¢к уσυ",
    3: "──(🤢)──тєяα вααρ кєηтσ", 4: "──(🫩)──мαα ¢нυ∂α",
    5: "──(🥴)──кαмzσя нαι тυ",
}

# Slide messages
SLIDE1_MSGS = [
    "𝐓ᴍᴋʙ 𝐑ɴᴅʏ ᴋᴇ 𝐋ᴀᴅᴋᴇ 😈🖕🏻",
    "𝐓ᴇʀɪ ᴍᴀᴀ ᴍᴀʀ ɢʏɪ ¿😆",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ʜᴜᴍᴇꜱʜᴀ ᴍᴜᴊʜꜱᴇ ʜɪ ᴋʏᴜ चुडती है ¡! 😡",
    "𝐃ᴇᴋʜ ᴀᴀᴊ ᴛᴇʀɪ 𝐌ᴀᴀ ᴋᴀ ɴᴀɴɢᴀ ᴅᴀɴᴄᴇ ᴅɪᴋʜᴀᴜ ! 🩰",
]
SLIDE2_MSGS = [
    "𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐆ᴜʟᴀʙɪ 𝐂ʜᴜᴛ ᴍɪᴇ 𝐌ᴜᴛ ᴋʀ ʙʜᴀɢ ᴊᴀᴜɢᴀ 𝐁ꜱᴅᴋ ! 😆",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ᴄʜᴏᴅɴᴇ ᴀʀʜᴀ ʜᴜ ʀᴜᴋ ᴡʜɪ ɢᴜʟᴀᴍ ! 😾",
    "𝐓ᴇʀɪ ᴍᴀᴀ ᴋɪ ᴄʜᴜᴛ ᴍɪᴇ ᴍᴀɢɢɪᴇ ʙɴᴀ ᴋʀ ᴍᴜᴛʜ ʙʜᴀʀ ᴅᴜɢᴀ ! 😆",
    "𝐂ʜʟ ɢᴜʟᴀᴍ ɢᴜʟᴀᴍɪ ᴋʀ ! 😾",
]
SLIDE3_PATTERN = "{t} જ⁀➴🍃જ⁀➴😆જ⁀➴❤️"
SWIPE_MSGS = [
    "{t} ---PILLE Uth ","Aʟᴏᴏ Kʜᴀᴋᴇ {t} Kɪ Mᴀ Cʜᴏᴅ Dᴜɴɢᴀ!",
    "{t} Cʜᴜᴅᴀ q chote🦖🪽","{t} CUDKE MARGYA Tu",
    "{t} ᴋᴜᴛᴛᴇ sipahi polish kr 😋","{t} ᴄʜᴜᴅ ᴋᴇ ᴘᴀɢᴀʟ ʜᴏɢᴀʏᴀ",
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📊 GLOBAL STATE — sabhi bots share karte hain
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
applications: List = []          # Sabhi bot Application objects
bots: List = []                   # Sabhi bot objects
all_groups: Set[int] = set()      # Sabhi known groups

# Sudo/rights users — persistent
if os.path.exists(SUDO_FILE):
    try:
        SUDO_USERS: Set[int] = set(json.load(open(SUDO_FILE)))
    except Exception:
        SUDO_USERS = set()
else:
    SUDO_USERS = set()

# Sticker storage
if os.path.exists(STICKER_FILE):
    try:
        USER_STICKERS: dict = json.load(open(STICKER_FILE))
    except Exception:
        USER_STICKERS = {}
else:
    USER_STICKERS = {}

# GC photo storage
GC_PHOTO_FILE_ID: Optional[str] = None

# Slide reply text (passive — reply to everyone)
slide_reply_text: Optional[str] = None

# Task dictionaries — har type ke active tasks track karte hain
nc_tasks: Dict[int, List] = {}
spam_tasks: Dict[int, List] = {}
reply_tasks: Dict[int, List] = {}
slide_tasks: Dict[int, List] = {}
swipe_tasks: Dict[int, List] = {}
pswipe_tasks: Dict[int, List] = {}
raid_tasks: Dict[int, List] = {}
sticker_tasks: Dict[int, List] = {}
gc_tasks: Dict[int, List] = {}
multinc_tasks: Dict[int, List] = {}
multispam_tasks: Dict[int, List] = {}
autoreply_data: Dict[int, dict] = {}  # {chat_id: {trigger: reply}}
vanitas_tasks: Dict[int, List] = {}

# Per-chat delay settings
chat_delays: Dict[int, float] = {}
chat_threads: Dict[int, int] = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔐 PERMISSION HELPERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def save_sudo():
    with open(SUDO_FILE, "w") as f:
        json.dump(list(SUDO_USERS), f)

def save_stickers():
    with open(STICKER_FILE, "w") as f:
        json.dump(USER_STICKERS, f)

def is_auth(uid: int) -> bool:
    return uid == OWNER_ID or uid in SUDO_USERS

UNAUTH_MSG = "ʙᴏᴛ ᴜꜱᴇ ᴋᴀʀɴᴇ ᴋɪ ᴀᴜᴋᴀᴀᴛ ɴʜɪ ʜᴀɪ ᴛᴇʀɪ 🔒 — sudo lo pehle!"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔧 PREFIX PARSER — sabhi prefixes ko parse karta hai
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def parse_cmd(text: str):
    """
    Koi bhi prefix ho (!,.,/,#,£,_,-,&,~,?) — command aur argument extract karta hai.
    Returns: (cmd_lower, arg_str) or (None, None)
    """
    if not text:
        return None, None
    for p in PREFIXES:
        if text.startswith(p):
            rest = text[len(p):]
            parts = rest.split(None, 1)
            if not parts:
                return None, None
            cmd = parts[0].lower().strip()
            arg = parts[1].strip() if len(parts) > 1 else ""
            return cmd, arg
    return None, None

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔁 GENERIC NC LOOP — title change with retry
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
async def _nc_loop(task_dict: dict, chat_id: int, patterns: list, delay: float = NC_DELAY):
    """Generic NC loop — koi bhi pattern list ke saath kaam karta hai."""
    i = 0
    n = len(patterns)
    while chat_id in task_dict:
        try:
            title = patterns[i % n][:100]
            for bot in bots:
                if chat_id not in task_dict:
                    return
                try:
                    await bot.set_chat_title(chat_id, title)
                except RetryAfter as e:
                    await asyncio.sleep(float(e.retry_after) + 0.5)
                except (BadRequest, Forbidden):
                    pass
                except (TimedOut, NetworkError):
                    await asyncio.sleep(0.5)
                except Exception:
                    pass
            i += 1
            d = chat_delays.get(chat_id, delay)
            if d > 0:
                await asyncio.sleep(d)
        except asyncio.CancelledError:
            break
        except Exception:
            await asyncio.sleep(1)

async def _nc_emoji_loop(task_dict: dict, chat_id: int, emoji_list: list, pattern_fn, delay: float = NC_DELAY):
    """NC loop jahan pattern mein emoji rotate hoti hai."""
    i = 0
    n = len(emoji_list)
    while chat_id in task_dict:
        try:
            e = emoji_list[i % n]
            title = pattern_fn(e)[:100]
            for bot in bots:
                if chat_id not in task_dict:
                    return
                try:
                    await bot.set_chat_title(chat_id, title)
                except RetryAfter as e2:
                    await asyncio.sleep(float(e2.retry_after) + 0.5)
                except (BadRequest, Forbidden, TimedOut, NetworkError, Exception):
                    pass
            i += 1
            d = chat_delays.get(chat_id, delay)
            if d > 0:
                await asyncio.sleep(d)
        except asyncio.CancelledError:
            break
        except Exception:
            await asyncio.sleep(1)

async def _spam_loop(task_dict: dict, chat_id: int, messages, delay: float = SPAM_DELAY):
    """Generic spam loop — message list ya string ke saath kaam karta hai."""
    i = 0
    is_list = isinstance(messages, (list, tuple))
    n = len(messages) if is_list else 1
    while chat_id in task_dict:
        try:
            msg = messages[i % n] if is_list else messages
            for bot in bots:
                if chat_id not in task_dict:
                    return
                try:
                    await bot.send_message(chat_id, msg)
                except RetryAfter as e:
                    await asyncio.sleep(float(e.retry_after) + 0.3)
                except (BadRequest, Forbidden, TimedOut, NetworkError, Exception):
                    pass
            i += 1
            d = chat_delays.get(chat_id, delay)
            if d > 0:
                await asyncio.sleep(d)
        except asyncio.CancelledError:
            break
        except Exception:
            await asyncio.sleep(1)

async def _reply_loop(task_dict: dict, chat_id: int, target: str, delay: float = SPAM_DELAY):
    """Reply spam — user ke naam ke saath random messages."""
    i = 0
    msgs = [m.format(t=target) for m in REPLY_MSGS]
    n = len(msgs)
    while chat_id in task_dict:
        try:
            msg = msgs[i % n]
            for bot in bots:
                if chat_id not in task_dict:
                    return
                try:
                    await bot.send_message(chat_id, msg)
                except Exception:
                    pass
            i += 1
            d = chat_delays.get(chat_id, delay)
            if d > 0:
                await asyncio.sleep(d)
        except asyncio.CancelledError:
            break
        except Exception:
            await asyncio.sleep(1)

async def _swipe_loop(task_dict: dict, chat_id: int, msgs, delay: float = SWIPE_DELAY):
    """Swipe — messages ek ke baad ek reply chain mein."""
    i = 0
    is_list = isinstance(msgs, (list, tuple))
    n = len(msgs) if is_list else 1
    reply_id = None
    while chat_id in task_dict:
        try:
            msg = msgs[i % n] if is_list else msgs
            for bot in bots:
                if chat_id not in task_dict:
                    return
                try:
                    kwargs = {"chat_id": chat_id, "text": msg}
                    if reply_id:
                        kwargs["reply_to_message_id"] = reply_id
                    sent = await bot.send_message(**kwargs)
                    reply_id = sent.message_id
                    break
                except Exception:
                    pass
            i += 1
            d = chat_delays.get(chat_id, delay)
            if d > 0:
                await asyncio.sleep(d)
        except asyncio.CancelledError:
            break
        except Exception:
            await asyncio.sleep(1)

async def _gc_photo_loop(task_dict: dict, chat_id: int, photo_id: str):
    """GC photo changer loop."""
    while chat_id in task_dict:
        try:
            for bot in bots:
                if chat_id not in task_dict:
                    return
                try:
                    await bot.set_chat_photo(chat_id, photo_id)
                except RetryAfter as e:
                    await asyncio.sleep(float(e.retry_after) + 1)
                except Exception:
                    pass
            await asyncio.sleep(5)
        except asyncio.CancelledError:
            break
        except Exception:
            await asyncio.sleep(2)

def _stop(task_dict: dict, chat_id: int):
    """Task dict se chat_id remove karo (loop bandh ho jayega)."""
    task_dict.pop(chat_id, None)

def _stop_all_chat(chat_id: int):
    """Ek chat ke sabhi tasks bandh karo."""
    for d in [nc_tasks, spam_tasks, reply_tasks, slide_tasks,
              swipe_tasks, pswipe_tasks, raid_tasks, sticker_tasks,
              gc_tasks, vanitas_tasks]:
        d.pop(chat_id, None)

def _stop_all_global():
    """Sabhi chats ke sabhi tasks bandh karo."""
    for d in [nc_tasks, spam_tasks, reply_tasks, slide_tasks,
              swipe_tasks, pswipe_tasks, raid_tasks, sticker_tasks,
              gc_tasks, multinc_tasks, multispam_tasks, vanitas_tasks]:
        d.clear()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 💬 MENU TEXT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MENU_TEXT = """
╔══════════════════════════════════╗
   🌙 𝐆ᴇɴᴏs 𝐕𝐈𝐏 • 𝐌𝐄𝐆𝐀 𝐄𝐃𝐈𝐓𝐈𝐎𝐍 🕷️
╚══════════════════════════════════╝

📑 | ░N░░C░░S░ (Name Changers)
• !nc <naam>         ➔ Basic NC
• !snc <naam>        ➔ Single-group NC
• !exonc <naam>      ➔ Exo NC (flower)
• !hindinc <naam>    ➔ Hindi NC
• !urdunc <naam>     ➔ Urdu NC
• !bengalnc <naam>   ➔ Bengali NC
• !biharinc <naam>   ➔ Bihari NC
• !engnc <naam>      ➔ English block NC
• !emonc <naam>      ➔ Emoji NC
• !nc1 - !nc5 <naam> ➔ Special NCs (1-5)
• !knc <naam>        ➔ KNC
• !anc <naam>        ➔ ANC weather
• !fnc <naam>        ➔ FNC heart
• !ncmoon <naam>     ➔ Moon NC
• !ncflag <naam>     ➔ Flag NC
• !nccurly <naam>    ➔ Curly brace NC
• !timenc <naam>     ➔ Time NC
• !nctmkc <naam>     ➔ TMKC NC
• !ncspace <naam>    ➔ Space NC
• !fulnc <naam>      ➔ Full NC
• !flowernc <naam>   ➔ Flower NC
• !gcnc <naam>       ➔ GC Name Changer
• !ncbaap <naam>     ➔ NCBAAP (combo)
• !genosnc <naam>    ➔ Genos personal NC
• !multinc <naam>    ➔ Multi-group NC

⚙️ | ░S░░P░░A░░M░
• !spam <text>       ➔ Spam message
• !sspam <text>      ➔ Single-group spam
• !reply <naam>      ➔ Reply spam
• !spam1-4 <naam>    ➔ Special spam patterns
• !fuck <1-5> <naam> ➔ Fuck spam (5 types)
• !raid <naam>       ➔ Raid (random texts)
• !multispam <text>  ➔ Multi-group spam
• !rainbowspam <naam>➔ Rainbow spam
• !glitchspam <text> ➔ Glitch spam
• !numberspam <text> ➔ Number spam

🎭 | ░S░░L░░I░░D░░E░
• !slide <text>      ➔ Slide reply (passive)
• !slide1 <naam>     ➔ Slide1 reply chain
• !slide2 <naam>     ➔ Slide2 reply chain
• !slide3 <naam>     ➔ Slide3 pattern chain
• !swipe <naam>      ➔ Swipe (reply chain)
• !pswipe <text>     ➔ Personal swipe text
• !slidespam <naam>  ➔ Slide spam

📸 | ░G░░C░░P░░F░░P░
• !setgc             ➔ Photo reply se set karo
• !gc                ➔ GC photo changer ON

🎨 | ░S░░T░░I░░C░░K░░E░░R░
• !newsticker        ➔ Sticker add karo
• !sticker           ➔ Sticker spam
• !delsticker        ➔ Apne stickers clear
• !stopsticker       ➔ Sticker spam band

🎙️ | ░V░░O░░I░░C░░E░
• !vn <text>         ➔ Voice note (TTS)
• !vn2 <text>        ➔ Voice note v2

👑 | ░A░░D░░M░░I░░N░
• !son               ➔ Reply se sudo add
• !delsudo           ➔ Reply se sudo hata
• !listsudo          ➔ Sudo list dekho
• !promote           ➔ Reply se promote
• !target <naam>     ➔ Default target set

⚙️ | ░U░░T░░I░░L░░S░
• !me / !help        ➔ Yeh menu
• !ping              ➔ Ping check
• !status            ➔ Bot status
• !myid              ➔ Apna ID dekho
• !delay <0-10>      ➔ Delay set karo
• !threads <1-50>    ➔ Threads set
• !refresh           ➔ Refresh karo
• !join <link>       ➔ Group join
• !proxy add <url>   ➔ Proxy add
• !autoreply <t> <r> ➔ Auto reply set
• !vanitas <naam>    ➔ Vanitas mode (nc+spam)

🛡️ | ░S░░T░░O░░P░
• !stop / !stopall   ➔ Sabhi band karo
• !stopnc            ➔ NC band
• !stopspam          ➔ Spam band
• !stopreply         ➔ Reply band
• !stopswipe         ➔ Swipe band
• !stopraid          ➔ Raid band
• !stopgc            ➔ GC photo band
• !stopmultinc       ➔ Multi-NC band
• !stopmultispam     ➔ Multi-spam band
• !stopslide         ➔ Slide reply band
• !stopvanitas       ➔ Vanitas band

📌 Sab prefixes kaam karte hain: ! . / # £ _ - & ~ ?
"""

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🤖 MAIN MESSAGE HANDLER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global GC_PHOTO_FILE_ID, slide_reply_text

    if not update.message:
        return

    msg = update.message
    chat_id = msg.chat_id
    user_id = msg.from_user.id if msg.from_user else 0

    # Sabhi groups track karo
    all_groups.add(chat_id)

    # ── Passive slide reply (authorized users ke messages par reply)
    if slide_reply_text and not is_auth(user_id):
        if msg.text or msg.caption:
            try:
                await msg.reply_text(slide_reply_text)
            except Exception:
                pass
            return

    # ── Auto-reply check
    if chat_id in autoreply_data and (msg.text or msg.caption):
        text_lower = (msg.text or msg.caption or "").lower()
        for trigger, reply in autoreply_data.get(chat_id, {}).items():
            if trigger.lower() in text_lower:
                try:
                    await msg.reply_text(reply)
                except Exception:
                    pass

    # ── Sirf authorized users ke commands process karo
    if not is_auth(user_id):
        return

    text = msg.text or ""
    cmd, arg = parse_cmd(text)
    if not cmd:
        return

    # ════════════════════════════════
    # MENU / HELP
    # ════════════════════════════════
    if cmd in ("me", "help", "start", "menu"):
        try:
            await msg.reply_text(MENU_TEXT)
        except Exception:
            pass

    # ════════════════════════════════
    # PING
    # ════════════════════════════════
    elif cmd == "ping":
        t = time.time()
        sent = await msg.reply_text("🏓 Pinging...")
        ms = int((time.time() - t) * 1000)
        try:
            await sent.edit_text(f"🏓 Pong! {ms}ms\n🤖 Bots Active: {len(bots)}")
        except Exception:
            pass

    # ════════════════════════════════
    # STATUS
    # ════════════════════════════════
    elif cmd == "status":
        active_nc = len(nc_tasks)
        active_spam = len(spam_tasks)
        active_swipe = len(swipe_tasks) + len(pswipe_tasks)
        await msg.reply_text(
            f"╔══ 𝐆ᴇɴᴏs 𝐒𝐭𝐚𝐭𝐮𝐬 ══╗\n"
            f"🤖 Bots: {len(bots)}\n"
            f"👥 Groups: {len(all_groups)}\n"
            f"👑 Sudo: {len(SUDO_USERS)}\n"
            f"🔄 Active NC: {active_nc}\n"
            f"💬 Active Spam: {active_spam}\n"
            f"🔃 Active Swipe: {active_swipe}\n"
            f"📸 GC Slide: {'ON' if slide_reply_text else 'OFF'}\n"
            f"╚══════════════╝"
        )

    # ════════════════════════════════
    # MYID
    # ════════════════════════════════
    elif cmd == "myid":
        await msg.reply_text(f"🆔 Your ID: `{user_id}`\n💬 Chat ID: `{chat_id}`")

    # ════════════════════════════════
    # REFRESH
    # ════════════════════════════════
    elif cmd == "refresh":
        await msg.reply_text(f"⚡ Refreshed! Bots: {len(bots)} | Groups: {len(all_groups)}")

    # ════════════════════════════════
    # SUDO MANAGEMENT (owner only)
    # ════════════════════════════════
    elif cmd in ("son", "sudo", "addsudo") and user_id == OWNER_ID:
        target = None
        if msg.reply_to_message and msg.reply_to_message.from_user:
            target = msg.reply_to_message.from_user.id
        elif arg:
            try:
                target = int(arg)
            except ValueError:
                pass
        if target:
            SUDO_USERS.add(target)
            save_sudo()
            await msg.reply_text(f"✅ Sudo added: `{target}`")
        else:
            await msg.reply_text("⚠️ Reply karo kisi message pe ya ID do.")

    elif cmd in ("delsudo", "removesudo") and user_id == OWNER_ID:
        target = None
        if msg.reply_to_message and msg.reply_to_message.from_user:
            target = msg.reply_to_message.from_user.id
        elif arg:
            try:
                target = int(arg)
            except ValueError:
                pass
        if target:
            SUDO_USERS.discard(target)
            save_sudo()
            await msg.reply_text(f"✅ Sudo removed: `{target}`")
        else:
            await msg.reply_text("⚠️ Reply karo ya ID do.")

    elif cmd in ("listsudo", "listrights", "sudolist"):
        if not SUDO_USERS:
            await msg.reply_text("📋 Koi sudo nahi hai abhi.")
        else:
            lines = "\n".join(f"🆔 `{uid}`" for uid in SUDO_USERS)
            await msg.reply_text(f"👑 Sudo List ({len(SUDO_USERS)}):\n{lines}")

    # ════════════════════════════════
    # PROMOTE
    # ════════════════════════════════
    elif cmd == "promote" and user_id == OWNER_ID:
        if msg.reply_to_message and msg.reply_to_message.from_user:
            target = msg.reply_to_message.from_user.id
            for bot in bots:
                for g in list(all_groups):
                    try:
                        await bot.promote_chat_member(
                            g, target,
                            can_manage_chat=True,
                            can_change_info=True,
                            can_delete_messages=True,
                            can_invite_users=True,
                            can_restrict_members=True,
                            can_pin_messages=True,
                        )
                    except Exception:
                        pass
            await msg.reply_text(f"✅ Promote sent to all groups for `{target}`!")
        else:
            await msg.reply_text("⚠️ Kisi ka message reply karo pehle.")

    # ════════════════════════════════
    # DELAY
    # ════════════════════════════════
    elif cmd == "delay":
        try:
            d = float(arg)
            chat_delays[chat_id] = max(0.0, d)
            await msg.reply_text(f"⏱ Delay set: {d}s for this chat")
        except ValueError:
            await msg.reply_text("⚠️ !delay <seconds> — e.g. !delay 0.5")

    # ════════════════════════════════
    # THREADS
    # ════════════════════════════════
    elif cmd == "threads":
        try:
            t = max(1, min(50, int(arg)))
            chat_threads[chat_id] = t
            await msg.reply_text(f"🔄 Threads set: {t}")
        except ValueError:
            await msg.reply_text("⚠️ !threads <1-50>")

    # ════════════════════════════════
    # JOIN GROUP
    # ════════════════════════════════
    elif cmd == "join" and user_id == OWNER_ID:
        if not arg:
            await msg.reply_text("⚠️ !join <link or username>")
            return
        link = arg.replace("https://t.me/", "").replace("http://t.me/", "")
        link = link.lstrip("+").lstrip("@")
        for bot in bots:
            try:
                await bot.join_chat(link)
            except Exception:
                pass
        await msg.reply_text("✅ Join attempt sent to all bots!")

    # ════════════════════════════════
    # PROXY
    # ════════════════════════════════
    elif cmd == "proxy" and user_id == OWNER_ID:
        parts = arg.split(None, 1)
        sub = parts[0].lower() if parts else ""
        if sub == "add" and len(parts) > 1:
            with open("proxies.txt", "a") as f:
                f.write(parts[1].strip() + "\n")
            await msg.reply_text("✅ Proxy added!")
        else:
            count = 0
            if os.path.exists("proxies.txt"):
                count = sum(1 for l in open("proxies.txt") if l.strip())
            await msg.reply_text(f"📡 Proxies saved: {count}\nUsage: !proxy add <url>")

    # ════════════════════════════════
    # AUTO REPLY
    # ════════════════════════════════
    elif cmd == "autoreply":
        parts = arg.split(None, 1)
        if len(parts) < 2:
            await msg.reply_text("⚠️ !autoreply <trigger> <reply_text>")
            return
        trigger, reply = parts[0], parts[1]
        if chat_id not in autoreply_data:
            autoreply_data[chat_id] = {}
        autoreply_data[chat_id][trigger] = reply
        await msg.reply_text(f"🤖 Auto-reply set!\nTrigger: {trigger}\nReply: {reply}")

    elif cmd == "stopautoreply":
        if arg and chat_id in autoreply_data:
            autoreply_data[chat_id].pop(arg, None)
            await msg.reply_text(f"🛑 Auto-reply removed for: {arg}")
        else:
            autoreply_data.pop(chat_id, None)
            await msg.reply_text("🛑 Sabhi auto-replies hataye!")

    # ════════════════════════════════
    # GC PHOTO — SETGC + GC
    # ════════════════════════════════
    elif cmd == "setgc":
        # Photo reply se set karo
        if msg.reply_to_message and msg.reply_to_message.photo:
            GC_PHOTO_FILE_ID = msg.reply_to_message.photo[-1].file_id
            await msg.reply_text("✅ GC Photo saved! Ab !gc se start karo.")
        elif msg.photo:
            GC_PHOTO_FILE_ID = msg.photo[-1].file_id
            await msg.reply_text("✅ GC Photo saved! Ab !gc se start karo.")
        else:
            await msg.reply_text("⚠️ Photo ke saath reply karo is command se.")

    elif cmd == "gc":
        if not GC_PHOTO_FILE_ID:
            await msg.reply_text("⚠️ Pehle !setgc se photo set karo.")
            return
        if chat_id in gc_tasks:
            await msg.reply_text("⚠️ GC photo changer already running!")
            return
        gc_tasks[chat_id] = True
        asyncio.create_task(_gc_photo_loop(gc_tasks, chat_id, GC_PHOTO_FILE_ID))
        await msg.reply_text("📸 GC Photo Changer STARTED! !stopgc se band karo.")

    elif cmd == "stopgc":
        _stop(gc_tasks, chat_id)
        await msg.reply_text("🛑 GC Photo Changer stopped!")

    # ════════════════════════════════
    # STICKER SYSTEM
    # ════════════════════════════════
    elif cmd == "newsticker":
        if msg.reply_to_message and msg.reply_to_message.sticker:
            sid = msg.reply_to_message.sticker.file_id
            uid_str = str(user_id)
            if uid_str not in USER_STICKERS:
                USER_STICKERS[uid_str] = []
            USER_STICKERS[uid_str].append(sid)
            save_stickers()
            count = len(USER_STICKERS[uid_str])
            await msg.reply_text(f"✅ Sticker added! Total: {count}")
        else:
            await msg.reply_text("⚠️ Kisi sticker pe reply karo.")

    elif cmd == "sticker":
        uid_str = str(user_id)
        if uid_str not in USER_STICKERS or not USER_STICKERS[uid_str]:
            await msg.reply_text("❌ Koi sticker nahi! Pehle !newsticker se add karo.")
            return
        stickers = USER_STICKERS[uid_str]
        sticker_tasks[chat_id] = True
        async def _sticker_loop(d, cid, s_list):
            while cid in d:
                try:
                    for bot in bots:
                        if cid not in d:
                            return
                        try:
                            await bot.send_sticker(cid, random.choice(s_list))
                        except Exception:
                            pass
                    await asyncio.sleep(chat_delays.get(cid, 0.3))
                except asyncio.CancelledError:
                    break
                except Exception:
                    await asyncio.sleep(0.5)
        asyncio.create_task(_sticker_loop(sticker_tasks, chat_id, stickers))
        await msg.reply_text("🎨 Sticker spam started!")

    elif cmd == "delsticker":
        uid_str = str(user_id)
        USER_STICKERS[uid_str] = []
        save_stickers()
        await msg.reply_text("✅ Saare stickers clear!")

    elif cmd == "stopsticker":
        _stop(sticker_tasks, chat_id)
        await msg.reply_text("🛑 Sticker spam stopped!")

    # ════════════════════════════════
    # SLIDE (passive reply to everyone)
    # ════════════════════════════════
    elif cmd == "slide":
        if not arg:
            await msg.reply_text("⚠️ !slide <text>")
            return
        slide_reply_text = arg
        await msg.reply_text(f"✅ Slide reply ON: {arg}")

    elif cmd == "stopslide":
        slide_reply_text = None
        await msg.reply_text("🛑 Slide reply band!")

    # ════════════════════════════════
    # SLIDE1 — reply chain
    # ════════════════════════════════
    elif cmd in ("slide1", "slidespam"):
        if not arg:
            await msg.reply_text("⚠️ !slide1 <naam>")
            return
        msgs_list = [m.format(t=arg) if "{t}" in m else m for m in SLIDE1_MSGS]
        slide_tasks[chat_id] = True
        asyncio.create_task(_spam_loop(slide_tasks, chat_id, msgs_list, SWIPE_DELAY))
        await msg.reply_text(f"🎭 Slide1 STARTED for: {arg}")

    elif cmd == "slide2":
        if not arg:
            await msg.reply_text("⚠️ !slide2 <naam>")
            return
        msgs_list = SLIDE2_MSGS[:]
        slide_tasks[chat_id] = True
        asyncio.create_task(_spam_loop(slide_tasks, chat_id, msgs_list, SWIPE_DELAY))
        await msg.reply_text(f"🎭 Slide2 STARTED!")

    elif cmd == "slide3":
        if not arg:
            await msg.reply_text("⚠️ !slide3 <naam>")
            return
        pattern = SLIDE3_PATTERN.format(t=arg)
        slide_tasks[chat_id] = True
        asyncio.create_task(_spam_loop(slide_tasks, chat_id, pattern, SWIPE_DELAY))
        await msg.reply_text(f"🎭 Slide3 STARTED for: {arg}")

    # ════════════════════════════════
    # SWIPE
    # ════════════════════════════════
    elif cmd == "swipe":
        if not arg:
            await msg.reply_text("⚠️ !swipe <naam>")
            return
        msgs_list = [m.format(t=arg) if "{t}" in m else m for m in SWIPE_MSGS]
        swipe_tasks[chat_id] = True
        asyncio.create_task(_swipe_loop(swipe_tasks, chat_id, msgs_list, SWIPE_DELAY))
        await msg.reply_text(f"🔄 SWIPE STARTED for: {arg}")

    elif cmd == "pswipe":
        if not arg:
            await msg.reply_text("⚠️ !pswipe <text>")
            return
        pswipe_tasks[chat_id] = True
        asyncio.create_task(_swipe_loop(pswipe_tasks, chat_id, arg, SWIPE_DELAY))
        await msg.reply_text(f"⚡ Personal Swipe STARTED: {arg}")

    elif cmd == "stopswipe":
        _stop(swipe_tasks, chat_id)
        _stop(pswipe_tasks, chat_id)
        await msg.reply_text("🛑 Swipe stopped!")

    # ════════════════════════════════
    # RAID
    # ════════════════════════════════
    elif cmd == "raid":
        if not arg:
            await msg.reply_text("⚠️ !raid <naam>")
            return
        msgs_list = [f"{arg} {t}" for t in RAID_TEXTS]
        raid_tasks[chat_id] = True
        asyncio.create_task(_spam_loop(raid_tasks, chat_id, msgs_list, RAID_DELAY))
        await msg.reply_text(f"💀 RAID STARTED for: {arg}")

    elif cmd == "stopraid":
        _stop(raid_tasks, chat_id)
        await msg.reply_text("🛑 Raid stopped!")

    # ════════════════════════════════
    # NC — BASIC (multi group)
    # ════════════════════════════════
    elif cmd == "nc":
        if not arg:
            await msg.reply_text("⚠️ !nc <naam>")
            return
        patterns = [m.format(t=arg) for m in BASIC_NC_MSGS]
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"⚡ NC STARTED for: {arg}")

    # ════════════════════════════════
    # SNC — single group NC
    # ════════════════════════════════
    elif cmd == "snc":
        if not arg:
            await msg.reply_text("⚠️ !snc <naam>")
            return
        patterns = [m.format(t=arg) for m in BASIC_NC_MSGS]
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"⚡ SNC STARTED for: {arg}")

    # ════════════════════════════════
    # EXONC
    # ════════════════════════════════
    elif cmd == "exonc":
        if not arg:
            await msg.reply_text("⚠️ !exonc <naam>")
            return
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_emoji_loop(
            nc_tasks, chat_id, EXONC_TEXTS,
            lambda e: f"{arg} {e}"
        ))
        await msg.reply_text(f"🌺 ExoNC STARTED for: {arg}")

    # ════════════════════════════════
    # HINDI NC
    # ════════════════════════════════
    elif cmd == "hindinc":
        if not arg:
            await msg.reply_text("⚠️ !hindinc <naam>")
            return
        patterns = [m.format(t=arg) for m in HINDI_NC_PATTERNS]
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"🇮🇳 HindiNC STARTED for: {arg}")

    # ════════════════════════════════
    # URDU NC
    # ════════════════════════════════
    elif cmd == "urdunc":
        if not arg:
            await msg.reply_text("⚠️ !urdunc <naam>")
            return
        patterns = [m.format(t=arg) for m in URDU_NC_PATTERNS]
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"🕌 UrduNC STARTED for: {arg}")

    # ════════════════════════════════
    # BENGAL NC
    # ════════════════════════════════
    elif cmd == "bengalnc":
        if not arg:
            await msg.reply_text("⚠️ !bengalnc <naam>")
            return
        patterns = [m.format(t=arg) for m in BENGALI_NC_PATTERNS]
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"🐯 BengalNC STARTED for: {arg}")

    # ════════════════════════════════
    # BIHARI NC
    # ════════════════════════════════
    elif cmd == "biharinc":
        if not arg:
            await msg.reply_text("⚠️ !biharinc <naam>")
            return
        patterns = [m.format(t=arg) for m in BIHARI_NC_PATTERNS]
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"🌾 BihariNC STARTED for: {arg}")

    # ════════════════════════════════
    # ENGLISH NC
    # ════════════════════════════════
    elif cmd == "engnc":
        if not arg:
            await msg.reply_text("⚠️ !engnc <naam>")
            return
        patterns = [m.format(t=arg) for m in ENGLISH_NC_PATTERNS]
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"🔤 EngNC STARTED for: {arg}")

    # ════════════════════════════════
    # EMOJI NC
    # ════════════════════════════════
    elif cmd in ("emonc", "ncemo"):
        if not arg:
            await msg.reply_text("⚠️ !emonc <naam>")
            return
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_emoji_loop(
            nc_tasks, chat_id, EMOJI_NC_EMOJIS,
            lambda e: EMOJI_NC_PATTERN.format(t=arg, e=e)
        ))
        await msg.reply_text(f"🐧 EmojiNC STARTED for: {arg}")

    # ════════════════════════════════
    # NC1-NC5
    # ════════════════════════════════
    elif cmd == "nc1":
        if not arg:
            await msg.reply_text("⚠️ !nc1 <naam>")
            return
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_emoji_loop(nc_tasks, chat_id, NC1_EMOJIS, lambda e: NC1_PATTERN.format(t=arg, e=e)))
        await msg.reply_text(f"🌸 NC1 STARTED for: {arg}")

    elif cmd == "nc2":
        if not arg:
            await msg.reply_text("⚠️ !nc2 <naam>")
            return
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_emoji_loop(nc_tasks, chat_id, NC2_EMOJIS, lambda e: NC2_PATTERN.format(t=arg, e=e)))
        await msg.reply_text(f"🐦 NC2 STARTED for: {arg}")

    elif cmd == "nc3":
        if not arg:
            await msg.reply_text("⚠️ !nc3 <naam>")
            return
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_emoji_loop(nc_tasks, chat_id, NC3_EMOJIS, lambda e: NC3_PATTERN.format(t=arg, e=e)))
        await msg.reply_text(f"🚩 NC3 STARTED for: {arg}")

    elif cmd == "nc4":
        if not arg:
            await msg.reply_text("⚠️ !nc4 <naam>")
            return
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_emoji_loop(nc_tasks, chat_id, NC4_EMOJIS, lambda e: NC4_PATTERN.format(t=arg, e=e)))
        await msg.reply_text(f"🌋 NC4 STARTED for: {arg}")

    elif cmd == "nc5":
        if not arg:
            await msg.reply_text("⚠️ !nc5 <naam>")
            return
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_emoji_loop(nc_tasks, chat_id, NC5_EMOJIS, lambda e: NC5_PATTERN.format(t=arg, e=e)))
        await msg.reply_text(f"🩷 NC5 STARTED for: {arg}")

    # ════════════════════════════════
    # KNC / ANC / FNC
    # ════════════════════════════════
    elif cmd == "knc":
        if not arg:
            await msg.reply_text("⚠️ !knc <naam>")
            return
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_emoji_loop(nc_tasks, chat_id, KNC_EMOJIS, lambda e: KNC_PATTERN.format(t=arg, e=e)))
        await msg.reply_text(f"🫯 KNC STARTED for: {arg}")

    elif cmd == "anc":
        if not arg:
            await msg.reply_text("⚠️ !anc <naam>")
            return
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_emoji_loop(nc_tasks, chat_id, ANC_EMOJIS, lambda e: ANC_PATTERN.format(t=arg, e=e)))
        await msg.reply_text(f"🌈 ANC STARTED for: {arg}")

    elif cmd == "fnc":
        if not arg:
            await msg.reply_text("⚠️ !fnc <naam>")
            return
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_emoji_loop(nc_tasks, chat_id, FNC_EMOJIS, lambda e: FNC_PATTERN.format(t=arg, e=e)))
        await msg.reply_text(f"❤️ FNC STARTED for: {arg}")

    # ════════════════════════════════
    # MOON NC
    # ════════════════════════════════
    elif cmd == "ncmoon":
        if not arg:
            await msg.reply_text("⚠️ !ncmoon <naam>")
            return
        patterns = [m.format(t=arg) for m in MOON_NC_MSGS]
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"🌙 MoonNC STARTED for: {arg}")

    # ════════════════════════════════
    # FLAG NC
    # ════════════════════════════════
    elif cmd == "ncflag":
        if not arg:
            await msg.reply_text("⚠️ !ncflag <naam>")
            return
        patterns = [m.format(t=arg) for m in FLAG_NC_MSGS]
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"🚩 FlagNC STARTED for: {arg}")

    # ════════════════════════════════
    # CURLY NC
    # ════════════════════════════════
    elif cmd == "nccurly":
        if not arg:
            await msg.reply_text("⚠️ !nccurly <naam>")
            return
        patterns = [m.format(t=arg) for m in CURLY_NC_MSGS]
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"🌀 CurlyNC STARTED for: {arg}")

    # ════════════════════════════════
    # TIME NC
    # ════════════════════════════════
    elif cmd == "timenc":
        if not arg:
            await msg.reply_text("⚠️ !timenc <naam>")
            return
        patterns = [m.format(t=arg) for m in TIME_NC_MSGS]
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"⏰ TimeNC STARTED for: {arg}")

    # ════════════════════════════════
    # TMKC NC
    # ════════════════════════════════
    elif cmd == "nctmkc":
        if not arg:
            await msg.reply_text("⚠️ !nctmkc <naam>")
            return
        patterns = [m.format(t=arg) for m in TMKC_NC_MSGS]
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"💢 TmkcNC STARTED for: {arg}")

    # ════════════════════════════════
    # SPACE NC
    # ════════════════════════════════
    elif cmd in ("ncspace", "spacenc"):
        if not arg:
            await msg.reply_text("⚠️ !ncspace <naam>")
            return
        patterns = [m.format(t=arg) for m in SPACE_NC_MSGS]
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"🌀 SpaceNC STARTED for: {arg}")

    # ════════════════════════════════
    # FULL NC (flower style)
    # ════════════════════════════════
    elif cmd == "fulnc":
        if not arg:
            await msg.reply_text("⚠️ !fulnc <naam>")
            return
        patterns = [m.format(t=arg) for m in FUL_NC_MSGS]
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"🌿 FulNC STARTED for: {arg}")

    # ════════════════════════════════
    # FLOWER NC
    # ════════════════════════════════
    elif cmd == "flowernc":
        if not arg:
            await msg.reply_text("⚠️ !flowernc <naam>")
            return
        patterns = [m.format(t=arg) for m in FLOWER_NC_MSGS]
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"🌸 FlowerNC STARTED for: {arg}")

    # ════════════════════════════════
    # GCNC — GC Name Changer (raid texts)
    # ════════════════════════════════
    elif cmd == "gcnc":
        if not arg:
            await msg.reply_text("⚠️ !gcnc <naam>")
            return
        patterns = [f"{arg} {t}" for t in RAID_TEXTS]
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"⚡ GCNC STARTED for: {arg}")

    # ════════════════════════════════
    # NCBAAP — combo NC (raid + emoji + exo)
    # ════════════════════════════════
    elif cmd == "ncbaap":
        if not arg:
            await msg.reply_text("⚠️ !ncbaap <naam>")
            return
        patterns = (
            [f"{arg} {t}" for t in RAID_TEXTS] +
            [f"{arg} {e}" for e in NCEMO_EMOJIS] +
            [f"{arg} {e}" for e in EXONC_TEXTS]
        )
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"💀🔥 NCBAAP ACTIVATED for: {arg}")

    # ════════════════════════════════
    # GENOS NC (personal style)
    # ════════════════════════════════
    elif cmd == "genosnc":
        if not arg:
            await msg.reply_text("⚠️ !genosnc <naam>")
            return
        patterns = [m.format(t=arg) for m in GENOSNC_MSGS]
        nc_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(nc_tasks, chat_id, patterns))
        await msg.reply_text(f"👑 GenosNC STARTED for: {arg}")

    # ════════════════════════════════
    # MULTINC — sabhi groups mein NC
    # ════════════════════════════════
    elif cmd == "multinc" and user_id == OWNER_ID:
        if not arg:
            await msg.reply_text("⚠️ !multinc <naam>")
            return
        if not all_groups:
            await msg.reply_text("⚠️ Koi group nahi mila abhi.")
            return
        for g in list(all_groups):
            if g not in multinc_tasks:
                patterns = [f"{arg} {t}" for t in RAID_TEXTS]
                multinc_tasks[g] = True
                asyncio.create_task(_nc_loop(multinc_tasks, g, patterns, 1.0))
        await msg.reply_text(f"🌐 Multi-NC STARTED in {len(all_groups)} groups for: {arg}")

    elif cmd == "stopmultinc":
        multinc_tasks.clear()
        await msg.reply_text("🛑 Multi-NC stopped!")

    # ════════════════════════════════
    # STOP NC
    # ════════════════════════════════
    elif cmd in ("stopnc", "stopncflag", "stopnccurly", "stoptimenc",
                 "stopncmoon", "stopncspace", "stopncemo", "stopnctmkc",
                 "stopknc", "stopanc", "stopfnc", "stopnc1", "stopnc2",
                 "stopnc3", "stopnc4", "stopnc5", "stopexonc", "stophindinc",
                 "stopurdunc", "stopbengalnc", "stopbiharinc", "stopengnc",
                 "stopgcnc", "stopncbaap", "stopgenosnc", "stopflowernc",
                 "stopfulnc", "stopspacenc"):
        _stop(nc_tasks, chat_id)
        await msg.reply_text("🛑 NC stopped!")

    # ════════════════════════════════
    # SPAM — basic
    # ════════════════════════════════
    elif cmd in ("spam", "sspam"):
        if not arg:
            await msg.reply_text("⚠️ !spam <text>")
            return
        spam_tasks[chat_id] = True
        asyncio.create_task(_spam_loop(spam_tasks, chat_id, arg))
        await msg.reply_text(f"⚡ SPAM STARTED!")

    # ════════════════════════════════
    # REPLY SPAM
    # ════════════════════════════════
    elif cmd == "reply":
        if not arg:
            await msg.reply_text("⚠️ !reply <naam>")
            return
        reply_tasks[chat_id] = True
        asyncio.create_task(_reply_loop(reply_tasks, chat_id, arg))
        await msg.reply_text(f"💬 Reply Spam STARTED for: {arg}")

    elif cmd == "stopreply":
        _stop(reply_tasks, chat_id)
        await msg.reply_text("🛑 Reply spam stopped!")

    # ════════════════════════════════
    # SPAM1-4 special patterns
    # ════════════════════════════════
    elif cmd == "spam1":
        if not arg:
            await msg.reply_text("⚠️ !spam1 <naam>")
            return
        msg_text = SPAM1_PATTERN.format(t=arg)
        spam_tasks[chat_id] = True
        asyncio.create_task(_spam_loop(spam_tasks, chat_id, msg_text))
        await msg.reply_text("🎐 Spam1 STARTED!")

    elif cmd == "spam2":
        if not arg:
            await msg.reply_text("⚠️ !spam2 <naam>")
            return
        msg_text = SPAM2_PATTERN.format(t=arg)
        spam_tasks[chat_id] = True
        asyncio.create_task(_spam_loop(spam_tasks, chat_id, msg_text))
        await msg.reply_text("💢 Spam2 STARTED!")

    elif cmd == "spam3":
        if not arg:
            await msg.reply_text("⚠️ !spam3 <naam>")
            return
        msg_text = SPAM3_PATTERN.format(t=arg)
        spam_tasks[chat_id] = True
        asyncio.create_task(_spam_loop(spam_tasks, chat_id, msg_text))
        await msg.reply_text("💞 Spam3 STARTED!")

    elif cmd == "spam4":
        if not arg:
            await msg.reply_text("⚠️ !spam4 <naam>")
            return
        msg_text = SPAM4_PATTERN.format(t=arg)
        spam_tasks[chat_id] = True
        asyncio.create_task(_spam_loop(spam_tasks, chat_id, msg_text))
        await msg.reply_text("𓆩 Spam4 STARTED!")

    # ════════════════════════════════
    # FUCK SPAM (5 types)
    # ════════════════════════════════
    elif cmd == "fuck":
        parts = arg.split(None, 1)
        if len(parts) < 2:
            await msg.reply_text("⚠️ !fuck <1-5> <naam>\nTypes:\n1=Hearts 2=White 3=Black 4=Flags 5=Wizard")
            return
        try:
            opt = int(parts[0])
            naam = parts[1]
            if opt not in range(1, 6):
                raise ValueError
        except ValueError:
            await msg.reply_text("⚠️ Option 1-5 hona chahiye.")
            return
        base = FUCK_TEXTS[opt]
        if opt == 1:
            elist = FUCK_HEART_EMOJIS
        elif opt == 4:
            elist = FUCK_FLAG_EMOJIS
        else:
            elist = MAIN_EMOJIS
        spam_tasks[chat_id] = True
        async def _fuck_loop(d, cid, name, base_txt, emojis):
            i = 0
            while cid in d:
                try:
                    e = emojis[i % len(emojis)]
                    msg_text = f"{name} {base_txt} {e}"
                    for bot in bots:
                        if cid not in d:
                            return
                        try:
                            await bot.send_message(cid, msg_text)
                        except Exception:
                            pass
                    i += 1
                    await asyncio.sleep(chat_delays.get(cid, SPAM_DELAY))
                except asyncio.CancelledError:
                    break
                except Exception:
                    await asyncio.sleep(0.3)
        asyncio.create_task(_fuck_loop(spam_tasks, chat_id, naam, base, elist))
        await msg.reply_text(f"🎯 FUCK Type {opt} STARTED for: {naam}")

    elif cmd == "sfuck":
        _stop(spam_tasks, chat_id)
        await msg.reply_text("🛑 Fuck spam stopped!")

    # ════════════════════════════════
    # RAINBOW SPAM
    # ════════════════════════════════
    elif cmd == "rainbowspam":
        if not arg:
            await msg.reply_text("⚠️ !rainbowspam <naam>")
            return
        msgs_list = [f"{c} {arg} {c}" for c in RAINBOW_COLORS]
        spam_tasks[chat_id] = True
        asyncio.create_task(_spam_loop(spam_tasks, chat_id, msgs_list))
        await msg.reply_text(f"🌈 Rainbow Spam STARTED for: {arg}")

    # ════════════════════════════════
    # GLITCH SPAM
    # ════════════════════════════════
    elif cmd == "glitchspam":
        if not arg:
            await msg.reply_text("⚠️ !glitchspam <text>")
            return
        glitch_chars = "̴̵̶̷̸̡̢̧̨̛̖̗̘̙̜̝̞̟̠̤̥̦̩̪̫̬̭̮̯̰̱̲̳̹̺̻̼͇͈͉͍͎̀́̂̃̄̅̆̇̈̉̊̋̌̍̎̏̐̑̒̓̔̽̾̿̀́͂̓̈́͆͊͋͌͑͐͒͗͛͘͟͠͝͞͡ͅ"
        glitched = "".join(c + random.choice(glitch_chars) for c in arg)
        spam_tasks[chat_id] = True
        asyncio.create_task(_spam_loop(spam_tasks, chat_id, glitched))
        await msg.reply_text("⚡ Glitch Spam STARTED!")

    # ════════════════════════════════
    # NUMBER SPAM
    # ════════════════════════════════
    elif cmd == "numberspam":
        if not arg:
            await msg.reply_text("⚠️ !numberspam <text>")
            return
        msgs_list = [f"{i}. {arg}" for i in range(1, 101)]
        spam_tasks[chat_id] = True
        asyncio.create_task(_spam_loop(spam_tasks, chat_id, msgs_list))
        await msg.reply_text("🔢 Number Spam STARTED!")

    # ════════════════════════════════
    # MULTI SPAM — sabhi groups
    # ════════════════════════════════
    elif cmd == "multispam" and user_id == OWNER_ID:
        if not arg:
            await msg.reply_text("⚠️ !multispam <text>")
            return
        if not all_groups:
            await msg.reply_text("⚠️ Koi group nahi.")
            return
        for g in list(all_groups):
            multispam_tasks[g] = True
            asyncio.create_task(_spam_loop(multispam_tasks, g, arg, 2.0))
        await msg.reply_text(f"🌐 Multi-Spam STARTED in {len(all_groups)} groups!")

    elif cmd == "stopmultispam":
        multispam_tasks.clear()
        await msg.reply_text("🛑 Multi-Spam stopped!")

    # ════════════════════════════════
    # VANITAS MODE — NC + spam combined
    # ════════════════════════════════
    elif cmd == "vanitas":
        if not arg:
            await msg.reply_text("⚠️ !vanitas <naam>")
            return
        nc_patterns = [m.format(t=arg) for m in BASIC_NC_MSGS]
        spam_msgs = [m.format(t=arg) for m in SPAM_MSGS]
        vanitas_tasks[chat_id] = True
        asyncio.create_task(_nc_loop(vanitas_tasks, chat_id, nc_patterns, 0.1))
        asyncio.create_task(_spam_loop(vanitas_tasks, chat_id, spam_msgs, 0.2))
        await msg.reply_text(f"🌙 VANITAS MODE ACTIVATED for: {arg}")

    elif cmd == "stopvanitas":
        _stop(vanitas_tasks, chat_id)
        await msg.reply_text("🛑 Vanitas mode stopped!")

    # ════════════════════════════════
    # STOP SPAM
    # ════════════════════════════════
    elif cmd == "stopspam":
        _stop(spam_tasks, chat_id)
        await msg.reply_text("🛑 Spam stopped!")

    # ════════════════════════════════
    # VOICE NOTE (TTS)
    # ════════════════════════════════
    elif cmd in ("vn", "vn2", "vn4"):
        if not GTTS_AVAILABLE:
            await msg.reply_text("❌ gtts install nahi hai. pip install gtts karo.")
            return
        if not arg:
            await msg.reply_text("⚠️ !vn <text>")
            return
        try:
            lang = "hi" if cmd == "vn2" else "en"
            tts = gTTS(text=arg, lang=lang)
            buf = io.BytesIO()
            tts.write_to_fp(buf)
            buf.seek(0)
            await msg.reply_voice(voice=buf)
        except Exception as e:
            await msg.reply_text(f"❌ Voice note error: {e}")

    # ════════════════════════════════
    # STOP ALL
    # ════════════════════════════════
    elif cmd in ("stop", "stopall"):
        slide_reply_text = None
        _stop_all_global()
        await msg.reply_text("👑 𝐆ᴇɴᴏs 𝐁ᴀᴀᴘ 𝐇ᴀɪ 👑\n✅ Sabhi tasks bandh!")

    # ════════════════════════════════
    # Unknown command — no response (noise avoid)
    # ════════════════════════════════


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚀 BOT STARTUP — ek saath sabhi bots start
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
async def start_bot(token: str, index: int):
    """Ek bot token ke liye application start karo."""
    try:
        app = ApplicationBuilder().token(token).build()
        app.add_handler(MessageHandler(filters.ALL, handle_message))
        await app.initialize()
        await app.start()
        applications.append(app)
        bots.append(app.bot)
        await app.updater.start_polling(
            drop_pending_updates=True,
            allowed_updates=["message", "callback_query"],
        )
        print(f"✅ Bot {index+1} started: @{app.bot.username}")
    except Exception as e:
        print(f"❌ Bot {index+1} failed ({token[:20]}...): {e}")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MAIN ASYNC LOOP WITH FLASK INTEGRATION (REPLACE YOUR END WITH THIS)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

async def main():
    print("""
╔══════════════════════════════════════════════╗
║   𝐆ᴇɴᴏs 𝐕𝐈𝐏 • 𝐌𝐄𝐆𝐀 𝐄𝐃𝐈𝐓𝐈𝐎𝐍 🦋             ║
║   39 Files → 1 File Mega Merge              ║
║   Prefix: ! . / # £ _ - & ~ ?              ║
╚══════════════════════════════════════════════╝
    """)

    # Flask Server ko background thread mein start karo (Render ke liye)
    keep_alive()

    # Sabhi bots parallel mein start karo
    await asyncio.gather(*[
        start_bot(token, i)
        for i, token in enumerate(BOT_TOKENS)
    ], return_exceptions=True)

    print(f"\n✅ {len(bots)}/{len(BOT_TOKENS)} bots active!")
    print(f"👑 Owner ID: {OWNER_ID}")
    print(f"📋 Commands: !me ya /me se menu dekho\n")

    # Signal handlers — graceful shutdown
    def _shutdown(sig, frame):
        print("\n🛑 Shutting down gracefully...")
        _stop_all_global()
        sys.exit(0)

    signal.signal(signal.SIGINT, _shutdown)
    signal.signal(signal.SIGTERM, _shutdown)

    # LIFETIME FREE LOOP: Yeh Render par server ko kabhi band nahi hone dega
    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__":
    # Python ke modern asyncio event loop se application run karo
    asyncio.run(main())
