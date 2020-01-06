# Generated by Django 2.2.7 on 2019-12-11 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_types', models.CharField(choices=[('checking', 'CHECKING'), ('savings', 'SAVINGS'), ('credit', 'CREDIT'), ('debit', 'DEBIT')], default=('savings', 'SAVINGS'), max_length=8)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_email', models.EmailField(max_length=300)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.Branch')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bank.Customer'),
        ),
    ]
