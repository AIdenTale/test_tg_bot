async def first_time_handler(message, state):
    await state.finish()

    await message.answer("Привет")

def setup_handler(dp):
    dp.register_message_handler(first_time_handler, commands=['start'], state="*")