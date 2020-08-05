import discord
from discord.ext import commands

class Test1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def send_s(self, ctx):
        embed = discord.Embed(
            title="***7 SIN'S SOCIALS***\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬",
            description=":instagram: **Instagram:**\n• <https://www.instagram.com/7sins.ggs>\n\n:youtube: **YouTube:**\n• <https://www.youtube.com/channel/UCrA0fNlbVXKoA1eSu8YsYhA/featured>\n\n:twitter: **Twitter:**\n• <https://twitter.com/7soffical>\n\n:discord: **Discord:**\n• <https://discord.gg/MwVC2AR>",
            color=0xee3463,
            timestamp=ctx.message.created_at
        )
        embed.set_footer(text="Management Team", icon_url="https://cdn.discordapp.com/attachments/726193232798810132/740629657191186562/7S-.gif")
        await ctx.send(embed=embed)
        
        
def setup(bot):
    bot.add_cog(Test1(bot))