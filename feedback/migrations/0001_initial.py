# Generated by Django 4.1.7 on 2023-04-13 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('game_choice', models.CharField(choices=[('chat', 'chat'), ('quiz', 'quiz')], max_length=100)),
                ('message', models.CharField(max_length=350)),
            ],
        ),
    ]
