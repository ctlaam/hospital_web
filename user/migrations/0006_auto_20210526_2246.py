# Generated by Django 2.2 on 2021-05-26 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210525_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donviyte',
            name='ten',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='donviyte',
            name='trangthaidonvi',
            field=models.CharField(choices=[('1', 'Hoạt động'), ('0', 'Không hoạt động')], default='', max_length=20, null=True),
        ),
    ]
