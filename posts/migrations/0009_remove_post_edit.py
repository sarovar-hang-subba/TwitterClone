# Generated by Django 4.0.3 on 2022-03-25 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_post_body_alter_post_email_alter_post_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='edit',
        ),
    ]
