# Generated by Django 3.2.4 on 2021-07-15 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210714_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goals',
            name='calories',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='goals',
            name='carbohydrates',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='goals',
            name='fats',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='goals',
            name='protein',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='macros',
            name='calories',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='macros',
            name='carbohydrates',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='macros',
            name='fats',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='macros',
            name='protein',
            field=models.IntegerField(),
        ),
    ]