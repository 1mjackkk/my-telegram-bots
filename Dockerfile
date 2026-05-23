FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir python-telegram-bot pyTelegramBotAPI pyrogram telethon tgcrypto gTTS qrcode requests yt-dlp database-client pytz AsyncAndroid

WORKDIR /app
COPY . /app

EXPOSE 5000

CMD ["python3", "Genoshu.py"]
