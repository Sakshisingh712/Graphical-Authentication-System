import speech_recognition as sr
from PIL import Image, ImageDraw, ImageFont
import random
import string
# set up the microphone
r = sr.Recognizer()
mic = sr.Microphone()
from PIL import Image, ImageDraw, ImageFont
import random

# Set up image size and background color
img_width = 400
img_height = 200
background_color = (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))

# Create a new image with the given size and background color
img = Image.new('RGB', (img_width, img_height), background_color)

# Get a drawing context for the image
draw = ImageDraw.Draw(img)

# Set up the font and text for the image
font_size = 48
font_color = (0, 0, 0)
font = ImageFont.truetype("arial.ttf", font_size)

def generate_random_text(length=10):
    # Define the characters to choose from
    letters = string.ascii_letters
    digits = string.digits
    #special_chars = string.punctuation

    # Generate the random text
    random_text = ''.join(random.choice(letters + digits ) for i in range(length))

    return random_text

# Example usage
text = generate_random_text(10)


# Get the size of the text and calculate its position in the center of the image
text_width, text_height = draw.textsize(text, font)
text_x = (img_width - text_width) // 2
text_y = (img_height - text_height) // 2

# Draw the text on the image
draw.text((text_x, text_y), text, font=font, fill=font_color)

# Add a watermark to the text
watermark_text = "This is sample text."
watermark_font_size = 42
watermark_font_color = (128,128,128)
watermark_font = ImageFont.truetype("arial.ttf", watermark_font_size)
watermark_width, watermark_height = draw.textsize(watermark_text, watermark_font)
watermark_x = ((text_x + text_width)/15)
watermark_y = ((text_y + text_height) - watermark_height)
draw.text((watermark_x, watermark_y), watermark_text, font=watermark_font, fill=watermark_font_color, rotate =45)
img.save("Obscured_image.png")
# Display the image
img.show()


original_text=text
# use pytesseract to extract the original text from the image
try:
    img = Image.open('random_text_image.png')
    print("Original text: ", original_text)
except:
    print("Unable to read the image.")

# overwrite the text on the image with texts
draw.text((50, 50), "This is for test." , font=font, fill=(0, 0, 0))
img.save('obscured_text_image.png')

# prompt the user to read the original text
with mic as source:
    print("Please read the following text aloud: ")
    print(original_text)
    audio = r.listen(source)

# use speech recognition to compare user input to original text
try:
    spoken_text = r.recognize_google(audio)
    print("Spoken text: ", spoken_text)
    
    if original_text == spoken_text.lower():
        print("You correctly read the text from the image!")
    else:
        print("Sorry, you did not correctly read the text from the image.")
except:
    print("Unable to recognize speech.")
