# Generated by Django 4.2.7 on 2023-11-28 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lms_video', '0002_rename_category_id_video_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bkash_number', models.CharField(max_length=50)),
                ('trx_id', models.CharField(max_length=100)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms_video.video')),
            ],
        ),
    ]