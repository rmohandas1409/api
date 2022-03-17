# Generated by Django 4.0.3 on 2022-03-15 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatares/')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('descricao', models.CharField(blank=True, max_length=280, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=14)),
                ('contato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ramais.contato')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.EmailField(max_length=255)),
                ('contato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ramais.contato')),
            ],
        ),
        migrations.AddField(
            model_name='contato',
            name='grupos',
            field=models.ManyToManyField(to='ramais.grupo'),
        ),
    ]
