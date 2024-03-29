# Generated by Django 4.1.3 on 2023-05-23 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguros', '0004_terms_userseguro_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Privacidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privacidad', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserSeguroInfo',
            fields=[
            ],
            options={
                'verbose_name': 'User Seguro Info',
                'verbose_name_plural': 'Users Seguro Info',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('seguros.userseguro',),
        ),
        migrations.AlterField(
            model_name='account',
            name='medio_cotizacion',
            field=models.CharField(choices=[('WP', 'WhatsApp'), ('LL', 'Llamado')], max_length=50),
        ),
        migrations.AlterField(
            model_name='autoflotaseguro',
            name='uso',
            field=models.CharField(choices=[('P', 'Particular'), ('C', 'Comercial')], max_length=25),
        ),
        migrations.AlterField(
            model_name='autoseguro',
            name='uso',
            field=models.CharField(choices=[('P', 'Particular'), ('C', 'Comercial')], max_length=25),
        ),
        migrations.AlterField(
            model_name='comercioseguro',
            name='m2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comercioseguro',
            name='valor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='hogarseguro',
            name='m2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hogarseguro',
            name='marca_modelo_bici',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='hogarseguro',
            name='tipo_bici',
            field=models.CharField(choices=[('NO', 'No agrego bicicleta'), ('SI', 'Si, dentro y fuera del domicilio')], max_length=40),
        ),
        migrations.AlterField(
            model_name='hogarseguro',
            name='valor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='hogarseguro',
            name='valor_bici',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='motoseguro',
            name='uso',
            field=models.CharField(choices=[('P', 'Particular'), ('C', 'Comercial')], max_length=25),
        ),
    ]
