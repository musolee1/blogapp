# Generated by Django 5.1.3 on 2024-12-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_blog_blog_date_alter_blog_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]