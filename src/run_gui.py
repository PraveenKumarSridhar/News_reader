from tkinter import *
from PIL import ImageTk, Image
from utils.get_news import *

# key down function
def click():
    #  to collect the text from the textbox
    entered_text = text_entry.get()
    output.delete(0.0,END)
    try:
        definition = my_comp_dict[entered_text]
    except:
        definition = "Sorry!!! I dont know."
    output.insert(END,definition)

def show_news():
    #  to collect the text from the textbox
    entered_text = text_entry.get()
    headline_box.delete(0.0,END)
    link_box.delete(0.0,END)
    try:
        headlines, links = get_news(entered_text)
        out_headlines  = '\n'.join(headlines).strip('\n')
        out_links  = '\n'.join(links).strip('\n')
    except:
        definition = "Sorry!!! I dont know."
    headline_box.insert(END,out_headlines)
    link_box.insert(END,out_links)


# main
window = Tk()
window.title("Get News")
window.configure(background="black")

# image
img = ImageTk.PhotoImage(Image.open("./assests/news_reading-black.jpg").resize((200,200)))
Label (window,image = img,bg= "black").grid(row=0,column=0,sticky = W)

# text
Label (window, text= "Enter News you are interested in:", bg="black",\
         fg= "white",font = "none 11 bold").grid(row = 1, column = 0, sticky = W)

# input
text_entry = Entry(window, width = 40, bg = "white")
text_entry.grid(row = 2 , column = 0, sticky = W)

# Button
Button(window,text = "SUBMIT", width = 6, command= show_news).\
    grid(row=2, column = 1, sticky= W)

# Label 
Label(window, text = "\nNews headlines: " ,bg="black",\
         fg= "white",font = "none 12 bold").grid(row = 4, column = 0, sticky = W)

# output 
headline_box = Text(window,width = 75,height = 6, wrap = WORD, background="white")
headline_box.grid(row= 5, column = 0, columnspan=2,sticky = W)

# Label 
Label(window, text = "\nNews Links: " ,bg="black",\
         fg= "white",font = "none 12 bold").grid(row = 6, column = 0, sticky = W)

# output 
link_box = Text(window,width = 75,height = 6, wrap = WORD, background="white")
link_box.grid(row= 7, column = 0, columnspan=2,sticky = W)

# dictionary 
# my_comp_dict = {
#     "algorithm" : "a logic",
#     "model" : "a math framework"
# }

window.mainloop()