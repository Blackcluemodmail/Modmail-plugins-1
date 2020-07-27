import discord
from discord.ext import commands
import asyncio
from datetime import datetime

class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.maincolor = 0x06c9ff
        self.errorcolor = 0xFF0000
        self.log_channel = 737378978410790912 #ID of the log channel
        self.defaultRole = 586643846780158087 #ID of the Discord Member role

    @commands.command(name="send-verify")
    @commands.has_permissions(administrator=True)
    async def sendverifymsg(self, ctx):
        embed = discord.Embed(
            title="**Verification**",
            description="To gain access to the Team Hope Discord Server, you will have to verify.\n\nVerifying means that you have agreed to our Rules and Guidelines\n\nTo verify, please type `verify` in this channel!",
            color=self.maincolor
        )
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        else:
            if message.content.lower() == "verify":
                guild = message.guild
                role = guild.get_role(self.defaultRole)
                await message.author.add_roles(role)
                log_channel = guild.get_channel(self.log_channel)
                await message.add_reactions(":white_check_mark:")
                embed = discord.Embed(
                    title="Someone just verified!",
                    description=f"{message.author.mention} just verified!\n\nHis ID is {message.author.id}\n\nThe message ID is {message.id}\nThe channel ID is {message.channel.id}\nThe message was sent at {message.created_at}",
                    color=self.maincolor
                )
                log_channel.send(embed=embed)
                await asyncio.sleep(2)
                await message.delete()
            else:
                await message.delete()
                return
        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(Verify(bot))