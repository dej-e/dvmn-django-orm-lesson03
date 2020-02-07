import random

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from .models import Chastisement, Commendation, Lesson, Mark, Schoolkid

COMMENDATIONS = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!',
]


def get_child(child_name):
    try:
        return Schoolkid.objects.get(full_name__contains=child_name)
    except ObjectDoesNotExist:
        print(f'Школьника с именем {child_name} нет в базе')
    except MultipleObjectsReturned:
        print(f'Уточните имя школьника, школьников с {child_name} больше одного')
    


def fix_mark(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for mark in marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def get_lesson(year, letter, subject_title):
    return Lesson.objects.filter(
        year_of_study=year,
        group_letter=letter,
        subject__title=subject_title
    ).order_by('date').first()


def create_commendation(schoolkid, subject):
    
    lesson = get_lesson(
        schoolkid.year_of_study,
        schoolkid.group_letter,
        subject
    )

    if lesson:
        Commendation.objects.create(
            text=random.choice(COMMENDATIONS),
            created=lesson.date,
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher
        )
