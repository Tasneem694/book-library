# Generated by Django 4.2.5 on 2023-09-23 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admn', '0013_alter_books_borow_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='retrn_dt',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
