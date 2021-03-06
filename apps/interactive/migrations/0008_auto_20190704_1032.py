# Generated by Django 2.2.2 on 2019-07-04 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactive', '0007_auto_20190703_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interactives',
            name='background',
            field=models.ImageField(blank=True, default='interactive/default.png', null=True, upload_to='interactive/%Y/%m', verbose_name='背景图'),
        ),
        migrations.AlterField(
            model_name='interactives',
            name='next_content',
            field=models.ManyToManyField(blank=True, related_name='_interactives_next_content_+', to='interactive.Interactives', verbose_name='下一个内容'),
        ),
    ]
