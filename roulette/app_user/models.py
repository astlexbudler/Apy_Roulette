from django.db import models

class VISIT(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=20)
    visit_date = models.DateTimeField(auto_now_add=True)