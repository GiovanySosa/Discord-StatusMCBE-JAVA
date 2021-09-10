import discord
import os
from dotenv import load_dotenv
from mcstats import mcstats

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command()
async def status(ctx,):
    host = 'yourip'
    port = 19132 #yourport
    q = Query(host, port)
    data = q.query()
    online = data.num_players
    max = data.max_players
    jugadores = str(data.players)
    
    

    embed = discord.Embed(title="MonsterNetwork", description=f"**IP:** {host} **PUERTO:** {port}",color=discord.Color.random())
    
    embed.add_field(name="HCF:", value=f"*ACTIVOS:** {online} **de** {max} \n \n **JUGADORES:** {jugadores}", inline=False)
    
    embed.add_field(name="**invita a tus amigos**", value='[**TOCA AQUI PARA INVITAR**](linkinviteordiscord)')
    
    embed.set_footer(text=f" **juega y divierte te!!** ")

    await channel.send(embed=embed)
    print(jugadores)






bot.run(TOKEN)
