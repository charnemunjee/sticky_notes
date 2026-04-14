### **Sticky Notes application**



#### Overview

The project is a sticky notes application. The application allows the user to create a number of sticky notes on a webpage. The following functionalities are possible in the sticky notes app:

* view all sticky notes
* add new sticky notes to the list 
* delete a sticky note
* edit an existing sticky note



#### Installation

The project is written in python using Django. This project also includes four HTML files and one css file



**Clone the project on GitHub**

Navigate to the terminal VS code

Type the following into the VS code terminal:

&#x09;cd <link where sticky\_notes app should be stored> 	

&#x09;git clone https://github.com/charnemunjee/sticky\_notes 

&#x09;

**Create a virtual environment IN VSCode**

* type the following command into the terminal: 

&#x09;python -m venv venv



**Install dependencies**

As stated in the requirements.txt file, the following packages need to be installed

* asgiref==3.11.1
* Django==6.0.3
* sqlparse==0.5.5
* tzdata==2025.3

Install these packages by running the following terminal: 

&#x09;pip install -r requirements.txt



**Collect the static folders and apply migrations**

Type the following into the commands in the terminal:

* python manage.py collectstatic
* python manage.py makemigrations
* python manage.py migrate



**Run the development server**

Type the following into the command prompt

* python manage.py runserver



sqlite3 should be created - includes a database table with the sticky note information



#### Views

The sticky notes will have the following views:



**Base View**

The base view allows the user to do the following:

* add a sticky note
* click on a sticky note to view more details of the sticky note



**Detailed sticky note view**

Clicking on the sticky note title allows the user the option to:

* View the details of the sticky note
* Update the sticky note
* Go back to the previous view
* Delete the sticky note - This removes the sticky note and it is no longer displayed in the base view (list of sticky notes)



**Update sticky note**

The web page allows the user to edit the Title and detail/content of the sticky note

The button at the bottom allows the user to save the updated sticky note

The link below the button allows the user to go back to the base view



**Add sticky note**

Clicking "Add sticky note" takes the user to a webpage where they can enter the title and content of the sticky note.

The button at the bottom allows the user to save the sticky note

The "Back to list" button allows the user to return to the base view

