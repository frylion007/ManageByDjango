# Generated by Django 2.2.3 on 2019-07-20 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20190720_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleclass',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subs', to='news.ArticleClass', verbose_name='父类'),
        ),
    ]
