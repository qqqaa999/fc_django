# Generated by Django 4.0 on 2022-02-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0002_alter_fcuser_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcuser',
            name='level',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], default='user', max_length=8, verbose_name='등급'),
            preserve_default=False,
        ),
    ]
