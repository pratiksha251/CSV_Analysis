from django.db import models

# Create your models here.
#class File(models.Model):
 #   file = models.FileField(upload_to="files")



class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

#adding below line to analysis_file
class AnalysisFile(models.Model):
    file_name = models.CharField(max_length=255)
    file_data = models.BinaryField()        