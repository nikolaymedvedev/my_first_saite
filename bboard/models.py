from django.db import models

# Create your models here.

class Bb(models.Model):
	title = models.CharField( max_length=50, verbose_name="Товар", help_text="поле заголовка", default="Типо заголовок",)
	content = models.TextField(null = True, blank=True, verbose_name="Описание", help_text="основное поле", default="Типо текс")
	price = models.FloatField(null=True, blank=True, verbose_name="Цена", help_text="поле цены",)
	published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликованно", help_text="поле даты",)
	rubrik = models.ForeignKey("Rubrik", null=True, on_delete=models.PROTECT, verbose_name="Рубрика", help_text="поле рубрики",)

	 
	def __str__(self):
		return "Товар"
	
	class Meta:
		verbose_name_plural = "обьявления"
		verbose_name = "обьявление"
		ordering = ["-published"]

class Rubrik(models.Model):
	name = models.CharField(max_length=20, db_index=True, verbose_name="Название")
	
	def __str__(self):
		return self.name
		
	class Meta:
		verbose_name_plural = "рубрики"
		verbose_name = "рубрика"
		ordering = ["name"]