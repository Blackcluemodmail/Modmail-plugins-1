import asyncio
import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel


class Moderation(commands.Cog):
    """
    Commands to moderate your server.*
    NOTE: You will need the moderator permission
    level in order to run any of these commands.*_ _
    """

    def __init__(self, bot):
        self.bot = bot
        self.db = bot.api.get_plugin_partition(self)

    async def cog_command_error(self, ctx, error):
        """Checks errors"""
        error = getattr(error, "original", error)
        if isinstance(error, commands.CheckFailure):
            return await ctx.send(
                embed=discord.Embed(
                    title="Error",
                    description="You don't have enough permissions to run this command!",
                    color=discord.Color.red(),
                ).set_footer(text="Are you a moderator?")
            )
        raise error
 
    @commands.command(name="pban", aliases=['fban'] 
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def fban(self, ctx, member: discord.Member = None, reason = None):
        await ctx.message.delete()
        if not member:
            embed = discord.Embed(title="Error", description="Please provide a user to ban!", color=self.bot.error_color)
            await ctx.send(embed=embed)
        else:
            if not reason:
                embed = discord.Embed(title="Ban", description=f"{member.mention} Has been banned!", color=self.color)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Ban", description=f"{member.mention} Has been banned for {reason}!", color=self.color)
                await ctx.send(embed=embed)           
        
def setup(bot):
    bot.add_cog(fakeBan(bot))
