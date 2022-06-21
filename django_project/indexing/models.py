from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class StudentGroup(models.Model):
    """ Группа студентов """
    teacher = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name='Преподаватель',
        related_name='student_groups',
        related_query_name='student_groups'
    )
    title = models.CharField(verbose_name='Название группы', unique=True, max_length=1000)

    class Meta:
        verbose_name = 'Группы студентов'
        verbose_name_plural = 'Группа студентов'

    def __str__(self):
        return """ Название группы:  {}""".format(self.title)


class Lecture(models.Model):
    """ Занятия """
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Преподаватель')
    title = models.CharField(verbose_name='Тема занятия', max_length=1000, help_text='Теория большого взрыва')
    date = models.DateField(verbose_name='Дата проведения')
    time = models.IntegerField(verbose_name='Длительность занятия', default=45)
    group = models.ManyToManyField(StudentGroup, verbose_name='Группа студентов', help_text='Это список доступных групп, '
                                                                                     'выберите у какой группы будет '
                                                                                     'занятие')

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятий'

    def __str__(self):
        return """Занятие: {}""".format(self.title)


class Students(models.Model):
    """ Студенты """
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Преподаватель')
    full_name = models.CharField(verbose_name='Фамилия Имя', max_length=1000, help_text='Савельев Максим')
    key = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, verbose_name='Группа')

    class Meta:
        verbose_name = 'Студента'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return """Студент: {}""".format(self.full_name)


class Grade(models.Model):
    """ Оценка """
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Преподаватель')
    grades = models.IntegerField(verbose_name='Оценка',  default=0)
    key = models.ForeignKey(Lecture, verbose_name='За занятие', on_delete=models.CASCADE)
    key_to_student = models.ManyToManyField(Students, verbose_name='Студентам')

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return """ Оценка: {}, за занятие: {}""".format(self.grades, self.key.title)


class List_Of_Control_Activities(models.Model):
    """ Лист контрольных мероприятий """
    FACULTY_CHOICES = [
        ('МиП', 'МиП'),
        ('ТД', 'ТД'),
        ('КТиИБ', 'КТиИБ'),
        ('УЭФ', 'УЭФ'),
        ('ЭиФ', 'ЭиФ'),
        ('ЛиЖ', 'ЛиЖ'),
        ('ЮФ', 'ЮФ'),
    ]
    faculty = models.CharField(max_length=20, verbose_name='факультет', choices=FACULTY_CHOICES, default='КТиИБ')
    dean = models.CharField(max_length=350, verbose_name='декан')
    head_department = models.CharField(max_length=350, verbose_name='Зав.Кафедрой')
    date_of_approval = models.DateField(verbose_name='дата утверждения')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Преподаватель')
    department = models.CharField(max_length=350, verbose_name='Кафедра')
    discipline = models.CharField(max_length=350, verbose_name='Дисциплина')
    course = models.IntegerField(verbose_name='Курс')
    semester = models.IntegerField(verbose_name='Семестр')
    group = models.ForeignKey(StudentGroup, verbose_name='Группа', on_delete=models.CASCADE)
    NAME_PA_CHOICES = [
        ('Экзамен', 'Экзамен'),
        ('Зачёт', 'Зачёт'),
    ]
    name_pa = models.CharField(verbose_name='Вид ПА', max_length=20, choices=NAME_PA_CHOICES, default='Экзамен')
    order_holding_pa = models.CharField(verbose_name='Порядок проведения ПА', max_length=350)
    evaluation_scale_pa = models.CharField(verbose_name='Шкала оценивания ПА', max_length=350)
    evaluation_criteria_pa = models.TextField(verbose_name='Критерии оценивания ПА')

    class Meta:
        verbose_name = 'Лист контрольных мероприятий'
        verbose_name_plural = 'Листы контрольных мероприятий'

    def __str__(self):
        return """ЛКМ {} / {}""".format(self.group.title, self.date_of_approval)


class List_Of_Control_Activities_Value(models.Model):
    """ Лист контрольных мероприятий содержание"""
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Преподаватель')
    check_point = models.IntegerField(verbose_name='Контрольная точка')
    grade_service = models.CharField(verbose_name='Оценочное средство', max_length=350)
    form_holding = models.CharField(verbose_name='Форма проведения', max_length=350)
    order_holding = models.CharField(verbose_name='Порядок проведения', max_length=350)
    evaluation_scale = models.CharField(verbose_name='Шкала оценивания', max_length=350)
    evaluation_criteria = models.TextField(verbose_name='Критерии оценивания')
    value = models.ForeignKey(
        List_Of_Control_Activities,
        verbose_name='Содержание',
        on_delete=models.CASCADE,
        related_name='lca_items'
    )

    class Meta:
        verbose_name = ' Лист контрольных мероприятий содержание'
        verbose_name_plural = ' Лист контрольных мероприятий содержание'

    def __str__(self):
        return """  Лист контрольных мероприятий """


class GradeService(models.Model):
    """Оценочное средство"""
    name = models.CharField(
        verbose_name='Название',
        blank=False,
        null=False,
        max_length=350,
        unique=True,
    )

    class Meta:
        verbose_name = 'Оценочное средство'
        verbose_name_plural = 'Оценочные средства'

    def __str__(self):
        return self.name


class OrderHolding(models.Model):
    """Порядок проведения"""
    description = models.TextField(
        verbose_name='Описание',
        blank=False,
        null=False,
        unique=True,
    )

    class Meta:
        verbose_name = 'Порядок проведения'
        verbose_name_plural = 'Порядки проведения'

    def __str__(self):
        return self.description


class FormHolding(models.Model):
    """Форма проведения"""
    description = models.TextField(
        verbose_name='Описание',
        blank=False,
        null=False,
        unique=True,
    )

    class Meta:
        verbose_name = 'Форма проведения'
        verbose_name_plural = 'Формы проведения'

    def __str__(self):
        return self.description


class CheckPoint(models.Model):
    """Контрольная точка"""
    lca = models.ForeignKey(
        List_Of_Control_Activities,
        verbose_name='ЛКМ',
        on_delete=models.CASCADE,
        related_name='lca_checkpoints'
    )
    number = models.SmallIntegerField(verbose_name='Номер')
    date = models.DateField(verbose_name='Дата')

    class Meta:
        verbose_name = 'Контрольная точка'
        verbose_name_plural = 'Контрольные точки'

    def __str__(self):
        return f'{self.lca} КТ №: {self.number}, Дата: {self.date}'


class GradeServiceSet(models.Model):
    """Группа оценочных средств"""
    check_point = models.ForeignKey(
        CheckPoint,
        verbose_name='Контрольная точка',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    grade_service = models.ForeignKey(
        GradeService,
        verbose_name='Оценочное средство',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    form_holding = models.ForeignKey(
        FormHolding,
        verbose_name='Форма проведения',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    order_holding = models.ForeignKey(
        OrderHolding,
        verbose_name='Порядок проведения',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    evaluation_quantity = models.IntegerField(verbose_name='Количество')
    evaluation_rate = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=False,
        blank=False,
        verbose_name='Баллов за единицу'
    )
    evaluation_scale = models.TextField(
        verbose_name='Шкала оценивания',
        null=True,
        blank=True,
    )
    evaluation_criteria = models.TextField(verbose_name='Критерии оценивания')

    class Meta:
        verbose_name = 'Группа оценочных средств'
        verbose_name_plural = 'Группы оценочных средств'

    def __str__(self):
        return f'{self.check_point} - {self.grade_service}'


class GradeItem(models.Model):
    """Занятие (оценочное средство)"""
    grade_service_set = models.ForeignKey(
        GradeServiceSet,
        verbose_name='Группа оценочных стредств',
        on_delete=models.CASCADE,
        related_name='lca_grade_items'
    )
    date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата занятия',
    )

    class Meta:
        verbose_name = 'Занятие (оценочное средство)'
        verbose_name_plural = 'Занятия (оценочное средства)'
        ordering = ['grade_service_set', 'date']

    def __str__(self):
        return f'{self.grade_service_set} - {self.date}'


class GradeResult(models.Model):
    """Результаты занятия"""
    grade_item = models.ForeignKey(
        GradeItem,
        verbose_name='занятие',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        Students,
        verbose_name='студент',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    score = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=False,
        blank=False,
        verbose_name='оценка'
    )

    class Meta:
        verbose_name = 'Результат (оценка)'
        verbose_name_plural = 'Результаты (оценки)'
        unique_together = ['grade_item', 'student']

    def __str__(self):
        return f'{self.student}, {self.grade_item} - {self.score}'

