from datetime import timedelta, datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
	question_text = models.CharField(max_length=200, verbose_name='Текст опроса')
	pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

	class Meta:
		verbose_name = 'Опрос'
		verbose_name_plural = 'Опросы'

	def __str__(self):
		short_text = ' '.join(str(self.question_text).split()[:5])
		date = datetime.strftime(self.pub_date, '%d.%m.%Y')
		return f'Опрос №{self.pk} ({short_text}..., {date})'

	def recent(self):
		return timezone.now() - self.pub_date <= timedelta(days=3)


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200, verbose_name='Текст варианта')
	votes = models.PositiveIntegerField(verbose_name='Количество голосов', default=1)

	class Meta:
		verbose_name = 'Вариант'
		verbose_name_plural = 'Варианты'

	def __str__(self):
		return f'{self.choice_text} (Опрос №{self.question__pk}, {self.votes} голос(ов))'