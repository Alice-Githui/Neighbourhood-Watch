# Generated by Django 3.2.4 on 2021-06-05 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighborapp', '0002_remove_neighbourhood_occupants_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='neighborhoud',
            new_name='neighbourhood',
        ),
    ]