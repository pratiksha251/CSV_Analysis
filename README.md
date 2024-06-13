# CSV_Analysis
python project using django analysis of file
Upload CSV files through a web form.
Store the uploaded files in the database.
Perform basic data analysis using pandas and numpy.
Display the first few rows of the data.
Calculate summary statistics (mean, median, standard deviation) for numerical columns.
Identify and handle missing values.
Generate basic plots using matplotlib and seaborn.
Display the analysis results and visualizations on the web interface.
analysis/models.py, define a model to handle file uploads
analysis/forms.py, define a form to upload CSV files
analysis/views.py, update your view to handle file uploads and save them to the database
analysis/urls.py, ensure your URLs are defined
Create templates for file upload and displaying results.
Update your settings.py to include the analysis app and configure file upload settings

Apply Migrations : 
      python manage.py migrate
      
Run the Development Server:
      python manage.py runserver

