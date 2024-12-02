# Generated by Django 5.1.3 on 2024-12-02 14:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_blog_category_blog_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog.category'),
        ),
    ]
