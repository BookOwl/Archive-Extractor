#!python3
# archiveextractor.pyw
# Created by Matthew (BookOwl)
# Released under the MIT license

from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import *
from tkinter import *
import shutil, _thread, queue, os.path, webbrowser

about = ("About Archive Extractor GUI 2.0",
"""
Archive Extractor GUI 2.0
A simple graphical archive extractor written in Python.
To use, just run archiveextractor.pyw

This tool support extracting
* gztar: gzip’ed tar-file
* bztar: bzip2’ed tar-file (if the bz2 module is available.)
* xztar: xz’ed tar-file (if the lzma module is available.)
* tar: uncompressed tar file
* zip: ZIP file


Changelog:
2.0: Extractions are now performed on a separate thread, so multiple extractions can be run at once. The file and directory pickers remember the last directory picked. Added an about button
1.0: First release.

License
Released under the MIT license.

The homepage for this project is https://github.com/BookOwl/Archive-Extractor
"""
)

def showabout():
    webbrowser.open("https://github.com/BookOwl/Archive-Extractor")
    showinfo(*about)

class ArchiveExtractorGUI(Frame):
    def __init__(self, parent=None,**options):
        Frame.__init__(self,parent,**options)
        self.archivefile = ''
        self.extractdir = ''
        self.lastfiledir = os.path.expanduser("~") # Get users home directory
        self.lasttodir = os.path.expanduser("~")
        self.queue = queue.Queue()
        Label(self, text='Archive Extractor GUI').pack()
        Button(self, text='Pick Archive File', command=self.getfile).pack(
            side=TOP, fill=BOTH)
        self.__arclabel = Label(self, text="You picked: ", bg='white')
        self.__arclabel.pack(side=TOP, fill=BOTH)
        Button(self, text='Pick Folder to Store Extracted Files', command=self.getdir).pack(
            side=TOP, fill=BOTH)
        self.__dirlabel = Label(self, text="You picked: ", bg='white')
        self.__dirlabel.pack(side=TOP, fill=BOTH)
        Button(self, text='Extract Archive', command=self.extract).pack(
            side=TOP, fill=BOTH)
        Button(self, text="About", command=showabout).pack(side=RIGHT)
        self.checkcallbacks()

    def getfile(self):
        self.archivefile = askopenfilename(initialdir=self.lastfiledir, title='Pick Archive File')
        self.lastfiledir = os.path.dirname(self.archivefile)
        self.__arclabel['text'] = 'You picked: ' + self.archivefile

    def getdir(self):
        self.extractdir = askdirectory(initialdir=self.lasttodir, title='Pick Folder to Extract Files To')
        self.lasttodir = os.path.dirname(self.extractdir)
        self.__dirlabel['text'] = 'You picked: ' + self.extractdir

    def extract(self):
        if self.archivefile == '' or self.extractdir == '':
            showerror('ERROR!','You did not select a archive or you did not select a folder to store extracted files.')
            return
        _thread.start_new_thread(self.extract_thread, (self.archivefile, self.extractdir))

    def extract_thread(self, file, dir):
        def callbackgood():
            showinfo('Success!','Archive {} unpacked succesfuly to {}'.format(file, dir))
        try:
            shutil.unpack_archive(self.archivefile,self.extractdir)
            self.queue.put(callbackgood)
        except Exception as e:
            error = e
            def callbackbad():
                print(error)
                showerror('ERROR!', str(error))
            self.queue.put(callbackbad)

    def checkcallbacks(self):
        try:
            while True:
                self.queue.get(False)()
        except queue.Empty:
            pass
        self.after(100, self.checkcallbacks)

if __name__ == '__main__':
    Tk().title('Archive Extractor GUI')
    gui = ArchiveExtractorGUI()
    gui.pack(fill=BOTH)
    gui.mainloop()
