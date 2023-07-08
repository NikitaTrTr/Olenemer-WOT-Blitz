from PIL import Image, ImageDraw, ImageFont
import os

def save_icon_with_id(tank_id, filename):
    icon = Image.new("RGBA", (64, 32), (0, 0, 0, 0))
    content = ImageDraw.Draw(icon)
    content.text(text_position, str(tank_id), font=font, fill=(255, 255, 255, 255))
    save_folder = "icons_with_ids/"
    icon.save(save_folder+filename, 'webp', lossless=True)

font = ImageFont.truetype("arial.ttf", 22)
text_position = (1, 4)
folder_path = 'original_icons'
file_names = os.listdir(folder_path)
for icon_name in file_names:
    underscore = icon_name.index('_')
    tank_id = icon_name[0:underscore]
    filename = icon_name[underscore+1:]
    save_icon_with_id(tank_id, filename)