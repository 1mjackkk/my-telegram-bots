FROM ubuntu:22.04

# 1. System tools, Python aur Node.js (PM2 ke liye) install karna
RUN apt-get update && apt-get install -y \
    curl \
    git \
    python3 \
    python3-pip \
    sudo \
    nodejs \
    npm \
    && curl -sLo /usr/local/bin/ttyd https://github.com/tsl0922/ttyd/releases/download/1.7.3/ttyd.x86_64 \
    && chmod +x /usr/local/bin/ttyd \
    && npm install -g pm2 \
    && rm -rf /var/lib/apt/lists/*

# 2. Tumhari Genoshu.py file ke liye saari required libraries
RUN pip3 install --no-cache-dir python-telegram-bot pyTelegramBotAPI pyrogram telethon tgcrypto gTTS qrcode requests yt-dlp database-client pytz AsyncAndroid

# 3. Admin user aur password (irshad@123) set karna
RUN useradd -m -s /bin/bash admin && echo "admin:irshad@123" | chpasswd && adduser admin sudo

EXPOSE 8000

# 4. Auto-start script: Agar Genoshu.py mile toh PM2 use apne aap chala dega
RUN echo '#!/bin/bash\n\
cd /home/admin\n\
if [ -f "Genoshu.py" ]; then\n\
    pm2 start Genoshu.py --interpreter python3\n\
fi\n\
ttyd -p 8000 -c "admin:irshad@123" bash' > /start.sh && chmod +x /start.sh

CMD ["/bin/bash", "/start.sh"]
