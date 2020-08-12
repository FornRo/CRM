from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CompanyAddress(models.Model):
    address = models.CharField('Адрес', max_length=255)
    phone_number = models.CharField('Номер телефона', max_length=100)
    e_mail = models.EmailField('E-mail', primary_key=True)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'{self.phone_number}|{self.e_mail}'

class Descriptin(models.Model):
    description = models.TextField('Описание')

    def __str__(self):
        return self.description

class Record(models.Model):
    name_company = models.CharField('Название компании', max_length=100)
    name_manager = models.CharField('ФИО руководителя', max_length=100)
    description_id = models.OneToOneField(Descriptin, on_delete=models.CASCADE)
    crt_date = models.DateField('Дата создание', auto_now_add=True, editable=False)
    date_record = models.DateField('Дата изменения записи', auto_now=True, editable=False)
    address = models.OneToOneField('CompanyAddress', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.pk} {self.name_company}'

class Project(models.Model):
    name_project = models.CharField('Название проекта', max_length=255)
    description_id = models.OneToOneField(Descriptin, on_delete=models.CASCADE)
    start_date = models.DateField('Сроки начала')
    deadline = models.DateField('Срок окончания')
    cost = models.FloatField('Стоимость')
    status = models.BooleanField('Статус')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'{self.pk} {self.name_project}'

class Communication(models.Model):
    communication = models.CharField('Канала обращения', max_length=25)

    def __str__(self):
        return self.communication

class Interaction(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Record, on_delete=models.CASCADE)
    communication_id = models.ForeignKey(Communication, on_delete=models.DO_NOTHING)
    # id Menedjers (id USER)
    description_id = models.OneToOneField(Descriptin, on_delete=models.CASCADE, blank=True)
    appraisal = models.PositiveSmallIntegerField('Оценка', default=0)  # оценки от 0 до 10

    class Meta:
        verbose_name = 'Взаимодействия'
        verbose_name_plural = 'Взаимодействия'

    def __str__(self):
        return f'{self.pk}  "{self.project_id} | {self.company_id}"'
