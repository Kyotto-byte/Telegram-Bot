TikTok Downloader Telegram Bot
Telegram bot written in Python for downloading videos directly from TikTok via link.

Features
Video Downloading: Fetch and download TikTok videos using direct links.
Cookie Support: Integrates browser cookies to bypass restrictions and process private or region-locked links.
Automated Processing: Instant link detection and video delivery inside the chat.

Tech Stack
Python 3
python-telegram-bot (or aiogram)
yt-dlp

Getting Started
Clone the repository:

Bash
git clone https://github.com/Kyotto-byte/tiktok-downloader-bot.git
cd tiktok-downloader-bot
Install dependencies:

Bash
pip install python-telegram-bot yt-dlp
Configure the bot:
Add your Telegram Bot Token and browser cookies file (cookies.txt) to the project directory.

Run the bot:

Bash
python main.py
