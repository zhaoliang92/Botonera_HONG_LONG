import os
import telegram
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, chataction, InputMediaPhoto
from requests import get

INPUT_TEXT = 0

randomPeopleUrl = "https://images2.imgbox.com/ae/80/bRrO7kaP_o.jpeg"

image = get(randomPeopleUrl).content


# ENLACE DE CANALES O GRUPOS DE LA BOTONERA

def start(update, context):

    button1 = InlineKeyboardButton(
        text="Dojo en TV",
        url="https://t.me/dojo_en_tv"
    )

    button2 = InlineKeyboardButton(
        text="Instituto Confucio, UH",
        url="https://t.me/ConfucioUH"
    )

    button3 = InlineKeyboardButton(
        text="🏮哈瓦那的唐人街🏮Barrio Chino de Zanja",
        url="https://t.me/Barrio_Chino_Cuba"
    )
    
    button4 = InlineKeyboardButton(
        text="Biblioteca Instituto Confucio",
        url="https://t.me/bibliotecaicuh"
    )

    otros_servicios = InlineKeyboardButton(
        text="Otros Servicios",
        url="https://telegra.ph/Otros-servicios-11-29"
    )

    contacto = InlineKeyboardButton(
        text="Unete a la botonera",
        url="@DojoTVBot"
    )
    
    
# NOMBRE Y BOTONES DE LA BOTONERA
    update.message.reply_text(
        text='🏮🏮🏮🏮"HONG LONG"🏮🏮🏮🏮',
        reply_markup=InlineKeyboardMarkup([
            [button1, button2],
            [button3, button4],
            [otros_servicios],
            [contacto]
            ])
    )


if __name__ == "__main__":

    token = os.environ['TOKEN']

    bot = telegram.Bot(token=token)

    updater = Updater(token=token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()
