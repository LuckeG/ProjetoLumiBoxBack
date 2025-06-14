# Generated by Django 5.2.1 on 2025-06-10 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_lb", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Filme",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("duracao", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Genero",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Serie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("qtd_episodios", models.IntegerField()),
                ("qtd_temporadas", models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name="usuario",
            name="email",
        ),
        migrations.RemoveField(
            model_name="usuario",
            name="id_usuario",
        ),
        migrations.RemoveField(
            model_name="usuario",
            name="senha",
        ),
        migrations.AlterField(
            model_name="usuario",
            name="nome",
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name="Obra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=50)),
                ("descricao", models.CharField(max_length=60)),
                ("ano_lancamento", models.IntegerField()),
                ("genero", models.ManyToManyField(to="api_lb.genero")),
            ],
        ),
        migrations.AddField(
            model_name="usuario",
            name="Email",
            field=models.CharField(default="", max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usuario",
            name="Senha",
            field=models.CharField(default="", max_length=30),
            preserve_default=False,
        ),
    ]
