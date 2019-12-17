# Generated by Django 3.0 on 2019-12-17 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=100)),
                ('refresh_rate_in_minutes', models.DecimalField(decimal_places=2, max_digits=5)),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('short_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='organizations.Organization')),
            ],
        ),
    ]
