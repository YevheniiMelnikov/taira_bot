from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

    
main_menu = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text='Задать вопрос', url='https://t.me/GargaevaTaira'),
    InlineKeyboardButton(text='Тест на базовые дефициты', url='https://telegra.ph/TEST-NA-BAZOVYE-DEFICITY-09-06'),
    InlineKeyboardButton(text='Тест: «КОЛЕСО ПИЩЕВОГО БАЛАНСА»', url='https://telegra.ph/Test-KOLESO-PISHCHEVOGO-BALANSA-09-06'),
    InlineKeyboardButton(text='Рекомендации по рациону', url='https://telegra.ph/REKOMENDACII-PO-RACIONU-08-29'),
    InlineKeyboardButton(text='Список продуктов', url='https://telegra.ph/Produkty-dlya-pravilnogo-pitaniya-08-29'),
    InlineKeyboardButton(text='Рекомендации по чек-апу', url='https://telegra.ph/LABORATORNYJ-CHEK-AP-18-08-29'),
    InlineKeyboardButton(text='О биоритмах', url='https://telegra.ph/BIORITMY-09-06'),
    InlineKeyboardButton(text='Обо мне', url='https://telegra.ph/Privet-vsem-uchastnikam-proekta-08-29-2'))
    

