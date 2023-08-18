#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


# In[3]:


root = Tk()
root.geometry('1080x400')


# In[4]:


root.resizable(0,0)
root.config(bg = 'ghost white')


# In[5]:


root.title("Project Code Alpha--Language Translator")


# In[6]:


Label(root, text = "LANGUAGE TRANSLATOR", font = "arial 15 bold", bg='white smoke').pack()


# In[7]:


Label(root,text ="Project Code Alpha", font = 'arial 18 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')


# In[8]:


Label(root,text ="Enter Text", font = 'arial 13 bold', bg ='white smoke').place(x=200,y=60)


# In[9]:


Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60)
Input_text.place(x=30,y = 100)


# In[10]:


Label(root,text ="Output", font = 'arial 13 bold', bg ='white smoke').place(x=780,y=60)


# In[11]:


Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
Output_text.place(x = 600 , y = 100)


# In[13]:


language = list(LANGUAGES.values())


# In[15]:


src_lang = ttk.Combobox(root, values= language, width =22)


# In[16]:


src_lang.place(x=20,y=60)
src_lang.set('choose input language')


# In[18]:


dest_lang = ttk.Combobox(root, values= language, width =22)


# In[22]:


dest_lang.place(x=890,y=60)
dest_lang.set('choose output language')


# In[23]:


def Translate():
    translator = Translator()


# In[25]:


translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())


# In[27]:


Output_text.delete(1.0, END)
Output_text.insert(END, translated.text)


# In[29]:


trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = 'royal blue1', activebackground = 'sky blue')trans_btn.place(x = 490, y= 180 )root.mainloop()



# In[ ]:
