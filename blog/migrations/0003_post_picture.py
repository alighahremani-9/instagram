# Generated by Django 4.2.5 on 2023-10-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_post_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='profile.jpg', upload_to='post/'),
            preserve_default=False,
        ),
    ]