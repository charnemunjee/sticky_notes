### **Sticky Notes application**



#### Overview

The project is a sticky notes application

The application allows the user to create a number of sticky notes on the webpage. Once a list of sticky notes is made, it is possible to add more sticky notes to the list, delete the sticky notes or edit them



#### Installation

The project is written in python using Django. This project also includes four HTML files and one css file



To install the project, copy the following folders in the "sticky notes" folder, open the folder in VSCode and run the command "python manage.py runserver" in the terminal

* posts
* sticky\_notes
* manage.py
* requirements.txt



As stated in the requirements.txt file, the following packages need to be installed

* asgiref==3.11.1
* Django==6.0.3
* sqlparse==0.5.5
* tzdata==2025.3
* 



#### Views



**Base View**

The base view allows the user to do the following:

* add a sticky note
* click on a sticky note to view more details of the sticky note



**Detailed sticky note view**

Clicking on the sticky note title allows the user the option to:

* Update the sticky note
* View the details of the sticky note
* Go back to the previous view
* Delete the sticky note - This removes the sticky note and it is no longer displayed in the base view (list of sticky notes)



**Update sticky note**

The web page allows the user to edit the Title and detail/Content of the sticky note

The button at the bottom allows the user to save the updated sticky note

The link below the button allows the user to go back to the base view



**Add sticky note**

Clicking "Add sticky note" takes the user to a webpage where they can enter the title and content of the sticky note.

The button at the bottom allows the user to save the sticky note

The "Back to list" button allows the user to return to the base view

