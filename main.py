#import statments
import PyPDF2
import easygui
from gtts import gTTS

#get the pdf file and create PyPDF2 object
path = easygui.fileopenbox()
pdffileobj = open(path,"rb")
reader = PyPDF2.PdfReader(pdffileobj)

#get the number of pages
num_page = len(reader.pages)

#convert pdf to text. doesn't work well with diagrams/unorgenised text. file is mostly accurate but still needs to be prof read.
with open(r"text.txt", 'w') as file1:
    for page in range(num_page):
        page_obj = reader.pages[page]
        file1.writelines([f"Page {page+1}", "\n"])
        text = page_obj.extract_text()
        file1.writelines([text, "\n"])

#convert the txt file to mp3
#this tts library sound a bit robotic. For better reasults we need to use an api but its not free, so this is what we get
with open(r"text.txt", "r") as file2:
    text = file2.read()
    audio = gTTS(text=text,lang ="en", slow=False)
    audio.save("example.mp3")

    

    
    







