from django.db import models

class RecordType(models.Model):
    title = models.CharField(max_length=30)


class Record(models.Model):
    text = models.TextField(null=True)
    phone = models.CharField(max_length=15)
    preferred_timing = models.TimeField()
    record_type = models.ForeignKey(RecordType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

