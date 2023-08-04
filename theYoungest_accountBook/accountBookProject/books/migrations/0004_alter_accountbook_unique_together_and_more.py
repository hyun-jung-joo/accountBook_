# Generated by Django 4.2.1 on 2023-08-04 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_accountbook_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='accountbook',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='accountbook',
            name='category',
            field=models.TextField(default='카테고리', null=True),
        ),
        migrations.AddField(
            model_name='accountbook',
            name='memo',
            field=models.TextField(default='소비내역', null=True),
        ),
        migrations.AddField(
            model_name='accountbook',
            name='money',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='accountbook',
            name='type_name',
        ),
        migrations.RemoveField(
            model_name='accountbook',
            name='writer',
        ),
    ]