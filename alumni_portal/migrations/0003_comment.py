# Generated by Django 2.2.5 on 2020-06-07 17:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_portal', '0002_alumnistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='alumni_portal.Post')),
            ],
        ),
    ]
