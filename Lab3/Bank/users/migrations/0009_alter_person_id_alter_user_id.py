# Generated by Django 5.1.2 on 2024-11-10 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='ID',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ID',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
