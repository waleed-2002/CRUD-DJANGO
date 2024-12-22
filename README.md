# CRUD-DJANGO
I developed a Django-based web application with a sleek and user-friendly interface to perform CRUD operations seamlessly. The application allows users to add, update, and delete items while integrating features like selecting a location and downloading the created list in PDF format. The project utilizes Django's default SQLite3 database.
## Features  

- **CRUD Operations**:  
  - Add new items to the list.  
  - Update existing items.  
  - Delete unwanted items.  

- **Location Selection**:  
  - Choose a location for each entry using a simple interface.  

- **PDF Export**:  
  - Download the list of items in PDF format with a single click.  

- **Database**:  
  - Uses Django's default SQLite3 database for easy setup and data management.
  - 

## Installation and Setup  

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/waleed-2002/CRUD-DJANGO.git
   cd CRUD-DJANGO

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install django
python manage.py migrate
python manage.py runserver

