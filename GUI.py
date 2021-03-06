import Tkinter as tk
import tkFileDialog
import time
import csv
import subprocess

from Tkinter import *
import cPickle as pickle

  
class Window:       
	def __init__(self, master):     
	    self.filename=""
	    csvfile=Label(root, text="File").grid(row=1, column=0)
	    bar=Entry(master).grid(row=1, column=1) 

	    #Buttons  
	    y=7
	    self.cbutton= Button(root, text="OK", command=self.process_csv)
	    y+=1
	    self.cbutton.grid(row=10, column=3, sticky = W + E)
	    self.bbutton= Button(root, text="Browse", command=self.browsecsv)
	    self.bbutton.grid(row=1, column=3)

	def browsecsv(self):
	    from tkFileDialog import askopenfilename

	    # Tk().withdraw() 
	    self.filename = askopenfilename()
	    print self.filename

	def process_csv(self):
		print "hello world"
		#print self.filename
		cmd = "python audio_graph_using_functions.py "+ self.filename
		subprocess.call(cmd, shell = True)
                cmd = "python code.py "+self.filename
                subprocess.call(cmd, shell = True)
                audiolen = pickle.load(open('audiolength', 'rb'))
                cmd = "python convertlisttosec.py "+self.filename+".trans "+str(audiolen)
                subprocess.call(cmd, shell = True)
                cmd = "python timetoword.py "+self.filename+".transsec timelist > "+"words_from_audio.txt"
                subprocess.call(cmd, shell = True)
                cmd = "rm input_file.txt"
                subprocess.call(cmd, shell = True)
                
                cmd = "python transtocsv.py "+self.filename+".transsec > "+"input_file.txt"
                subprocess.call(cmd, shell = True)
                cmd = "python generate_summary.py"
                subprocess.call(cmd, shell = True)
                sys.exit(1)
	    
root = Tk()
window=Window(root)
root.mainloop()  
