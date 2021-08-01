from discord.ext import commands
import discord

class WelcomeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        print(msg.content)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        await member.send(f"Welcome to the server {member.display_name}")
