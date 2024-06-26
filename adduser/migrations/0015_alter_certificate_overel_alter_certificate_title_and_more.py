# Generated by Django 5.0.4 on 2024-05-02 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adduser', '0014_alter_certificate_overel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='overel',
            field=models.CharField(choices=[('B2', 'B2'), ('C1', 'C1')], max_length=2, verbose_name='Overel'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='title',
            field=models.CharField(choices=[('english', 'english'), ('others', 'others'), ('nemesis', 'nemesis')], max_length=300, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='title',
            field=models.CharField(choices=[('english', 'english'), ('others', 'others'), ('nemesis', 'nemesis')], max_length=300, verbose_name='Language'),
        ),
    ]
