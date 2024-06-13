# CSV_Analysis
python project using django analysis of file
This Django-based web application allows users to upload CSV files and perform data analysis using pandas and numpy. Uploaded files are stored in a database, and basic data analysis such as displaying the first few rows, calculating summary statistics, and identifying missing values is performed. The results, including histograms generated using matplotlib and seaborn, are displayed on a user-friendly web interface. The application consists of a Django project with an analysis app, including models, views, forms, and templates. The setup requires configuring Django settings, URLs, and applying migrations. Users can easily upload CSV files and view detailed analysis results through a web browser.
Display the analysis results and visualizations on the web interface.
analysis/models.py, define a model to handle file uploads
analysis/forms.py, define a form to upload CSV files
analysis/views.py, update your view to handle file uploads and save them to the database
analysis/urls.py, ensure your URLs are defined
Create templates for file upload and displaying results.
Update your settings.py to include the analysis app and configure file upload settings

create a project using command:
      django-admin startproject csv_analysis
      
create an app using command:
      python manage.py startapp analysis
      
Apply Migrations : 
      python manage.py migrate
      
Run the Development Server:
      python manage.py runserver

