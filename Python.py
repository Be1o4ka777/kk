import discord
from discord.ext import commands




intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')



x1 = ['Пластиковые_бутылки','Пластиковые_упаковки','Одноразовая_пластиковая посуда','Полителеновые_пакеты']
x2 = ['Бумага',"Бумажные_упаковки","Одноразовая_бумажная_посуда"]
x3 = ["Стеклянные_бутылки "]

@bot.command()
async def eco(ctx, my1):
  if my1 in x1:
    await ctx.send("Контейнер для пластика")
  elif my1 in x2:
    await ctx.send("Контейнер для бумаги")
  elif my1 in x3:
    await ctx.send("Контейнер для стекла")
  else:
    await ctx.send("Попробуйте еще раз")

bot.run("")
