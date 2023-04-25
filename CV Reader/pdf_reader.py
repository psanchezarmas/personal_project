# importing required modules
import PyPDF2
from pathlib import Path
import os
from os import listdir
from os.path import isfile, join
import numpy as np
import ipdb 
import openai

openai.api_key = "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"
Files_Path = (Path.cwd())
Files_Path = str(Files_Path) + "\CV Reader\CVs"
Files_Path = Path(Files_Path)


#ipdb.set_trace()   
onlyfiles = [f for f in listdir(Files_Path) if isfile(join(Files_Path, f))]

len_onlyfiles = len(onlyfiles)

def obtain_cv(i):
    onlyfiles = [f for f in listdir(Files_Path) if isfile(join(Files_Path, f))]
    cv_path = Path(str(Files_Path) + "\\" +  onlyfiles[i])
    return cv_path

# Substitute this loop below with multiprocess

for x in range(0, len_onlyfiles):

# create a pdf file object
    pdfFileObj = open(obtain_cv(x), 'rb')

    # create a pdf reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    page_number = len(pdfReader.pages)
    # print number of pages in the pdf file
    # print("Page Number:", len(pdfReader.pages))

    # create a page object

    # we need to create a loop for all the pages that the cv has

    for i in range(0, page_number):
        pageObj = pdfReader.pages[i]
        # extract text from page
        text = pageObj.extract_text()
        if i == 0:
            final_text = text
        else:
            final_text += text

    textchatGPT = "Can you generate a professional profile from the following text? The professional profile is a description of the CV according to his/her professional experience, programming languages, education and skills " +  final_text

    # print(textchatGPT)

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    
    messages=[
            {"role": "system", "content": textchatGPT}
            ]
    )
    
    profile = (response['choices'][0]['message']['content'])        
    
    profile = profile.replace('"role": "assistant"', ' ')