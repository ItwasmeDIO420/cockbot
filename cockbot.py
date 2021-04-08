import discord
import os
import random

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


insult = ["ya nan gay", "your dad lesbian", "youre a vegetable", "idiotic prick biscuit", "pie-eating bitch dragon",
          "ya pp only 55cm but mine is 5", "YO MAMA'S GOT SO MUCH WEAVE, WHEN A FLY GOES BY HER HAIR SWATS AT IT",
          "YO MAMA IS SO UGLY THAT HER BIRTH CERTIFICATE CONTAINED AN APOLOGY LETTER FROM THE CONDOM FACTORY",
          "YOU'RE AS USELESS AS A WOODEN FRYING-PAN",
          "YO MAMA IS SO NASTY THAT EVERY TIME SHE OPENS HER MOUTH SHE'S TALKING SHIT",
          "YO MAMA IS SO NASTY THAT EVERY TIME SHE OPENS HER MOUTH SHE'S TALKING SHIT",
          "YO MAMA'S TEETH ARE SO YELLOW THAT TRAFFIC SLOWS DOWN WHEN SHE SMILES!", "your mom",
          "YO MAMA IS SO STUPID THAT SHE GOT FIRED FROM THE M&M FACTORY FOR THROWING AWAY ALL THE W'S",
          "I'M NOT SAYING YOU'RE FAT, BUT IT LOOKS LIKE YOU WERE POURED INTO YOUR CLOTHES AND SOMEONE FORGOT TO SAY STOP",
          "people clap when they see you,clap their hands over their eyes", "your STUPID", "Fattie",
          "8=====================D = me,8=D = you",
          "youre as useful as having Stephen Hawking back me up in a pub fight", "ya forehead huge"]

rush = [
    "ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA",
    "MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA",
    "DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA DORA",
    "ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRI ARRIVEDERCI",
    "WANNNNNNNNNNNNNNAAAAAAAAAAAAAAAAA BEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE",
    "VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLA VOLARE VIA",
    "PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS PASS",
    "HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA HORA",
    "YAAAAAAAAAAAAAAAAAAAAAAAAAROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOGAAAAAAA",
    "CHIBABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABA"]


def rushRng():
    return random.randint(0, len(rush) - 1)


def insultRng():
    return random.randint(0, len(insult) - 1)

    return random.ran


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send("Woah Nice Cock")

    if message.content.startswith("$stand fight"):
        await message.channel.send(rush[rushRng])

    if message.content.startswith("thanks bro"):
        await message.channel.send("no problem bro,its an 8.5 outta 10")

    if message.content.startswith('$this is requiem'):
        await message.channel.send(
            "What youre seeing is indeed the truth. You are seeing the movements created by your abilities, but you will NEVER arrive at the truth thats going to happen. None who stand before me shall ever get there, regardless of their abilities. This is the power of Gold Experience Requiem!")

    if message.content.startswith('$inspire'):
        await message.channel.send(insult[insultRng()])
    if message.content.startswith("$roast me"):
        await message.channel.send(insult[insultRng()])


client.run(os.getenv('TOKEN')) 