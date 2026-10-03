import discord
from discord.ext import commands
from discord import ui, ButtonStyle, TextStyle
from config import TOKEN

class TestModal(ui.Modal, title='Judul Test'):
    field_1 = ui.TextInput(label='Teks Pendek')
    field_2 = ui.TextInput(label='Teks Panjang', style=TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.edit_message(content=f'Teks Pendek: {self.field_1.value}\n'
                                                       f'Teks Panjang: {self.field_2.value}')

class TestButton(ui.Button):
    def __init__(self, label="Tombol Test", style=ButtonStyle.blurple, row=0):
        super().__init__(label=label, style=style, row=row)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(TestModal())

        self.style = ButtonStyle.gray

        try:
            await interaction.user.send("Kamu telah menekan tombol")
        except discord.Forbidden:
            pass
        await interaction.message.channel.send("Kamu telah menekan tombol")

class TestView(ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(TestButton(label="Tombol Test"))

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Berhasil login sebagai {bot.user}')

@bot.command()
async def test(ctx):
    await ctx.send("Tekan tombol di bawah ini:", view=TestView())

bot.run(TOKEN)
