# -*- coding: utf-8 -*-
"""
Created on Sat May  7 09:59:10 2022

@author: Andreas
"""
import tkinter
from PIL import ImageTk
from transformers import pipeline, Conversation

# top-level widget which represents the main 
# window of the application
class Huberta:
    
    def __init__(self, mainframe, modelclass):
        mainframe.title('Ask Huberta')
        
        # adding blank space into the frame
        self.BlankLine = tkinter.Label(text="")
        self.BlankLine.pack()
        
        # adding label with different font and formatting
        self.HeadingLabel = tkinter.Label(text="Hi, I'm Huberta.",
                            font = "Helvetica 16 bold italic")
        self.HeadingLabel.pack()
        
        self.SubHeadingLabel = tkinter.Label(text = "Please ask me any question.",
                                font = "Helvetica 13 italic")
        self.SubHeadingLabel.pack()
        
        # starting image which then will be updated
        self.HubertaImage = ImageTk.PhotoImage(file='Huberta.png')
        
        # construct a label widget for image
        self.ImageLabel = tkinter.Label(image=self.HubertaImage)
        self.ImageLabel.image = self.HubertaImage
        
        self.ImageLabel.pack(expand=True)
        
        self.text = "Question:"
        self.answer = "Answer:"
        
        self.QuestionAsked = tkinter.Label(text = self.text, 
                                           font= "Helvetica 12 bold italic")
        self.QuestionAsked.pack()
        
        self.HubertaAnswerSection = tkinter.Label(text = self.answer, 
                                                  font= "Helvetica 12 bold italic")
        self.HubertaAnswerSection.pack()
       
        self.QuestionSection = tkinter.Label(text='Type in Your Question:',
                                         font = "Helvetica 13")
        self.QuestionSection.pack(expand=False)
        
        self.comment_question = tkinter.Entry(width=50, font=('Arial', 10))
        self.comment_question.pack(expand=False)
        
        # adding button, and command will use ask_huberta and clear function
        self.button = tkinter.Button(text='Submit', 
                                fg='blue', 
                                command=lambda: [display_question(), 
                                                 update_conversation(modelclass),
                                                 display_answer(modelclass), clear()])
        # pack a widget in the parent widget
        self.button.pack(expand=True)
        
        # adding blank space into the frame
        self.FinalBlankLine = tkinter.Label(text="")
        self.FinalBlankLine.pack()  
          
        def clear():
            self.comment_question.delete(0,'end')
            
        def display_question():
            self.text = "Q: " + self.comment_question.get()
            self.QuestionAsked.configure(text=self.text)
            
        def display_answer(modelclass):
            self.answer = "A: " + modelclass.conv.generated_responses[-1]
            self.HubertaAnswerSection.configure(text=self.answer)
            
        def update_conversation(modelclass):
            user_input = self.comment_question.get()
            modelclass.conv.add_user_input(user_input)
            modelclass.conversational_pipeline(modelclass.conv)
        
        
        
class ConversationModel:
    
    def __init__(self):
        
        self.conversational_pipeline = pipeline('conversational')

        self.conv_start = 'Hi.'

        self.conv = Conversation(self.conv_start)

        self.conversational_pipeline(self.conv)
        
        
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