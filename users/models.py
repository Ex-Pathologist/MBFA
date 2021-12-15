from django.db import models


class Users(models.Model):
    """Пользователи"""

    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    date_of_birthday = models.DateField()
    sex = models.CharField("Пол", max_length=7)
    place_of_birth = models.CharField("Место рождения", max_length=100)
    place_of_life = models.CharField("Адрес проживания", max_length=100)
    education = models.CharField("Образование", max_length=100)
    profession = models.CharField("Занимаемая должность", max_length=50)
    is_doctor = models.BooleanField(default=False)
    id_cards = models.IntegerField()

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Cards(models.Model):
    """Карточки пациентов"""

    id_cards = models.ForeignKey(Users, verbose_name='Номер карточки', on_delete=models.SET_NULL, null=True)
    # id_tests = models.IntegerField(auto_created=)
    # visites =
    # diagnosis
