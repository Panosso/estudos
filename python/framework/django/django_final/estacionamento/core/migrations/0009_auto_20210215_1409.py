# Generated by Django 3.1.6 on 2021-02-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210215_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='id_pessoa',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
