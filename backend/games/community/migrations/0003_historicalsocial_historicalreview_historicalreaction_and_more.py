# Generated by Django 4.1.7 on 2023-04-17 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0003_historicalsubgenre_historicalproductlanguage_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_historicalsystemrequirement_historicalproduct'),
        ('community', '0002_alter_media_type_alter_reaction_like_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalSocial',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('type', models.CharField(choices=[('FACEBOOK', 'FaceBook'), ('VKONTAKTE', 'VKontakte'), ('SITE', 'Site'), ('YOUTUBE', 'YouTube'), ('TWITTER', 'Twitter'), ('TWITCH', 'Twitch'), ('TELEGRAM', 'Telegram')], default='SITE', max_length=9, verbose_name='Social_media')),
                ('url', models.URLField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, db_constraint=False, limit_choices_to={'type': 'GAMES'}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.product')),
            ],
            options={
                'verbose_name': 'historical social',
                'verbose_name_plural': 'historical socials',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalReview',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('user_uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('text', models.TextField()),
                ('grade', models.CharField(choices=[('LIKE', 'Like'), ('DISLIKE', 'Dislike')], max_length=7, verbose_name='Grade')),
                ('view_type', models.BooleanField(default=True)),
                ('can_reply', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('game', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.product')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('language', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='reference.language')),
            ],
            options={
                'verbose_name': 'historical Review',
                'verbose_name_plural': 'historical Reviews',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalReaction',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('user_uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('like_type', models.CharField(choices=[('LIKE', 'Like'), ('DISLIKE', 'Dislike')], max_length=7, verbose_name='Grade')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('review', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='community.review')),
            ],
            options={
                'verbose_name': 'historical Like/Dislike',
                'verbose_name_plural': 'historical Likes/Dislikes',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMedia',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('file_link', models.TextField(max_length=100)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('type', models.CharField(choices=[('GAME_LOGO', 'Game Logo'), ('PHOTO_SLIDER', 'Photo Slider')], max_length=12, verbose_name='Media_file')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.product')),
            ],
            options={
                'verbose_name': 'historical media',
                'verbose_name_plural': 'historical medias',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalComment',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('user_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('text', models.TextField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('review', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='community.review')),
            ],
            options={
                'verbose_name': 'historical Comment',
                'verbose_name_plural': 'historical Comments',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]