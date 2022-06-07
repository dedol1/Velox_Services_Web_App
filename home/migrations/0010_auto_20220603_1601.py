# Generated by Django 2.2.5 on 2022-06-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_create_service_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_provider',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('image2', models.FileField(blank=True, null=True, upload_to='images/service_provider')),
            ],
        ),
        migrations.AlterField(
            model_name='create_service',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
