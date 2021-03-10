#!/usr/bin/env python
# coding: utf-8

# # Description - This program converts PDF File into audio file

# # Import the libraries

# In[12]:


import pyttsx3
import PyPDF2
import pdfplumber


# # Get the File Name & location of the PDF File

# In[13]:


file = 'D:/Tor and the Dark Art of Anonymity (deep web, kali linux, hacking, bitcoins) Defeat NSA Spying/Tor and the Dark Art of Anonymity (deep web, kali linux, hacking, bitcoins) Defeat NSA Spying.pdf' 


# # Create a PDF File Object

# In[14]:


pdfFileObj = open(file,'rb') 


# # Create a PDF File Reader Object

# In[15]:


pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


# # Get the number of Pages

# In[16]:


pages = pdfReader.numPages


# # Create a PDFPlumber Object and loop through the number of pages in PDF File

# In[ ]:


with pdfplumber.open(file) as pdf:
    #loop through the number of pages
    for i in range(0,pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()
        


# In[ ]:


# Setting the voice of audio to male/female
voices = speaker.getProperty('voices')
print(voices)
#changing index, changes voices, 0 for male
speaker.setProperty('voice', voices[0].id)
#changing index, changes voices, 1 for female
speaker.setProperty('voice', voices[1].id)


# In[ ]:


# Volume
volume = speaker.getProperty('volume')
print(volume)
speaker.setProperty('volume',1.0)


# In[ ]:


# Saving Voice to Audio file:
speaker.save_to_file(text, 'audio.mp3')
speaker.runAndWait()

