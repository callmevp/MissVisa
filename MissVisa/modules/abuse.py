import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from MissVisa import dispatcher
from MissVisa.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "Jaa na Bsdk, gaand mara jaake.",
    "Tu paidaishi chutiya hai ki koi course kiya hai? ",
    "I came to know that some shops were selling your ass for 69$",
    " TERI MAA KE BHOSDE MEI GITHUB DAL KE APNA BOT HOST KARUNGAA 🤩👊👤😍",
    "TERI MAA KE BHOSDE ME AC LAGA DUNGA SAARI GARMI NIKAL JAAYEGI",
    " TERI VAHEEN KO HORLICKS PEELAUNGA MADARCHOD😚",
    "MADARCHOD TERI MAA KI CHUT ME GHUTKA KHAAKE THOOK DUNGA 🤣🤣",
    "SUN SUN SUAR KE PILLE JHANTO KE SOUDAGAR APNI MUMMY KI NUDES BHEJ",
    "GALI GALI NE SHOR HE TERI MAA RANDI CHOR HE 💋💋💦",
    "The world would have been so smooth if your dad had just pulled out",
    "And the truth is, you're a fucking cunt",
    "What else can you do other than spreading your legs?",
    "Jaa na Gandu",
    "Aand ka na Gaand ka, Gyaan jhaare pure Brahmand ka",
    "Dhaat teri maa ki ch*t",
    "Gaand se tatti nikalke jaadugar samajhta hai apne aap ko?",
    "Bitches be trippin'",
    "Please fuck off bitch, and get a life",
    "Tu aise nhi maanega - Mat maan, maa chuda",
    "Tujhse zada sundar teri jali hui gaand hai",
    "Ye aapki Randikhana nhi hai, kripya yaha se dur rahe",
    "I'm a good girl, I don't abuse. But you're a bitch."
  )

@run_async
def dark(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /dark  🤬.
"""

__mod_name__ = "Abuse"

DARK_HANDLER = DisableAbleCommandHandler("dark", dark)

dispatcher.add_handler(DARK_HANDLER)