# Generated by Django 4.1.2 on 2022-10-14 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_evento_usuario_alter_evento_data_criacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local_evento',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Local do evento'),
        ),
    ]
