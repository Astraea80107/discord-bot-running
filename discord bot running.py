# python版本至少3.11以上
# 使用discord.py 模組，此版本為2.2.3
import discord
#commands為discord.py 模組中的子函式，用於處理機器人的指令
from discord.ext import commands

#token為discord提供給機器人的身分識別，同時用於將機器人連結至discord伺服器
token = "your_discord_bot_token" #填入discord bot提供的token

#新版discord.py所新增的指令，用於設定機器人的意圖，若未設定機器人則無法運作
#設定一個對象，表示機器人的意圖，並以default()將其設置為預設狀態
intents = discord.Intents.default()

#將用戶的輸入狀態及上線狀態設為False，使機器人不受其影響，減少機器人的負擔
intents.typing = False
intents.presences = False

#建立一台Bot，並以"!"作為命令前綴詞，並以該機器人為意圖對象
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event # 指機器人的運作事件
#設定on_ready指令，當機器人成功登入discord伺服器，並可正常運作時，出現上線提示
async def on_ready():
    print(f"Bot已成功登錄為 {bot.user.name}")

@bot.command() # 指機器人的運作事件
#設定hello指令，當用戶輸入"!hello"時，會回應用戶的訊息
async def hello(ctx):
    await ctx.send("你好！我是一台Discord機器人！")

#啟動機器人，並利用token連結至discord伺服器
bot.run(token)
