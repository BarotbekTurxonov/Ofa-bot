from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN ="BOT TOKEN HERE"     # Забираем значение типа str
ADMINS =   [5235865310, 1635920175]    
                                     # Тут у нас будет список из админов
CHANNEL = [-1001710909528]
