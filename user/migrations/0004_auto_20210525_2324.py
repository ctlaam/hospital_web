# Generated by Django 2.2 on 2021-05-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210525_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donviyte',
            name='trangthaidonvi',
            field=models.CharField(choices=[('1', 'Hoạt động'), ('0', 'Không hoạt động')], default='', max_length=20),
        ),
    ]
