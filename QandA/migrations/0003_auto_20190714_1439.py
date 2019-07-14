# Generated by Django 2.2 on 2019-07-14 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QandA', '0002_auto_20190713_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='userqa',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='userqa',
            name='question',
            field=models.CharField(max_length=100, null=True, verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='userqa',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]