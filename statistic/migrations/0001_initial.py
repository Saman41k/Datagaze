# Generated by Django 5.0.3 on 2024-04-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='order')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('icon', models.ImageField(upload_to='statistic/icon/', verbose_name='icon')),
            ],
            options={
                'verbose_name': 'Statistic ',
                'verbose_name_plural': '3 Statistics',
                'db_table': 'statistic',
                'ordering': ('order',),
            },
        ),
    ]