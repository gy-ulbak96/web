# Generated by Django 2.2 on 2019-07-28 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QandA', '0003_auto_20190714_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userqa',
            name='username',
        ),
        migrations.AddField(
            model_name='userqa',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userqa',
            name='reader',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userqa',
            name='question',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userqa',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
