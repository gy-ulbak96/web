# Generated by Django 2.2 on 2019-08-09 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QandA', '0010_auto_20190809_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='userqa',
            name='a_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userqa',
            name='answer',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Answerqa',
        ),
    ]