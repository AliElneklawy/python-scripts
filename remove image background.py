from rembg import remove
from PIL.Image import open
from ntpath import basename
from tkinter import filedialog as fd
from tkinter.filedialog import  Tk

root = Tk()
root.withdraw()
root.attributes('-topmost', True)

input_path = fd.askopenfilename()
output_path = fd.askdirectory()
file_name = basename(input_path)
input_image = open(input_path)
output = remove(input_image)
output.save(f"{output_path}\\{file_name}.png")