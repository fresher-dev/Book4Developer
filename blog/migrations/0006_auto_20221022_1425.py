# Generated by Django 3.2 on 2022-10-22 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('blog', '0005_alter_post_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='tags.Tag'),
        ),
    ]
