# Generated by Django 4.1.2 on 2022-10-16 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Execucao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.cliente')),
                ('tarefa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.tarefa')),
            ],
        ),
        migrations.DeleteModel(
            name='Etapa_Cliente',
        ),
    ]
