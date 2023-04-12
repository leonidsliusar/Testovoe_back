# Generated by Django 4.2 on 2023-04-12 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menu_options_menu_url_alter_menu_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['branch', 'title'], 'verbose_name': 'Меню', 'verbose_name_plural': 'Меню'},
        ),
        migrations.AddField(
            model_name='menu',
            name='branch',
            field=models.IntegerField(default=0),
        ),
    ]