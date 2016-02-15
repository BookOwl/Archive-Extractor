#!python3
# Archive Extractor
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import *
from tkinter import *
import shutil

class ArchiveExtractorGUI(Frame):
    def __init__(self, parent=None,**options):
        Frame.__init__(self,parent,**options)
        self.archivefile = ''
        self.extractdir = ''
        self.pack(fill=BOTH)
        Label(self,text='Archive Extractor GUI').pack()
        Button(self,text='Pick Archive File',command=self.getfile).pack(
            side=TOP, fill=BOTH)
        self.__arclabel = Label(self,text="You picked: ", bg='white')
        self.__arclabel.pack(side=TOP, fill=BOTH)
        Button(self,text='Pick Folder to Store Extracted Files',command=self.getdir).pack(
            side=TOP, fill=BOTH)
        self.__dirlabel = Label(self, text="You picked: ", bg='white')
        self.__dirlabel.pack(side=TOP, fill=BOTH)
        Button(self,text='Extract Archive',command=self.extract).pack(
            side=TOP, fill=BOTH)
    def getfile(self):
        self.archivefile = askopenfilename(initialdir='C:\\',title='Pick Archive')
        self.__arclabel['text'] = 'You picked: ' + self.archivefile
    def getdir(self):
        self.extractdir = askdirectory(initialdir='C:\\',title='Pick Folder to Extract Files To')
        self.__dirlabel['text'] = 'You picked: ' + self.extractdir
    def extract(self):
        if self.archivefile == '' or self.extractdir == '':
            showerror('ERROR!','You did not select a archive or you did not select a folder to store extracted files.')
            return
        try:
            shutil.unpack_archive(self.archivefile,self.extractdir)
            showinfo('Success!','Archive {} unpacked succesfuly to {}'.format(self.archivefile, self.extractdir))
        except Exception as e:
            print(e)
            showerror('ERROR!', str(e))

if __name__ == '__main__':
    Tk().title('Archive Extractor GUI')
    ArchiveExtractorGUI().mainloop()   
