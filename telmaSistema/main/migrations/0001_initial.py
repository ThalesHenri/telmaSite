# Generated by Django 5.1.1 on 2024-09-18 23:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.IntegerField(unique=True)),
                ('telefone', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=100)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='Imagens_Produto/')),
            ],
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valorPago', models.DecimalField(decimal_places=2, max_digits=100)),
                ('pagamento', models.BooleanField(default=False)),
                ('quantidadeProdutos', models.IntegerField(default=1)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cliente')),
                ('produtoComprado', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.produto')),
            ],
        ),
    ]
