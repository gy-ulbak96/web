# Generated by Django 2.2 on 2019-08-09 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QandA', '0009_remove_answerqa_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userqa',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
