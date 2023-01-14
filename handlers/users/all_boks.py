from aiogram import types
from loader import dp, bot
from keyboards.default.boshlangich_button import boshlangich_button, boshlangich_button_eng





# Essential
@dp.message_handler(text='📚 Essential Books')
async def essintil(msg: types.Message):
    await msg.answer_document("BQACAgIAAxkBAAIBMGOIfmDRmUaeaQRlmiAm0mh4feyqAALGAQACekcwS6AsiKTKcVm2KwQ", caption="📙4000 Essential English Words 1\n\
                                                                                                                    O'zbekcha tarjimasi bilan birga ko'pchilikning e'tiboriga sa'zovor bo'lgan 4000 Essential English Words 1 kitobi")
    await msg.answer_document("BQACAgIAAxkBAAICYWNzb-Lm9DAwT9FdxUY-ml3RyeWKAALHAQACekcwS9RozaVU8iFUKwQ", caption="📙4000 Essential English Words 2\n\
                                                                                                                    O'zbekcha tarjimasi bilan birga ko'pchilikning e'tiboriga sa'zovor bo'lgan 4000 Essential English Words 2 kitobi")
    await msg.answer_document("BQACAgIAAxkBAAICdGNzcH6FOK3yQOS4vYqxQVzTMfT2AAKmCwACDHqJShXBqCT3Jor8KwQ", caption="📙4000 Essential English Words 3\n\
                                                                                                                    O'zbekcha tarjimasi bilan birga ko'pchilikning e'tiboriga sa'zovor bo'lgan 4000 Essential English Words 3 kitobi")
    await msg.answer_document("BQACAgIAAxkBAAICTWNzbvK6mU6crwTs7ipSOMKXymrMAAKaFQACDpERSr5K8siTiMKrKwQ", caption="📙4000 Essential English Words 4\n\
                                                                                                                    O'zbekcha tarjimasi bilan birga ko'pchilikning e'tiboriga sa'zovor bo'lgan 4000 Essential English Words 4 kitobi")
    await msg.answer_document("BQACAgIAAxkBAAICP2Nzbj3b7uTs8fCpJUZ5YcVqUQABRgACqAsAAgx6iUrnz7-Inr-E6ysE",caption="📙4000 Essential English Words 5\n\
                                                                                                                    O'zbekcha tarjimasi bilan birga ko'pchilikning e'tiboriga sa'zovor bo'lgan 4000 Essential English Words 5 kitobi")
    await msg.answer_document("BQACAgIAAxkBAAICZWNzcAhXdYL6NGjposTnDsxFmhJsAAKpCwACDHqJStperVwWd60AASsE",caption="📙4000 Essential English Words 6\n\
                                                                                                                    O'zbekcha tarjimasi bilan birga ko'pchilikning e'tiboriga sa'zovor bo'lgan 4000 Essential English Words 6 kitobi")



# Reading
@dp.message_handler(text='📚 Reading Books')
async def reading(msg: types.Message):
    await msg.reply_document('BQACAgIAAxkBAAIBbWOIgmRHoc7x1LNCaoWUPDb0fwsFAALCCwAC8nJ5SHbMcfdPbOoTKwQ', caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")
    await msg.reply_document('BQACAgIAAxkBAAIBd2OIgoEAAWBEE7zOpP-ZFafTWIfAhAACvg8AAi4EMEgAAbKF8bTnulgrBA', caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")
    await msg.reply_document('BQACAgIAAxkBAAIBeWOIgpfYWztmM17DP0tIMa2eyTTGAALBCwAC8nJ5SAoagYO2cRPwKwQ', caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")
    await msg.reply_document('BQACAgIAAxkBAAIBe2OIgqoki-v2a79JVY2qbg4QlfVsAAKVGwACxij4Sf632oE8zGOAKwQ', caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")
    await msg.reply_document('BQACAgIAAxkBAAIBfWOIg0dt663pVCBNygQqqYfIRnRrAAK9CwAC8nJ5SMmiUNmtXdCGKwQ', caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")
    await msg.reply_document('BQACAgIAAxkBAAIBgWOIg5aXZs0kivsaRYLZytebVQWmAALBCwAC8nJ5SAoagYO2cRPwKwQ', caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")
    await msg.reply_document('BQACAgIAAxkBAAIBg2OIg65-vMVeU7vyAyyG0uNMlE2pAALCCwAC8nJ5SHbMcfdPbOoTKwQ', caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")
    await msg.reply_document('BQACAgIAAxkBAAIBf2OIg3VH9RIRVywZwOlpIdr35HlWAAK-CwAC8nJ5SI-22Yb7Uqk1KwQ', caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")
    await msg.answer('OFA eng zo\'ri😉')



# IELTS
@dp.message_handler(text='📚 IELTS Books')
async def ielts(msg: types.Message):
    await msg.reply_document('BQACAgIAAxkBAAIBKGOIfiI58yYlShgezYCptIshn8eqAAIGBgACCIZZSFy9RLZCfHD9KwQ', caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")
    await msg.reply_document('BQACAgIAAxkBAAIBLGOIfjYo8B8gojozvhGiRZaz-uHdAAIGBgACCIZZSFy9RLZCfHD9KwQ', caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")
    await msg.reply_document('BQACAgQAAxkBAAOlY4hzWVE4-impMU-XjCVS0rN7X7wAAvAMAALF-PFSbIx9MXM7fUQrBA', caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")
    await msg.reply_document('BQACAgQAAxkBAAOsY4hzbiUaH7CB3bwyDohjLF1GrdYAAvEMAALF-PFShOD2ZxXdEdwrBA', caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")
    await msg.reply_document('BQACAgQAAxkBAAOwY4hzmoXPJZCoz5yeQ3-VC0fdKkoAAgENAALF-PFSMUXXMyqoqXsrBA', caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")
    await msg.reply_document('BQACAgQAAxkBAAOyY4hzqA13DNsVMbdQ01qQmCNGKXYAAgINAALF-PFSh_TfQfmS1PIrBA', caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")
    await msg.reply_document('BQACAgIAAxkBAAO0Y4hzyScLVNdgRatn04fBKMZjlaYAAmYWAAJAJEBKIUkYg1JDh8YrBA', caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")






# Tests
@dp.message_handler(text='📚 English Tests')
async def test(msg: types.Message):
    await msg.reply_document('BQACAgIAAxkBAANXY4hnvnU-X31jZGcZFVPi7RlcEpwAAtkUAALnQJlI0Mf-bjsYlA0rBA', caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊") 
    await msg.reply_document('BQACAgIAAxkBAAN4Y4hn9yxniPeieQ0U6tK_9zIEAAG0AALIGwACSPtQSoiLUQnxbJgBKwQ',  caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊") 
    await msg.reply_document('BQACAgIAAxkBAAN6Y4hoEt5R4A85DIjJzvG13KFDDusAAnogAAK5lwABSZBaQcTL8yZ0KwQ',  caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊") 
    await msg.reply_document('BQACAgIAAxkBAAN_Y4ho8c_PmvtzAl6HPNUge1h1_ZkAAoogAAK5lwABSeuFYM22pPuDKwQ',  caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊") 
    await msg.reply_document('BQACAgIAAxkBAAOBY4hpOLbLXerMbiOY1ZrZZ-dVCoIAAp4gAAK5lwABSdSbIYR1bFOXKwQ',  caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")
    await msg.reply_document('BQACAgIAAxkBAAOSY4hw_WAlilMRjyjR-BQjvfdd2toAAu0cAAKeO1hJ8I0GXSGlZDorBA',  caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")
    # await msg.reply_document('',  caption="t.me/Osiyo_fanlar_akademiyasi 👈 😊")
    # await msg.reply_document('',  caption="\nSuper TEST!\n🧪All tests Here\n📑818 Pages")
    





# Collocations
@dp.message_handler(text='📚 Collocation Books')
async def collocation(msg: types.Message):
    await msg.answer('Siz Collocation Books-dasiz!')
    await msg.reply_document('BQACAgIAAxkBAAOWY4hyLIjhiUx7ZvaSdVhygi2i5f4AAkAKAALm04lIUPygSjh_u2IrBA')
    await msg.reply_document('BQACAgIAAxkBAAOdY4hyoG_z_A6tgPI2qviP-Z86rmYAAvEYAAIs5aBILEvflPpU3sMrBA')
    await msg.reply_document('BQACAgIAAxkBAAOfY4hzAaIFzVXGRXYsIxIG4qNjH9UAAmIWAAJAJEBKjpYUc36i_i0rBA')
    await msg.reply_document('BQACAgIAAxkBAAOhY4hzFSolngABKfogCDuPXhrzWqGOAAJkFgACQCRAStzo_F_IjtiDKwQ')        
    await msg.reply_document('BQACAgIAAxkBAAOjY4hzPU4Dp1mFzyeZEGpsNeaEMT0AAmYWAAJAJEBKIUkYg1JDh8YrBA') 
    await msg.reply_document('BQACAgIAAxkBAAO0Y4hzyScLVNdgRatn04fBKMZjlaYAAmYWAAJAJEBKIUkYg1JDh8YrBA')
    











@dp.message_handler(text='🔙Orqaga')
async def back(msg: types.Message):
    await msg.answer('Bosh bo\'limdasiz!', reply_markup=boshlangich_button)





# English
@dp.message_handler(text='🔙Back')
async def back(msg: types.Message):
    await msg.answer('You are in the main section!', reply_markup=boshlangich_button_eng)











@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def cmd_se(message: types.Message):
    await message.answer(message.document.file_id)




