from django.db import models

class Report(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    generated_at = models.DateTimeField(auto_now_add=True)
    report_data = models.JSONField()

    def __str__(self):
        return self.title
