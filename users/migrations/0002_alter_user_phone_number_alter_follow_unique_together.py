# Generated by Django 5.0.6 on 2024-06-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('from_user', 'to_user')},
        ),
    ]
