# Generated by Django 5.1.2 on 2024-11-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_person_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
