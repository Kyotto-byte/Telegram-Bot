import os
import telebot
import yt_dlp

TOKEN = 'YOUR_BOT_TOKEN_HERE'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Отправь мне ссылку на видео из TikTok.")

@bot.message_handler(func=lambda message: True)
def download_and_send_video(message):
    url = message.text.strip()
    
    if "tiktok.com" not in url:
        bot.reply_to(message, "В ссылке нет tiktok.com")
        return

    status_msg = bot.reply_to(message, "Скачиваю...")
    output_filename = f"video_{message.chat.id}.mp4"

    ydl_opts = {
        'format': 'best',
        'outtmpl': output_filename,
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        with open(output_filename, 'rb') as video_file:
            bot.send_video(message.chat.id, video_file, caption="")
        
        bot.delete_message(message.chat.id, status_msg.message_id)

    except Exception as e:
        print(f"Ошибка: {e}")
        bot.edit_message_text(
            "Не удалось скачать видео", 
            chat_id=message.chat.id, 
            message_id=status_msg.message_id
        )
    
    finally:
        if os.path.exists(output_filename):
            os.remove(output_filename)

bot.infinity_polling()