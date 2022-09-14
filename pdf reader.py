import pyttsx3
import PyPDF2
from tkinter import filedialog as fd
from tkinter.filedialog import Tk

root = Tk()
root.withdraw()
root.attributes('-topmost', True)

file_path = fd.askopenfilename(title = 'Select a file', filetypes = [("pdf files", "*.pdf")])
save_path = fd.askdirectory(title = "Save file")
start = int(input("Start reading from page: "))
end = int(input("Stop reading at page: "))
m_f = int(input("1- Male voice\n2- female voice\n3- Toggle at each page\n "))
v = m_f - 1
book = open(file_path, "rb")
pdfreader = PyPDF2.PdfReader(book)
pages = pdfreader.numPages
speaker = pyttsx3.init()
speaker.setProperty("rate", 140)
voices = speaker.getProperty('voices')
for i in range(start-1, end+1):
    if m_f == 3:
        if v == 2:
            v = 1
        if v == 0:
            v = 1
        elif v == 1:
            v = 0
    page = pdfreader.getPage(i)
    text = page.extractText()
    # speaker.say(text)
    speaker.runAndWait()
    speaker.save_to_file(text, f'{save_path}\\page {i+1}.mp3')
    speaker.setProperty('voice', voices[v].id)
