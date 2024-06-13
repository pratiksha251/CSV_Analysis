from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import views 
from .models import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
from .forms import UploadFileForm
from .models import UploadedFile

# Create your views here.

#def create_db(file_path):
#    df = pd.read_csv(file_path,delimiter=',')
#    print(df)


#def upload_file(request):

 #   if request.method == "POST":
  #      file = request.FILES.get('file')
     #   obj =  File.objects.create(file = file)
    #  create_db(obj.file)
   # return render(request,"analysis/upload.html")

def handle_uploaded_file(file):
    df = pd.read_csv(file)
    return df

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            df = handle_uploaded_file(uploaded_file.file.path)
            df_json = df.to_json()  # Convert DataFrame to JSON string
            return redirect('results', df=df_json)
    else:
        form = UploadFileForm()
    return render(request, 'analysis/upload.html', {'form': form})

def results(request):
    df_json = request.GET.get('df')
    if df_json:
        df = pd.read_json(df_json)

        # Basic data analysis
        head = df.head().to_html()
        summary_stats = df.describe().to_html()
        missing_values = df.isnull().sum().to_html()

        # Visualizations
        plots = {}
        for column in df.select_dtypes(include=np.number).columns:
            plt.figure()
            sns.histplot(df[column].dropna())
            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            image_base64 = base64.b64encode(buf.read()).decode('utf-8')
            buf.close()
            plots[column] = image_base64

        context = {
            'head': head,
            'summary_stats': summary_stats,
            'missing_values': missing_values,
            'plots': plots,
        }
        return render(request, 'analysis/results.html', context)
    return render(request, 'analysis/results.html')