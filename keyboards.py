from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Temir odam", callback_data="Temir odam"),
     InlineKeyboardButton("Ajoyib Hulk", callback_data="Ajoyib Hulk")],

    [InlineKeyboardButton("Temir odam 2", callback_data="Temir odam 2"),
     InlineKeyboardButton("Tor", callback_data="Tor")],

    [InlineKeyboardButton("Kapitan Amerika: Birinchi qahramon", callback_data="Kapitan Amerika: Birinchi qahramon"),
     InlineKeyboardButton("Avengers (Qahramonlar jamoasi)", callback_data="Avengers")],

    [InlineKeyboardButton("Temir odam 3", callback_data="Temir odam 3"),
     InlineKeyboardButton("Tor: Qorong'u olam", callback_data="Tor: Qorong'u olam")],

    [InlineKeyboardButton("Kapitan Amerika: Qishki askar", callback_data="Kapitan Amerika: Qishki askar"),
     InlineKeyboardButton("Galaktikaning qo‘riqchilari", callback_data="Galaktikaning qo‘riqchilari")]
])