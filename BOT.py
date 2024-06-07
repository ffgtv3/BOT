import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

# Словарь для хранения количества сообщений от каждого пользователя
message_counts = {}

@bot.event
async def on_ready():
    print('Бот готов')

@bot.event
async def on_message(message):
    # Игнорируем сообщения от ботов
    if message.author.bot:
        return

    # Получаем ID автора сообщения
    author_id = message.author.id

    # Увеличиваем счетчик сообщений для данного пользователя
    message_counts.setdefault(author_id, 0)
    message_counts[author_id] += 1

    # Проверяем, если пользователь отправил более 5 сообщений за короткий промежуток времени
    if message_counts[author_id] > 5:
        await message.channel.send(f"{message.author.mention}, перестаньте спамить!")

    await bot.process_commands(message)

# Запускаем бота
bot.run('MTI0NjM5MjU0MTIzMDY2MTY5Ng.G72oSK.0lzy2sgqgJxlo6cBffX66DgWfhs4T23a9CBKrM')
