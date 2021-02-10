from discord.ext import commands
from discord import Embed
from exts.spreadsheets import Sheet


class Lookups(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sheet = Sheet()

    @commands.command(name='lookup')
    async def lookup(self, ctx, *, search_term: str):
        servers = self.sheet.search(search_term)
        e = Embed(title='Search Results')
        message = ''
        for server_number in servers:
            message = f'{message}\n{search_term} was found in server {server_number}.'
        if message == '':
            message = f'No Results for {search_term}'
        e.description = message
        await ctx.send(embed=e)

    @lookup.error
    async def lookup_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send('Search term is missing!')
            return
        raise error


def setup(bot):
    bot.add_cog(Lookups(bot))
    print('[+] Lookups extension has been loaded!')
