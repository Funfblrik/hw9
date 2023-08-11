from django.db import models
from django.utils.html import format_html
from django.contrib import admin
class Advertisement(models.Model):
    title = models.CharField('заголовок', max_length=128)
    desrciption = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%T%p")
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time)
        return self.created_at.strftime("%m-%d-%Y %T %p")

    @admin.display(description='Дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%T%p")
            return format_html('<span style="color: red; font-weight: bold;">Сегодня в {}</span>', updated_time)
        return self.updated_at.strftime("%m-%d-%Y %T %p")
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"
    class Meta:
        db_table = "advertisements"