# Generated by Django 3.1 on 2020-08-14 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20200815_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='title',
            field=models.CharField(default='پروژه یک', max_length=50, verbose_name='title'),
            preserve_default=False,
        ),
    ]