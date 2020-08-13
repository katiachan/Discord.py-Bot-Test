# This code makes the bot join and leave the voice channel


@client.command( brief="Makes KateBot join your channel")
async def join(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("I wanted to put that before, but there's no connection to a channel.")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await voice.disconnect()
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.send(f"I'm IIIN!!! \n Joined '{channel}' channel")
    

@client.command( brief="Makes KateBot leave your channel", aliases=['quit'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send("Got a valet, gotta leave...")
    else:
        await ctx.send("Don't think I am the one in a voice channel")
