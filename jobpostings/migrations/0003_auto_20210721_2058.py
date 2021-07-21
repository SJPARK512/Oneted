# Generated by Django 3.2.5 on 2021-07-21 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobpostings', '0002_tagcategory_is_multiple_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='benefit',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='main_task',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='preference',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='requirement',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
