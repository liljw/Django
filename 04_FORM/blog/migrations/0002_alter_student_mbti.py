# Generated by Django 3.2.18 on 2023-03-29 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mbti',
            field=models.CharField(choices=[('QWER', 'q w e r'), ('ASDF', 'a s d f'), ('POIU', 'p o i u')], max_length=4),
        ),
    ]
