from PIL import Image

print(""" 
        WARNING: This will replace the old image with the new one. 
        You'd better keep a copy.
 """)

path = input("Enter the path to the image: ")
im = Image.open(path)
width, height = im.size
ratio = height/width
choice = int(input("1- Maintain aspect ratio\n2- Don't maintain aspect ratio\n"))
if choice == 1:
    new_width = int(input("Enter the new width: "))
    new_height = int(ratio*new_width)
    resized_im = im.resize((new_width, new_height))
else: 
    new_width, new_height = tuple(map(int, input("Enter the new width and height separated by a space: ").split()))
    resized_im = im.resize((new_width, new_height))
resized_im.save(path)
resized_im.close()



