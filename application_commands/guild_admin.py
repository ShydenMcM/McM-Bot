from discord import Embed, Interaction, app_commands


class Admin(app_commands.Group):
    pass


admin = Admin(description="Administrative actions")


@admin.command()
async def ping(interaction: Interaction):
    """Displays the latency in ms;
    good (green),
    acceptable (orange),
    bad (red)"""
    rounded_latency_time = round(interaction.client.latency * 1000)
    if rounded_latency_time <= 50:
        colour = 0x44FF44
    elif rounded_latency_time <= 150:
        colour = 0xFF6600
    else:
        colour = 0x990000
    embed = Embed(
        title="PONG",
        description=f":ping_pong: The ping is **{rounded_latency_time}** milliseconds!",
        color=colour,
    )

    await interaction.response.send_message(embed=embed)


async def setup(bot):
    bot.tree.add_command(admin)
