# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
# from tele import func

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello, \n what's your currency :')

# async def currency (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     exchange =  update.message.text
#     home = func(exchange)
#     await update.message.reply_text(home)




# app = ApplicationBuilder().token("5548428639:AAGDNK2p84XeyZLq_Ot-j5fatjenYO-TLGk").build()

# app.add_handler(CommandHandler("start", start))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,currency))

# app.run_polling()




from telegram import Update #qayerdan telegram  import yangilash
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    CallbackQueryHandler
)

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from tele import get_rates # qayerdan functions file nomi  import get_rates funksyasi


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("🇺🇸 USD/UZS", callback_data="USD"),
            InlineKeyboardButton("🇹🇷 TRY/UZS", callback_data="TRY"),
        ],
        [
            InlineKeyboardButton("🇪🇺 EUR/UZS", callback_data="EUR"),
            InlineKeyboardButton("🇰🇿 KZT/UZS", callback_data="KZT"),
        ],
         [
            InlineKeyboardButton("🇷🇺 RUB/UZS", callback_data="RUB"),
        ],
       
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"Hello {update.message.from_user.first_name} \nSelect a currency: ",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.message.delete()
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🇺🇸 USD/UZS", callback_data="USD"),
            InlineKeyboardButton("🇹🇷 TRY/UZS", callback_data="TRY"),
        ],
        [
            InlineKeyboardButton("🇪🇺 EUR/UZS", callback_data="EUR"),
            InlineKeyboardButton("🇰🇿 KZT/UZS", callback_data="KZT"),
        ],
         [
            InlineKeyboardButton("🇷🇺 RUB/UZS", callback_data="RUB"),
        ],
       
    ]   
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    rate = get_rates()[query.data]["Rate"]
    await query.message.reply_text(text=f"1 {query.data} to {rate} UZS", reply_markup=reply_markup)
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"what kind of help do you need appeal @Utkirbek4Edu") 
    query = update.callback_query
    await query.message.delete()
    await query.answer()
    keybord = [
        [
            InlineKeyboardButton("@Utkirbek4Edu", callback_data="@Utkirbek4Edu")
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keybord)


app = (
    ApplicationBuilder().token("5548428639:AAGDNK2p84XeyZLq_Ot-j5fatjenYO-TLGk").build()
)

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
# app.add_handler(CommandHandler("", ))
# app.add_handler(CommandHandler("", ))
# app.add_handler(CommandHandler("", ))
# app.add_handler(CommandHandler("", ))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()