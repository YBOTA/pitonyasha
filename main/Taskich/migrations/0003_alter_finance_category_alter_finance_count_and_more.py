# Generated by Django 4.2.16 on 2024-12-24 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Taskich', '0002_catfin_alter_task_options_alter_task_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Taskich.catfin', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='finance',
            name='count',
            field=models.BigIntegerField(default=0, verbose_name='Сколько'),
        ),
        migrations.AlterField(
            model_name='finance',
            name='desc',
            field=models.TextField(verbose_name='Описание транзакции'),
        ),
        migrations.AlterField(
            model_name='finance',
            name='nameF',
            field=models.TextField(verbose_name='Название транзакции'),
        ),
    ]
