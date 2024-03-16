from django.shortcuts import render
from myfile.forms import UploadsForms
from myfile.models import *
from PyPDF2 import PdfReader
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from googletrans import Translator
import yake

# This function is created for uploading  pdf
def upload(request):
    if request.method == "POST":
        form = UploadsForms(request.POST, request.FILES)
        pdf_file=request.FILES['file']
        if form.is_valid():
           pdf_reader=PdfReader(pdf_file)
           no_page=len(pdf_reader.pages)
           if no_page>=15:
               pdf_file=request.FILES['file']
               #Extracting  text from the pdf with Extract_text function
               extractedtext=Extract_text(pdf_file)
               #Summarizing text from extracted text
               extracted_summary=get_summary(extractedtext) 
               #translating summary into English  
               translatedsummary1=translate_summary_English(extracted_summary)
               #Extracting key words  
               englishkey=English_key(translatedsummary1)
               #translating summary into
               translatedsummary2=translate_summary_Marathi(extracted_summary)
               #Extracting key words
               marathikey=marathi_key(translatedsummary2)
            #    extractedkeyword=extract_keyword(extractedtext)                   
            #    form.save()  
               return render(request,'display.html',{'value1':translatedsummary1,'value2':englishkey,'value3':translatedsummary2,'value4':marathikey})
           else:
               msg='uploaded file should not be  less than 15 pages'
               return render(request,'upload.html',{'msg':msg})
               
    else:
        form = UploadsForms()
    return render(request, "upload.html", {"form": form})


#  creating user define function for Extracting Text from PDF
def Extract_text(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# creating function for summarize the extracted text
def get_summary(extractedtext):    
    parser = PlaintextParser.from_string(extractedtext, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count=5)  # Adjust sentences_count as needed
    summary = " ".join(str(sentence) for sentence in summary)
    return summary

# creating function for tranlating  text in english
def translate_summary_English(extracted_summery):
    translator = Translator()
    translated_text = translator.translate(extracted_summery, dest='en')
    x=translated_text.text
    return x

# generating keywords
def English_key(translate_summary_English):
    test1= yake.KeywordExtractor()
    t=test1.extract_keywords(translate_summary_English)
    word=[word[0] for word in t]
    return word

# creating function for tranlating  text in marathi
def translate_summary_Marathi(extracted_summery):
    translator = Translator()
    translated_text = translator.translate(extracted_summery, dest='mr')
    x=translated_text.text
    return x    
# generating keywords
def marathi_key(translate_summary_Marathi):
    test1= yake.KeywordExtractor()
    t=test1.extract_keywords(translate_summary_Marathi)
    word=[word[0] for word in t]
    return word