from tkinter import *
from tkinter import ttk,filedialog,messagebox
from PIL import ImageTk, Image
import os,shutil

class Sorting_Folder:
       def __init__(self, root):
              self.root = root
              self.root.config(bg = "white")
              self.root.title("Jsort, File Sorting And Clearer | Developed By Sohail Ahmad")
              self.root.geometry("990x630+200+40")

              title = Label(self.root, text = "Jsort, File Sorting And Clearer Application", font = ("indie flower", 30), bg="#ed4f1a", fg="white").place(x=0, y=0, relwidth = 1 , height=80)
       
              #----------------------------------------------
              #for selecting folder directory

              self.var_folder_name = StringVar()

              label_select_folder = Label(self.root, text = "Select Folder", bg = "white", font = ("sans", 10, "bold") ).place(x = 50, y= 128)
              text_folder_name = Entry(self.root, textvariable = self.var_folder_name, font = ("sans", 10, "bold"), state = "readonly").place(x = 160, y= 125, height= 25 ,width = 350)
              button_browse = Button(self.root,bd = 2, command = self.browse_folder, text = "BROWSE", font = ("sans", 10, "bold") ,bg = "black", fg = "white", activebackground = "black", activeforeground = "white", cursor = "hand2").place(x = 500, y = 123)
              hr = Label(self.root, bg ="lightgray" ).place(x= 30,y = 180, height = 1, relwidth =0.90) 

        
              #-----------------------------------------------
        
              """
              TYPES
               ["HTML",".html5", ".html", ".htm", ".xhtml"],

               ["IMAGES",".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
               ["VIDEOS",".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
               ["DOCUMENTS",".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
               ["ARCHIVES",".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
               ["AUDIO",".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
               ["PLAINTEXT",".txt", ".in", ".out"],
               ["PDF",".pdf"],
               ["PYTHON",".py"],
               ["XML"".xml"],
               ["EXE",".exe"],
               ["SHELL",".sh"]
        
              """

              #-----------------------------------
              self.html_extensions = ["HTML Types",".html5", ".html", ".htm", ".xhtml"]
              self.image_extensions = ["Image Types", ".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",".heif", ".psd"]
              self.audio_extensions = ["Audio Types", ".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"]
              self.video_extensions = ["Video Types", ".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",".qt", ".mpg", ".mpeg", ".3gp"]
              self.document_extensions = ["Document Types" ,".txt",".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",".pptx"]
              self.pdf_extensions = ["PDF Typess", ".pdf"]
              self.archive_extensions = ["Archive Types", ".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",".dmg", ".rar", ".xar", ".zip",".zipx"]

              self.folders ={
                            'images' : self.image_extensions ,
                            'audios' : self.audio_extensions ,
                            'videos' : self.video_extensions , 
                            'documents' : self.document_extensions,
                            'archive' : self.archive_extensions 
                     } 

              #image extensions type
              label_supported_extension = Label(self.root, text = "Various Supported Types", bg = "white", font = ("sans", 10, "bold") ).place(x = 50, y= 200)
              self.image_box = ttk.Combobox(self.root, values = self.image_extensions, state = "readonly", justify = CENTER ,font= ("sans", 10, "bold"))
              self.image_box.place(x = 60, y= 250, width = 150, height= 25)
              self.image_box.current(0)

              #audio extensions type
              self.audio_box = ttk.Combobox(self.root, values = self.audio_extensions, state = "readonly", justify = CENTER ,font= ("sans", 10, "bold"))
              self.audio_box.place(x = 60, y= 300, width = 150, height= 25)
              self.audio_box.current(0)

              #video extensions type
              self.video_box = ttk.Combobox(self.root, values = self.video_extensions, state = "readonly", justify = CENTER ,font= ("sans", 10, "bold"))
              self.video_box.place(x = 60, y= 350, width = 150, height= 25)
              self.video_box.current(0)

              #document extensions type
              self.document_box = ttk.Combobox(self.root, values = self.document_extensions, state = "readonly", justify = CENTER ,font= ("sans", 10, "bold"))
              self.document_box.place(x = 60, y= 400, width = 150, height= 25)
              self.document_box.current(0)

              #archive extensions type
              self.archive_box = ttk.Combobox(self.root, values = self.archive_extensions, state = "readonly", justify = CENTER ,font= ("sans", 10, "bold"))
              self.archive_box.place(x = 60, y= 450, width = 150, height= 25)
              self.archive_box.current(0)

              #-----------------------------------------
        
              img_icn = Image.open("Assets/photo2.png")
              img_resize = img_icn.resize((80,80), Image.ANTIALIAS)
              self.image_icon = ImageTk.PhotoImage(img_resize)
       
              aud_icn = Image.open("Assets/audio.png")
              aud_resize = aud_icn.resize((80,80), Image.ANTIALIAS)
              self.audio_icon = ImageTk.PhotoImage(aud_resize)

              vid_icn = Image.open("Assets/video.png")
              vid_resize = vid_icn.resize((80,80), Image.ANTIALIAS)
              self.video_icon = ImageTk.PhotoImage(vid_resize) 
       
              doc_icn = Image.open("Assets/document.png")
              doc_resize = doc_icn.resize((80,80), Image.ANTIALIAS)     
              self.document_icon = ImageTk.PhotoImage(doc_resize)
       
              arch_icn = Image.open("Assets/archive.png")
              arch_resize = arch_icn.resize((80,80), Image.ANTIALIAS)     
              self.archive_icon = ImageTk.PhotoImage(arch_resize)

              oth_icn = Image.open("Assets/others.png")
              oth_resize = oth_icn.resize((80,80), Image.ANTIALIAS)     
              self.other_icon = ImageTk.PhotoImage(oth_resize)

              #----------------------------------------

              self.Frame1 = Frame(self.root, bd = 0, relief = RIDGE)
              self.Frame1.place(x = 240, y = 200, width = 700, height = 350)#width = 797
              self.label_total_files = Label(self.Frame1, text = "Total Files : 0", font = ("sans", 10, "bold") )
              self.label_total_files.place(x = 10, y =5)
       
              self.label_total_image = Label(self.Frame1, bg = "white", text = "Total Images \n 0", image = self.image_icon, compound = TOP, font = ("sans", 10, "bold") )
              self.label_total_image.place(x = 40, y = 40, height = 140, width = 135)

              self.label_total_audio = Label(self.Frame1, bg = "white", text = "Total Audios \n 0", image = self.audio_icon, compound = TOP, font = ("sans", 10, "bold") )
              self.label_total_audio.place(x = 200, y = 40, height = 140, width = 135)

              self.label_total_video = Label(self.Frame1, bg = "white", text = "Total Videos \n 0", image = self.video_icon, compound = TOP, font = ("sans", 10, "bold") )
              self.label_total_video.place(x = 360, y = 40, height = 140, width = 135)
       
              self.label_total_document = Label(self.Frame1, bg = "white", text = "Total Documents \n 0", image = self.document_icon, compound = TOP, font = ("sans", 10, "bold") )
              self.label_total_document.place(x = 520, y = 40, height = 140, width = 135)

              self.label_total_archive = Label(self.Frame1, bg = "white", text = "Total Archives \n 0", image = self.archive_icon, compound = TOP, font = ("sans", 10, "bold") )
              self.label_total_archive.place(x =100 , y = 200, height = 140, width = 135)

              self.label_total_other = Label(self.Frame1, bg = "white", text = "Others \n 0", image = self.other_icon, compound = TOP,font = ("sans", 10, "bold") )
              self.label_total_other.place(x = 270, y = 200, height = 140, width = 135)       
       

              #------------------------------------------
       
              self.label_status = Label(self.root, text = "Status : ", bg = "white", font = ("sans", 10, "bold") )
              self.label_status.place(x = 47, y= 530)
              self.label_total = Label(self.root, text = "Total : 0", bg = "white", font = ("sans", 10, "bold") )
              self.label_total.place(x = 50, y= 580)
              self.label_moved = Label(self.root, text = "Moved : 0", bg = "white", font = ("sans", 10, "bold") )
              self.label_moved.place(x = 150, y= 580)
              self.label_left = Label(self.root, text = "Left : 0", bg = "white", font = ("sans", 10, "bold") )
              self.label_left.place(x = 250, y= 580)

              self.button_clear = Button(self.Frame1, command = self.clear_functn, bd = 0, text = "CLEAR", font = ("sans", 10, "bold") ,bg = "#141169", fg = "white", activebackground = "#141169", activeforeground = "white", cursor = "hand2")
              self.button_clear.place(x = 450, y = 220, height = 40, width = 200)

              self.button_start = Button(self.Frame1,  command = self.start_functn, bd = 0, text = "START" ,font = ("sans", 10, "bold") ,bg = "#11691a", fg = "white", activebackground = "#11691a", activeforeground = "white", cursor = "hand2")
              self.button_start.place(x = 450, y = 280, height = 40, width = 200)

       def Total_count(self):
              images = 0
              audios = 0
              videos = 0
              documents = 0
              arhcives = 0
              others = 0
              self.count = 0
              for i in self.all_files:
                     if os.path.isfile( os.path.join( self.folder_directory , i )) == True:
                            self.count += 1
                            ext = "." + i.split(".")[-1]   
                            for folder_name in self.folders.items():
                                   #print(folder_name)
                                   if ext in folder_name[1] and folder_name[0] == 'images':
                                          images +=1
                                   if ext in folder_name[1] and folder_name[0] == 'audios':
                                          audios +=1
                                   if ext in folder_name[1] and folder_name[0] == 'videos':
                                          videos +=1
                                   if ext in folder_name[1] and folder_name[0] == 'documents':
                                          documents +=1
                                   if ext in folder_name[1] and folder_name[0] == 'archive':
                                          arhcives +=1
                     
                     others = self.count - images - audios - videos - documents - arhcives

                     self.label_total_image.config(text = "Total Images \n" + str(images))
                     self.label_total_audio.config(text = "Total Audio \n" + str(audios))
                     self.label_total_video.config(text = "Total Videos \n" + str(videos))
                     self.label_total_document.config(text = "Total Documents \n" + str(documents))
                     self.label_total_archive.config(text = "Total Archives \n" + str(arhcives))

                     self.label_total_other.config(text = "Others \n" + str(others))

                     self.label_total_files.config(text = "Total Files :" + str(self.count))


       def start_functn(self):
              if self.var_folder_name.get() != "":
                     c=0
                     for i in self.all_files:
                                   #file_directory + '\\' + i
                                   if os.path.isfile( os.path.join( self.folder_directory , i )) == True:
                                          c+=1
                                          self.create_folder( i.split('.')[-1], i )
                                          self.label_total.config(text = "Total : " + str(self.count))
                                          self.label_moved.config(text = "Moved : " + str(c))
                                          self.label_left.config(text = "Left : " + str(self.count - c))

                                          self.label_total.update()
                                          self.label_moved.update()
                                          self.label_left.update()
                                          
                                   #print("Total Files: {} | Done: {} | Left: {}".format(length,count,length-count))
                                          #c+=1
                     self.label_status.config(text = "Status : Done")
                     messagebox.showinfo("Success", "All Files Have Moved Successfully...")
              
              else:
                     messagebox.showinfo("Error","Please Select Folder First...")
       
       def clear_functn(self):
              self.var_folder_name.set("")
              self.label_status.config(text = "Status : " )
              self.label_total.config(text = "Total : 0")
              self.label_moved.config(text = "Moved : 0")
              self.label_left.config(text = "Left : 0")
              
              self.label_total_image.config(text = "Total Images \n 0")
              self.label_total_audio.config(text = "Total Audios \n 0")
              self.label_total_video.config(text = "Total Videos \n 0")
              self.label_total_document.config(text = "Total Documents \n 0")
              self.label_total_archive.config(text = "Total Archives \n 0")

              self.label_total_other.config(text = "Others \n 0")

              self.label_total_files.config(text = "Total Files : 0")
                                         


       def browse_folder(self):
              op = filedialog.askdirectory(title = "Select Folder For Sorting And Clearing..")
              if op != None:
                     #print(op)
                     self.var_folder_name.set(str(op))
                     self.folder_directory = self.var_folder_name.get()
                     self.other_name = "others"
                     self.rename_folder()

                     self.all_files = os.listdir(self.folder_directory)

                     length = len(self.all_files)
                     count = 1
                     self.Total_count()


                     #print(self.all_files)

                     #* for filename in self.all_files:
                     #     print(filename)

                     # for i in self.all_files:
                     #        #file_directory + '\\' + i
                     #        if os.path.isfile( os.path.join( self.folder_directory , i )) == True:
                     #               self.create_folder( i.split('.')[-1], i )
                     #        print("Total Files: {} | Done: {} | Left: {}".format(length,count,length-count))
                     #        count+=1

       
       def rename_folder(self):
              for folder in os.listdir(self.folder_directory):
                     if os.path.isdir( os.path.join( self.folder_directory , folder )) == True:       
                            os.rename(os.path.join(self.folder_directory,folder ), os.path.join(self.folder_directory, folder.lower()))
                

       def create_folder (self,extension, file_name):
              find = False
              for folder_name in self.folders:
                     #print(extension,file_name)
                     if folder_name in self.folders:
                            if '.'+ extension in self.folders[folder_name]:
                                   if folder_name not in os.listdir(self.folder_directory):
                                          os.mkdir(os.path.join(self.folder_directory,folder_name))
                                   shutil.move(os.path.join(self.folder_directory,file_name), os.path.join(self.folder_directory,folder_name))
                                   find = True
                                   break

              if find != True:
                     if self.other_name not in os.listdir(self.folder_directory):
                            os.mkdir(os.path.join(self.folder_directory ,self.other_name ))
                     shutil.move(os.path.join(self.folder_directory,file_name), os.path.join( self.folder_directory, self.other_name ))
                            #print('found ', folder_name)
                            #break





root = Tk()
obj = Sorting_Folder(root)
root.mainloop()


