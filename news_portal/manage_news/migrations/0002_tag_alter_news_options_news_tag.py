# Generated by Django 4.1.7 on 2023-03-20 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Тег')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.ManyToManyField(to='manage_news.tag', verbose_name='Теги'),
        ),
    ]