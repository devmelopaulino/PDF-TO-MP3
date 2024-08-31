from pypdf import PdfReader # PDF READER LIBRARY
import pyttsx3 # AUDIO LIBRARY

audio = True # TO GERATE AUDIO
language = 'pt-br' # VOICE LANGUAGE, CHANGE
inicialPage = 0  # CHANGE
finalPage = 0 # CHANGE
nameMp3 = "NAME_MP3" # CHANGE

#           r'C:\...\EXAMPLE_PDF_FILE.pdf'
pdf = open(r'', 'rb') # PDF FILE 'rb' TO OPEN IN BINARY MODE, CHANGE

readerpdf = PdfReader(pdf) # READING THE PDF FILE
number_of_pages = len(readerpdf.pages) # NUMBER OF PAGES IN THE PDF


pages = [] # VARIABLE TO STORE THE PDF PAGES
allpdf = ''

print("-------------------STARTING-------------------")

for idx, p in enumerate(readerpdf.pages, start= inicialPage ):  # PROCESS TO STORE THE PAGES IN THE VARIABLE pages (start = 3 INITIAL LIMIT)
    if idx > finalPage: # FINAL PAGE LIMIT
        break    
    pages.append(readerpdf.pages[idx - 1]) 
    print("STORING PAGE NUMBER: ", idx)

for i, p in enumerate(pages):
    allpdf = allpdf + p.extract_text()
    print("EXTRACTING TEXT FROM PAGE NUMBER: ", i + 1)

print("-------------------TEXT EXTRACTED-------------------")

allpdf = allpdf.split("\n")

print("-------------------PARAGRAPHS SEPARATED-------------------")

allpdf = " ".join(allpdf)

print("-------------------SPACES JOINED-------------------")

print("NUMBER OF CHARACTERS: ",len(allpdf))

if audio:

    print("-------------------STARTING AUDIO-------------------")
    voice = pyttsx3.init()
    voice.setProperty('rate', 225)
    voice.save_to_file(allpdf, nameMp3 + '.mp3')
    voice.runAndWait()
    print("-------------------AUDIO COMPLETED-------------------")

print("------------------- END -------------------")
