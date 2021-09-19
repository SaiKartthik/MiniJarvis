import discord
import random
import asyncio
from webserver import keep_alive
from decouple import config
# from youtube_dl import YoutubeDL
from discord.ext import commands

client = commands.Bot(command_prefix='jarvis ')

list = ["Hello !","I am not in a mood","Shut Up !","Kaise ho aap log .. ?","Will you please give me some rest ... ","How are you ? ","Wait...",".....","he--\nhe--\nhe--\nhe--\nhe--\nhe--\nhello","Aah Sheet here we go again","Calling 100","Hi there","Howdy","Greetings","Hey, What’s up?","Morning/afternoon/evening","What’s going on?","Hey! There she/he is","How’s everything?","How are things?","Good to see you","Great to see you","Nice to see you","Tata bye bye"]

beliefslist = ["If you donot forward this message within 24 hours ,you will die","Many Problems ,One solution \nKanakaDurga Jyothishyalayam"]

rpsList = ["r","p","s"]

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def helps(ctx):
    await ctx.send("Commands available are \nhello : Welcoming  \nrps : play rock paper scissors eg.jarvis rps and follow instructions \nbeliefs : trash talking eg.jarvis beliefs\ncopycat\nsayhelloto : says what u say eg : jarvis copycat helloman\nDon't forget to include 'jarvis ' before commands ")

@client.event
async def on_command_error(ctx, error):
        if isinstance(error,commands.MissingRequiredArgument):
                await ctx.send("Whom should I roast ,You dumb ")
@client.command()
async def sayhelloto(ctx,a):
  list1 = ["Hello !"+a,"I am not in a mood anyway hii"+a,"Kaise ho aap  .. "+a,"How are you "+a+"?","Okay.....hii "+"a","he--\nhe--\nhe--\nhe--\nhe--\nhe--\nhello "+a,"Aah Sheet here we go again anyway hii "+a,"Hi there "+a,"Howdy "+a,"Greetings "+a,"Hey, What’s up? "+a,"Morning/afternoon/evening "+a,"What’s going on "+a+"?","Hey! There she/he is "+a,"How’s everything "+a+"?","How are things "+a+" ?","Good to see you "+a+"?","Great to see you "+a,"Nice to see you "+a+"?","Tata bye bye...wait hello "+a]
  await ctx.send(random.choice(list1))

@client.command()
async def add(ctx, a, b):
        c = int(a) + int(b)
        x = str(c)
        # await ctx.send("from replit")
        if c < 30:
            await ctx.send("The answer is "+x+"\n btw you are so dumb that you can't even calculate sum of these small numbers ")
        else :
            await ctx.send("The answer is "+x)

@client.command()
async def roast(ctx,a):
    print(a)
    if a == "<@!740600494149599284>" or a == "<@740600494149599284>" or a == "<@!774888738039922708>" or a == "<@774888738039922708>":
        await ctx.send("We dont do that here !")

    else:
      if(a[1] == "@"):
          rstl=[a+" STFU", "Keep quiet!, "+a, "This stupid dog "+a+" is very lazy.", a+", as a BOT even I am better than you!!","I don't know why God created "+a+",when there is already enough shit on Earth","When I peed today ,I saw "+a+"'s face :poop:","You are not eligible to get roasted even by a BOT","I am tired of roasting"+a,a + " STFU!!", "Keep quiet!, " + a, "This stupid dog " + a + " is very lazy.",a + ", as a BOT even I am better than you!!",a + " some day you will be lord of PIGS!!!", a + " you are just nothing.",a + " you smell like a pig!", "What kind of alien are you?, " + a,a + ", if I want to kill myself I'd climb your ego and jump to your IQ","I love what you've done with your hair.How do you get it to come out of nostrils like that?, " + a, a + ", I like you roasting you rather than doing other stuff- "]
          await ctx.send(random.choice(rstl))
      elif a == " ":
          await ctx.send("Enter some name")
      else:
          await ctx.send("You need to mention a person ,not your dream girl that dne")

@client.command()
async def kill(ctx,a):
  if(a[1] == "@"):
          killlist=[a + " was stabbed by Jason 100 times :knife::drop_of_blood:", a + " is attacked by an ant:ant:"
            , a + " was shot by peashooter.", a + " looked at Enderman and died...",
              "Pillager killed " + a + " with a crossbow."
            , a + " tried to hold his breath for long time and then died.",
              a + " tried to eat puffer fish and then died..."
            , a + " was eaten by a flerkin."
            , a + " tried to fly in the space but was hit by a meteor.", "John Wick is looking for " + a,"Ant-man entered " + a + " ear and expands bursting " + a + " head into pieces."
            , a + " was stomped by Mario.", a + " was eaten by Venom", "Ghost Rider used death stare on " + a, a + " tried to drink lava and dies.", a + " was bitten by a zombie.",
              "To become spider-man " + a + " tried to get bitten by a spider."
            , a + " died in hardcore minecraft while fighting with an Ender dragon.", a + " fell in the void."
            , a + " was arrested by FBI."]
          await ctx.send(random.choice(killlist))
  elif a == " ":
          await ctx.send("Enter some name")
  else:
          await ctx.send("You have to mention someone")

@client.command()
async def copycat(ctx,arg):
    await ctx.send(arg)


@client.command()
async def hello(ctx):
    await ctx.send(random.choice(list))

@client.command()
async def beliefs(ctx):
    await ctx.send(random.choice(beliefslist))

@client.command()
async def rps(ctx):
    await ctx.send("Just type r for rock or p for paper or s for scissors within 30 seconds\nNote : small letters only")
    n = random.choice(rpsList)
    try :
        message = await client.wait_for("message",check= lambda m :m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
    except asyncio.TimeoutError:
        await ctx.send("Why you bully me \nYou didn't reply in time\nRepeat the command to play again")
    if n == "r" and message.content.lower() == "p" :
        await ctx.send("You Won | Bot's pick is Rock")
    elif n == 'r' and message.content.lower() == 's' :
        await ctx.send("Bot Won | Bot's pick is Rock")
    elif n == 'p' and message.content.lower() == 's':
        await ctx.send("You Won | Bot's pick is Paper")
    elif n == 'p' and message.content.lower() == 'r':
        await ctx.send("Bot Won | Bot's pick is Paper")
    elif n == 's' and message.content.lower() == 'r':
        await ctx.send("You Won | Bot's pick is Scissors")
    elif n == 's' and message.content.lower() == 'p':
        await ctx.send("Bot Won | Bot's pick is Scissors")
    elif n == message.content.lower() :
        await ctx.send("We both picked same")

keep_alive()
key = config('TOKEN')
client.run(key)
