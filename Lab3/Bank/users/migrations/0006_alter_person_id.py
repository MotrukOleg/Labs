# Generated by Django 5.1.2 on 2024-11-10 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_person_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user'),
        ),
    ]
