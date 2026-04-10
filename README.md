I think my first idea will be in teachable machine i will first start with an image project,
so firstly a user sends an image to an AI and the AI identifies the waste item then AI tells
the bot how to dispose of it properly.

What my bot is going to be doing when its finished?
My bot helps people learn how to correctly dispose of waste, reducing recycling contamination and supporting climate.
It includes facts that people can get and learn from. 
Image recognition for identifying waste items, so people can identify diffrent wastes and where they go.

I will aslo include commands that the user will use:

/dispose battery
/dispose plastic
/dispose glass
/dispose paper
/dispose food

How its going to be
User types:
/dispose battery
Bot responses:
Batteries should be always thrown into the battery recycling points or recycling centres these are usually found in big shops/malls example Aldi/Lidl/tesco.
Do not throw them in normal bins.

iwill also include some extra commands like:
/tip tells you a random recycling tip
/help lists all commands
/fact tells you a fun climate/recycling fact

How im going to try organize my project.
1)
Set up Discord bot and the teachable machine in visual studio code and also import everything i need to make my discord bot.
2)
Make all text commands work.
3)
Store all facts in a dictionary.
4)
Style all responses.
5)
Attempt image recognition.


Now im going to gather images to teach the teachable machine!
Classes:
Battery – small and large
Plastic – bottles and containers
Paper/Cardboard – sheets and boxes
Glass – bottles and jars
Food waste – fruit and vegetables and leftovers

Getting Images:
I decided for each class ill get 8-15 images.
I also thought that diffrent angles and background and lighting will give me good benefits because the teachable machine
will then be able to tell me any picture and what it is. but i will avoid blury images because there not clear.

How im going to organize my images:
I will create a folder called "recycling_images" in here i will keep all the classes and in those classes will be the actual images of the class

Prepare for Teachable Machine:
I will also make sure that all images have the correct name and not be mixed up because if it is it could cause some chaos.
I will keep images the same size and avoid makeing one bgger and one smaller.
I will try get atleast 8 or more images.

In this image below you can see that i've got all my images and i trained my model and now im going to export my model in tensorflow keras.
i will name the image that shows what i've done 'How to export a model'.

After the project is exported you need to put the exported file in your project VSC folder.
I'll also include a images of how i do it, the file name is 'dragging-exported-file'.



















