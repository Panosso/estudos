# Generated by Django 3.1.6 on 2021-02-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210215_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='observacao',
        ),
        migrations.AlterField(
            model_name='cor',
            name='cor',
            field=models.CharField(default='preto', max_length=100),
        ),
    ]