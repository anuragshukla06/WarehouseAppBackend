# Generated by Django 2.2.2 on 2019-06-09 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190609_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropandprice',
            name='warehouse',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='main.warehouse'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cropandprice',
            name='crop',
            field=models.CharField(max_length=200),
        ),
    ]
