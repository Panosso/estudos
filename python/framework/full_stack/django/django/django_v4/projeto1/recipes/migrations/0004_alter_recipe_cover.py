# Generated by Django 4.1.2 on 2023-05-03 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cover',
            field=models.ImageField(blank=True, upload_to='recipes/cover/%Y/%m/%d/'),
        ),
    ]