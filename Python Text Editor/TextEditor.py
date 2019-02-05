#Simple Text Editor in Python
from tkinter import * 
import tkinter.messagebox
import tkinter.filedialog

#root is the main window
root = tkinter.Tk()
#window title
root.title("Text Editor 1.0")
#default size
root.geometry("600x400")

#Text area
text= Text(root, width=600, height=400)
text.pack()

#Exiting editor from file menu
def userExit():
    response = tkinter.messagebox.askokcancel(title="Exit Editor?", message="You may lose any unsaved changes.")
    if (response):
        root.destroy()
        
def newFile():
    #If user clicks on new file, empty the text area
    text.delete("0.0", END)
    
def openFile():
    #Get file
    file = tkinter.filedialog.askopenfile(parent = root, mode = 'r', title = "Select a file to open")
    if (file!=None):
        #If file is selected, read contents
        fileContent = file.read ()
        #Delete the existing text in the text area
        text.delete("0.0", END)
        #Insert file content to text area
        text.insert("0.0", fileContent)
        
    
def saveFile():
    #Ask user to create file
   fileName  = tkinter.filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
   
   if (fileName!=None): 
        #if user created a file, open it
        file = open(fileName, 'w')
        #get text area content
        fileContent =  text.get("0.0", END)
        #write content to file and close it
        file.write(fileContent)
        file.close()

def aboutMessage():
    tkinter.messagebox.showinfo("About","This text editor was created while exploring tkinter python module.")
    

#Main Menu 
mainMenu = Menu(root)
root.config(menu = mainMenu)

#File Menu
fileMenu= Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=fileMenu)

fileMenuLables = ["New", "Open", "Save", "Exit"]
fileMenuCommands = [newFile, openFile, saveFile, userExit]

for index in range(len(fileMenuLables)):
    fileMenu.add_command(label= fileMenuLables[index], command = fileMenuCommands[index])

#Edit Menu
editMenu= Menu(mainMenu)
mainMenu.add_cascade(label="Edit", menu=editMenu)

editMenuLables = ["Cut", "Copy", "Paste"]
editMenuAccelerator = ["Ctrl+X", "Ctrl+C", "Ctrl+V"]
editMenuCommands = [lambda: root.event_generate('<Control-x>'),
                    lambda: root.event_generate('<Control-c>'),
                    lambda: root.event_generate('<Control-v>')]

for index in range(len(editMenuLables)):
    editMenu.add_command(label= editMenuLables[index],  accelerator=editMenuAccelerator[index], command=editMenuCommands[index])


#About message
mainMenu.add_command(label="About", command= aboutMessage)

#event loop
root.mainloop()
