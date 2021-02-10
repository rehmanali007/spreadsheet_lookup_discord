from discord.ext.commands import Bot
import json

f = open('config.json', 'r')
config = json.load(f)

bot = Bot(command_prefix='-')

BOT_TOKEN = config.get("BOT_TOKEN")


@bot.event
async def on_ready():
    print('[+] We have logged in as {0.user}'.format(bot))
    print('[+] Bot is now ready!')

extensions = ['lookups']
for ext in extensions:
    bot.load_extension(f'Cogs.{ext}')
bot.run(BOT_TOKEN)
