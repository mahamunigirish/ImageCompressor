import sys
import PIL
from PyQt5.QtWidgets import *
import os
from PIL import Image

from PyQt5.QtGui import *
from  PyQt5.QtCore import Qt




class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Simple Image Compressor'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 600
        self.image_width = 0

        self.statusBar().showMessage("Message:")
        self.statusBar().setObjectName('status')
        self.setFixedSize(self.width,self.height)
        self.setObjectName("main_window")
        #self.setStyleSheet(design.stylesheet)
        #self.setStyleSheet('background-color:black')
        stylesheet = ""
        with open("design.qss","r") as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #__________________MAin_Window______________________________________--
        self.single_bubble = QFrame(self)
        #self.frame.setFrameShape(QFrame.StyledPanel)
        #self.frame.setLineWidth(0.6)

        self.single_bubble.setMaximumSize(300,125)
        self.single_bubble.setObjectName("single_buble")
        self.single_bubble.move(50, 100)
        self.single_bubble.mousePressEvent = self.single_bubble_clicked


        self.single_bubble_heading = QLabel(self.single_bubble)
        self.single_bubble_heading.setObjectName("bubble_heading")
        self.single_bubble_heading.move(80,8)
        self.single_bubble_heading.setText("Compress Single Image")

        self.single_bubble_para = QLabel(self.single_bubble)
        self.single_bubble_para.setObjectName("bubble_para")
        self.single_bubble_para.setText("Click here to compress Single Image!")
        self.single_bubble_para.move(25,32)






        #2nd Frame start form here

        self.dir_bubble = QFrame(self)
        self.dir_bubble.move(50, 275)
        self.dir_bubble.setObjectName("dir_bubble")
        self.dir_bubble.mousePressEvent = self.dir_bubble_clicked

        self.dir_bubble_heading = QLabel(self.dir_bubble)
        self.dir_bubble_heading.setObjectName("bubble_heading")
        self.dir_bubble_heading.setText("Compress Multiple Image ")
        self.dir_bubble_heading.move(75,8)



        self.dir_bubble_para = QLabel(self.dir_bubble)
        self.dir_bubble_para.setObjectName("bubble_para")
        self.dir_bubble_para.setText("Want to Compress Multiple images at once select the folder and get compressed version of te images inanother folder")
        self.dir_bubble_para.setWordWrap(True)
        self.dir_bubble_para.move(10,32)

        #___________________------------ENd Main_windoe





#_________________________Functionality________________________________

#_________________________SingleBubble expanded________________--
        self.single_bubble_expanded = QFrame(self)
        self.single_bubble_expanded.setObjectName("bubble_expanded")
        self.single_bubble_expanded.move(50, 100)
        self.single_bubble_expanded.setVisible(False )
        self.back_arrow_s = QLabel(self.single_bubble_expanded)
        self.back_arrow_s.move(25,0)
        self.back_arrow_s.setTextFormat(Qt.RichText)
        self.back_arrow_s.setText("&#8592;")
        self.back_arrow_s.setObjectName("back_arrow")
        self.back_arrow_s.mousePressEvent = self.back_arrow_clicked

        self.single_bubble_heading = QLabel(self.single_bubble_expanded)
        self.single_bubble_heading.setObjectName("bubble_heading")
        self.single_bubble_heading.move(80, 8)
        self.single_bubble_heading.setText("Compress Single Image")

        self.select_image_label = QLabel(self.single_bubble_expanded)
        self.select_image_label.setObjectName("bubble_para")
        self.select_image_label.move(30,50)
        self.select_image_label.setText("Choose Image")

        self.select_image_path = QLineEdit(self.single_bubble_expanded)
        self.select_image_path.setObjectName("path_text")
        self.select_image_path.move(60,85)

        self.browse_button = QPushButton(self.single_bubble_expanded)
        self.browse_button.setObjectName("browse_button")
        self.browse_button.setText("...")
        self.browse_button.clicked.connect(self.select_flie)
        self.browse_button.move(240,85)

        self.select_image_quality = QLabel(self.single_bubble_expanded)
        self.select_image_quality.setObjectName("bubble_para")
        self.select_image_quality.move(30, 130)
        self.select_image_quality.setText("Choose Quality")

        self.select_quality_path = QLineEdit(self.single_bubble_expanded)
        self.select_quality_path.setObjectName("quality_path_text")
        self.select_quality_path.move(60,160)

        self.quaity_combo = QComboBox(self.single_bubble_expanded)
        self.quaity_combo.addItem("High")
        self.quaity_combo.addItem("Medium")
        self.quaity_combo.addItem("Low")
        self.quaity_combo.move(170,160)
        self.quaity_combo.currentIndexChanged.connect(self.quality_current_value)
        self.quaity_combo.setObjectName("quality_combo")
        self.quaity_combo.resize(90,20)

        self.compress_Image = QPushButton(self.single_bubble_expanded)
        self.compress_Image.setObjectName("compress_button")
        self.compress_Image.setText("compress")
        self.compress_Image.move(100,260)
        self.compress_Image.clicked.connect(self.resize_pic)




#________________________single bubble_expanded  end_____________________________________
        self.dir_bubble_expanded = QFrame(self)
        self.dir_bubble_expanded.setObjectName("bubble_expanded")

        self.dir_bubble_expanded.move(50, 100)
        self.dir_bubble_expanded.setVisible(False)
        self.back_arrow_d = QLabel(self.dir_bubble_expanded)
        self.back_arrow_d.move(25, 0)
        self.back_arrow_d.setTextFormat(Qt.RichText)
        self.back_arrow_d.setText("&#8592;")
        self.back_arrow_d.setObjectName("back_arrow")
        self.back_arrow_d.mousePressEvent = self.back_arrow_clicked

        self.dir_bubble_heading = QLabel(self.dir_bubble_expanded)
        self.dir_bubble_heading.setObjectName("bubble_heading")
        self.dir_bubble_heading.move(80, 8)
        self.dir_bubble_heading.setText("Compress Multiple Images")

        self.select_image_label = QLabel(self.dir_bubble_expanded)
        self.select_image_label.setObjectName("bubble_para")
        self.select_image_label.move(30, 50)
        self.select_image_label.setText("Choose Source directory")

        self.select_source_path = QLineEdit(self.dir_bubble_expanded)
        self.select_source_path.setObjectName("path_text")
        self.select_source_path.move(60, 85)

        self.browse_source_button = QPushButton(self.dir_bubble_expanded)
        self.browse_source_button.setObjectName("browse_button")
        self.browse_source_button.setText("...")
        self.browse_source_button.move(240, 85)
        self.browse_source_button.clicked.connect(self.select_folder_source)

        self.select_dest_label = QLabel(self.dir_bubble_expanded)
        self.select_dest_label.setObjectName("bubble_para")
        self.select_dest_label.move(30, 130)
        self.select_dest_label.setText("Choose Destination directory")

        self.select_dest_path = QLineEdit(self.dir_bubble_expanded)
        self.select_dest_path.setObjectName("path_text")
        self.select_dest_path.move(60, 160)

        self.browse_dest_button = QPushButton(self.dir_bubble_expanded)
        self.browse_dest_button.setObjectName("browse_button")
        self.browse_dest_button.setText("...")
        self.browse_dest_button.move(240, 160)
        self.browse_dest_button.clicked.connect(self.select_folder_dest)

        self.select_dir_quality = QLabel(self.dir_bubble_expanded)
        self.select_dir_quality.setObjectName("bubble_para")
        self.select_dir_quality.move(30, 205)
        self.select_dir_quality.setText("Choose Quality")

        self.select_quality_dir_path = QLineEdit(self.dir_bubble_expanded)
        self.select_quality_dir_path.setObjectName("quality_path_text")
        self.select_quality_dir_path.move(60, 235)

        self.quaity_dir_combo = QComboBox(self.dir_bubble_expanded)
        self.quaity_dir_combo.addItem("High")
        self.quaity_dir_combo.addItem("Medium")
        self.quaity_dir_combo.addItem("Low")
        self.quaity_dir_combo.move(170,235)
        self.quaity_dir_combo.currentIndexChanged.connect(self.quality_current_value)
        self.quaity_dir_combo.setObjectName("quality_combo")
        self.quaity_dir_combo.resize(90, 20)

        self.compress_dir = QPushButton(self.dir_bubble_expanded)
        self.compress_dir.setObjectName("compress_button")
        self.compress_dir.setText("compress")
        self.compress_dir.move(100, 290)
        self.compress_dir.clicked.connect(self.resize_folder)


    #________________________directoryBubble expanded---------------

        self.show()

#directory bubble expanded end
    def single_bubble_clicked(self, event):
        print("Single buble clicked")
        self.single_bubble.setVisible(False)
        self.dir_bubble.setVisible(False)
        self.single_bubble_expanded.setVisible(True)
        self.dir_bubble_expanded.setVisible(False)

    def dir_bubble_clicked(self, event):
        print("dir buble clicked")
        self.single_bubble.setVisible(False)
        self.dir_bubble.setVisible(False)
        self.single_bubble_expanded.setVisible(False)
        self.dir_bubble_expanded.setVisible(True)

    def back_arrow_clicked(self,event):
        self.single_bubble.setVisible(True)
        self.dir_bubble.setVisible(True)
        self.single_bubble_expanded.setVisible(False)
        self.dir_bubble_expanded.setVisible(False)

    def select_flie(self):

        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;JPG (*.jpg);;JPEG(*.jpeg)" )
        if fileName:
            print(fileName)
            self.select_image_path.setText(fileName)
            img = Image.open(fileName)
            self.image_width = img.width

            self.select_quality_path.setText(str(self.image_width))


    def select_folder_source(self):
        folder = QFileDialog.getExistingDirectory(self,'Select Directory')
        print(folder)

        self.select_source_path.setText(folder)

        files = os.listdir(folder)
        #print(files)

        first_pic = folder + "/" + files[0]

        img = Image.open(first_pic)
        self.image_width = img.width

        self.select_quality_dir_path.setText(str(self.image_width))






    def select_folder_dest(self):
        folder = QFileDialog.getExistingDirectory(self,'Select Directory')
        print(folder)
        self.select_dest_path.setText(folder)







    def quality_current_value(self):
        if self.quaity_combo.currentText() == "High":
            self.select_quality_path.setText(str(self.image_width))


        if self.quaity_combo.currentText() == "Medium":
            self.select_quality_path.setText(str(int(self.image_width/2)))


        if self.quaity_combo.currentText() == "Low":
            self.select_quality_path.setText(str(int(self.image_width/4)))


        #_____________________________These is for multiple Images______________________________________--
        if self.quaity_dir_combo.currentText() == "High":
            self.select_quality_dir_path.setText(str(self.image_width))

        if self.quaity_dir_combo.currentText() == "Medium":
            self.select_quality_dir_path.setText(str(int(self.image_width/2)))

        if self.quaity_dir_combo.currentText() == "Low":
            self.select_quality_dir_path.setText(str(int(self.image_width/4)))


    def resize_pic(self):

        old_pic = self.select_image_path.text()
        '''if old_pic[-4:] != ".jpg" or old_pic[-5:] != ".jpeg" or old_pic[-4:] != ".png" or old_pic[-4:] != ".JPG" or old_pic[ -5:] != ".JPEG" or old_pic[-4:] != ".PNG":
            self.statusBar().showMessage("Meassage:Please Choose an valid Image")
            return'''

        if old_pic == "" :
                self.statusBar().showMessage("Meassage:Please Choose  an Image")
                return
        print(old_pic)
        print(int(self.select_quality_path.text()))
        directories =self.select_image_path.text().split("/")
        print(directories)
        new_pic = ""
        new_pic_name, okPressed = QInputDialog.getText(self, "Save Image as", "Image name:", QLineEdit.Normal, "")
        if okPressed and new_pic_name != '':
            print(new_pic_name)

            if old_pic[-4:] == 'jpeg':
                new_pic_name+= ".jpeg"

            if old_pic[-4:] == 'jpg':
                new_pic_name+= ".jpg"

            if old_pic[-4:] == 'png':
                new_pic_name+=".png"

            else:
                new_pic_name+=".jpeg"


        for direct in  directories[:-1] :
            new_pic = new_pic + direct+"/"

        new_pic+=new_pic_name
        self.comression_code(old_pic,new_pic, int(self.select_quality_path.text()))
        self.statusBar().showMessage("Message:Compressed")




        print(new_pic)

    def resize_folder(self):
        source_directory = self.select_source_path.text()
        files = os.listdir(source_directory)

        dest_directory = self.select_dest_path.text()

        if dest_directory == "" or source_directory == "":
            self.statusBar().showMessage("Message: Please select source and destination directory")
            return
        i=0

        for file in files :
            i+=1
            print(file)
            if file[-4:] == ".jpg" or file[-5:] == ".jpeg"  or file[-4:] == ".png"  or file[-4:] == ".JPG" or file[-5:] == ".JPEG" or file[-4:] == ".PNG":
                old_pic = source_directory + "/" + file
                new_pic = dest_directory + "/" + file
                img = Image.open(old_pic)
                self.image_width = img.width


                self.select_quality_dir_path.setText(str(self.image_width))


                self.comression_code(old_pic,new_pic,self.image_width)
                total_images = len(file)
                images_done = i
                percentage = int(images_done/total_images*100)
                #print(percentage,"%")
                #self.statusBar().showMessage("Message:Compressed"+str(int(images_done/total_images*100)+"%"))



            else:
                print("Ignore",file)
                continue

        self.statusBar().showMessage("Message:Compressed 100%")








    def comression_code(self,old_pic, new_pic,mywidth):
        try:
            img = Image.open(old_pic)
            #mywidth = int(self.select_quality_path.text())
            wpercent = (mywidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((mywidth, hsize), PIL.Image.ANTIALIAS)
            img.save(new_pic)
        except Exception as e:
            self.statusBar().showMessage("Message:"+e)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
