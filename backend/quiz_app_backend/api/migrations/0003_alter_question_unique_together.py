# Generated by Django 4.1.3 on 2025-02-14 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_question_question_number_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('quiz', 'question_number')},
        ),
    ]
