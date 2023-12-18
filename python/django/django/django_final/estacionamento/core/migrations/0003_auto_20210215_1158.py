# Generated by Django 3.1.6 on 2021-02-15 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210215_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cor',
            name='id_cor',
        ),
        migrations.RemoveField(
            model_name='marca',
            name='id_marca',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='id_pessoa',
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='id_veiculo',
        ),
        migrations.AddField(
            model_name='cor',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marca',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='veiculo',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]