# Generated by Django 5.1 on 2024-08-30 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_content_alter_post_posttitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimage',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='수정날짜'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]
