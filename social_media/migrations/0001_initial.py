# Generated by Django 5.0.3 on 2024-04-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='order')),
                ('icon', models.ImageField(upload_to='social_media/icons/', verbose_name='icon')),
                ('link', models.URLField(max_length=255, verbose_name='link')),
            ],
            options={
                'verbose_name': 'SocialMedia ',
                'verbose_name_plural': '8 SocialMedias',
                'db_table': 'social_media',
                'ordering': ('order',),
            },
        ),
    ]