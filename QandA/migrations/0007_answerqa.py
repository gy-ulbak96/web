# Generated by Django 2.2 on 2019-07-29 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QandA', '0006_userqa_a_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answerqa',
            fields=[
                ('userqa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='QandA.Userqa')),
                ('a_title', models.CharField(max_length=100, null=True)),
                ('answer', models.CharField(max_length=100, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
