# Generated by Django 4.0.6 on 2022-07-30 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rentrecord_confirmatin_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentrecord',
            old_name='confirmatin_code',
            new_name='confirmation_code',
        ),
    ]