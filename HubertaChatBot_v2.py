# -*- coding: utf-8 -*-
"""
Created on Sat May  7 09:59:10 2022

@author: Andreas
"""
import sys
import subprocess

# install required packages with pip-install
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'Pillow'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'transformers'])

# import required packages
import tkinter
from PIL import ImageTk
from transformers import pipeline, Conversation

# class containing the objects in the mainframe and functions for updating the frame
class Huberta:
    
    def __init__(self, mainframe, modelclass):
        mainframe.title('Ask Huberta')
        
        # adding blank space into the frame
        self.BlankLine = tkinter.Label(text="")
        self.BlankLine.pack()
        
        # adding the header 
        self.HeadingLabel = tkinter.Label(text="Hi, I'm Huberta.",
                            font = "Helvetica 16 bold italic")
        self.HeadingLabel.pack()
        
        # subheading
        self.SubHeadingLabel = tkinter.Label(text = "Please ask me any question.",
                                font = "Helvetica 13 italic")
        self.SubHeadingLabel.pack()
        
        # image of the bot
        self.HubertaImage = ImageTk.PhotoImage(file='Huberta.png')
        
        # construct a label widget for image
        self.ImageLabel = tkinter.Label(image=self.HubertaImage)
        self.ImageLabel.image = self.HubertaImage
        self.ImageLabel.pack(expand=True)
        
        # variables containing the text from the question and answer
        self.text = "Question:"
        self.answer = "Answer:"
        
        # label widgets presenting the last question and answer
        self.QuestionAsked = tkinter.Label(text = self.text, 
                                           font= "Helvetica 12 bold italic")
        self.HubertaAnswerSection = tkinter.Label(text = self.answer, 
                                                  font= "Helvetica 12 bold italic")
        self.QuestionAsked.pack()
        self.HubertaAnswerSection.pack()
       
        # label widget prompting user to type in their question
        self.QuestionSection = tkinter.Label(text='Type in Your Question:',
                                         font = "Helvetica 13")
        self.QuestionSection.pack(expand=False)
        
        # entry widget for users to enter their question
        self.comment_question = tkinter.Entry(width=50, font=('Arial', 10))
        self.comment_question.pack(expand=False)
        
        # adding button and command will use the functions defined below
        self.button = tkinter.Button(text='Submit', 
                                fg='blue', 
                                command=lambda: [display_question(), 
                                                 update_conversation(modelclass),
                                                 display_answer(modelclass), clear()])
        self.button.pack(expand=True)
        
        # adding blank space into the frame
        self.FinalBlankLine = tkinter.Label(text="")
        self.FinalBlankLine.pack()  
        
        # clears the question section after submiting
        def clear():
            self.comment_question.delete(0,'end')
        # updates the question section with latest prompt
        def display_question():
            self.text = "Q: " + self.comment_question.get()
            self.QuestionAsked.configure(text=self.text)
        # update answer section with the bot's latest answer    
        def display_answer(modelclass):
            self.answer = "A: " + modelclass.conv.generated_responses[-1]
            self.HubertaAnswerSection.configure(text=self.answer)
        # take the user's question input and update conversation to get bot's answer    
        def update_conversation(modelclass):
            user_input = self.comment_question.get()
            modelclass.conv.add_user_input(user_input)
            modelclass.conversational_pipeline(modelclass.conv)
        
        
# class which defines the conversation pipeline used and initializes the conversation      
class ConversationModel:
    
    def __init__(self):
        
        #define the type of pipeline
        self.conversational_pipeline = pipeline('conversational')
        #text to start the conversation
        self.conv_start = 'Hi.'
        # instantiate conversation with starter
        self.conv = Conversation(self.conv_start)
        # update conversation through the pipeline to get the bots response
        self.conversational_pipeline(self.conv)
        
# top-level widget which represents the main 
# window of the application       
def main():
    root = tkinter.Tk()
    root.geometry('600x600')
    model = ConversationModel()
    huberta = Huberta(root, model)
    # call the mainloop of Tk
    # keeps window open
    root.mainloop()
    
if __name__ == '__main__': 
    main()