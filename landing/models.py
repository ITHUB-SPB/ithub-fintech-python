from django.db import models

class RecordType(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title} (id={self.pk})'

    class Meta:
        verbose_name: "тип заявки"
        verbose_name_plural: "типы заявок"


class Record(models.Model):
    text = models.TextField(null=True)
    phone = models.CharField(max_length=15)
    preferred_timing = models.TimeField(verbose_name='удобное время звонка')
    record_type = models.ForeignKey(RecordType, on_delete=models.CASCADE, verbose_name='тип заявки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата заявки')

    def __str__(self):
        return f'Заявка #{self.pk} ({self.phone})'

    class Meta:
        verbose_name = "заявка"
        verbose_name_plural = "заявки"


class Messages(models.Model):
    theme = models.CharField(max_length=15, null=False)
    message = models.CharField(max_length=400, null=False)
    attachment = models.FileField(null=True)

    def __str__(self):
        return f'Сообщение #{self.pk} ({self.theme})'

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"
