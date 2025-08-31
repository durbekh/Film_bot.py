import asyncio
from aiogram import Bot, Dispatcher, types
from film_keyboard import keyboards  

API_TOKEN = "..." 

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(
        "Marvel filmlari haqida ma'lumot olish uchun quyidagi filmlardan birini tanlang:",
        reply_markup=keyboard
    )

@dp.callback_query_handler(text="Temir odam")
async def temir_odam(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo="https://upload.wikimedia.org/wikipedia/en/0/00/Iron_Man_poster.jpg",
        caption="Temir odam (Iron Man)\n\nBatafsil: https://uz.wikipedia.org/wiki/Iron_Man_(film)"
    )
    await callback.answer()

@dp.callback_query_handler(text="Ajoyib Hulk")
async def hulk(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo="https://upload.wikimedia.org/wikipedia/en/8/88/The_Incredible_Hulk_poster.jpg",
        caption="Ajoyib Hulk\n\nBatafsil: https://uz.wikipedia.org/wiki/The_Incredible_Hulk_(film)"
    )
    await callback.answer()

@dp.callback_query_handler(text="Temir odam 2")
async def temir_odam_2(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo="https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
        caption="Temir odam 2\n\nBatafsil: https://uz.wikipedia.org/wiki/Iron_Man_2"
    )
    await callback.answer()

@dp.callback_query_handler(text="Tor")
async def tor(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo="https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
        caption="Tor\n\nBatafsil: https://uz.wikipedia.org/wiki/Thor_(film)"
    )
    await callback.answer()

@dp.callback_query_handler(text="Kapitan Amerika: Birinchi qahramon")
async def kapitan_birinchi(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo="https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
        caption="Kapitan Amerika: Birinchi qahramon\n\nBatafsil: https://uz.wikipedia.org/wiki/Captain_America:_The_First_Avenger"
    )
    await callback.answer()

@dp.callback_query_handler(text="Avengers")
async def avengers(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo="https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
        caption="Avengers\n\nBatafsil: https://uz.wikipedia.org/wiki/The_Avengers_(2012_film)"
    )
    await callback.answer()

@dp.callback_query_handler(text="Temir odam 3")
async def temir_odam_3(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo="https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",
        caption="Temir odam 3\n\nBatafsil: https://uz.wikipedia.org/wiki/Iron_Man_3"
    )
    await callback.answer()

@dp.callback_query_handler(text="Tor: Qorong'u olam")
async def tor_qorongu(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo="https://upload.wikimedia.org/wikipedia/en/7/7e/Thor_The_Dark_World_poster.jpg",
        caption="Tor: Qorong'u olam\n\nBatafsil: https://uz.wikipedia.org/wiki/Thor:_The_Dark_World"
    )
    await callback.answer()

@dp.callback_query_handler(text="Kapitan Amerika: Qishki askar")
async def kapitan_qishki(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo="https://upload.wikimedia.org/wikipedia/en/2/2e/Captain_America_The_Winter_Soldier_poster.jpg",
        caption="Kapitan Amerika: Qishki askar\n\nBatafsil: https://uz.wikipedia.org/wiki/Captain_America:_The_Winter_Soldier"
    )
    await callback.answer()

@dp.callback_query_handler(text="Galaktikaning qo‘riqchilari")
async def galaktika(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo="https://upload.wikimedia.org/wikipedia/en/b/b5/Guardians_of_the_Galaxy_poster.jpg",
        caption="Galaktikaning qo‘riqchilari\n\nBatafsil: https://uz.wikipedia.org/wiki/Guardians_of_the_Galaxy_(film)"
    )
    await callback.answer()


@dp.callback_query_handler(text="Ortga")
async def back(callback: types.CallbackQuery):
    await callback.message.answer(
        "Ortga qaytdingiz. Quyidagi filmlardan birini tanlang:",
        reply_markup=keyboard
    )
    await callback.answer()

async def main():
    dp.include_router(dp)       
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
