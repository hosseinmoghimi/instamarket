# Generated by Django 3.1 on 2020-08-14 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('short_desc', models.CharField(max_length=1000, verbose_name='شرح کوتاه')),
                ('description', models.CharField(max_length=10000, verbose_name='شرح کامل')),
                ('thumb_image_origin', models.ImageField(upload_to='dashboard/images/Blog/', verbose_name='تصویر کوچک')),
                ('big_image_origin', models.ImageField(upload_to='dashboard/images/Blog/big/', verbose_name='تصویر بزرگ')),
                ('priority', models.IntegerField(verbose_name='ترتیب')),
                ('author', models.CharField(max_length=50, verbose_name='توسط')),
                ('date_added', models.CharField(max_length=50, verbose_name='تاریخ')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50, verbose_name='نام')),
                ('lname', models.CharField(max_length=50, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('subject', models.CharField(max_length=50, verbose_name='عنوان پیام')),
                ('message', models.CharField(max_length=50, verbose_name='متن پیام')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='افزوده شده در')),
            ],
            options={
                'verbose_name': 'ContactMessage',
                'verbose_name_plural': 'ContactMessages',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='شماره')),
                ('question', models.CharField(max_length=200, verbose_name='سوال')),
                ('answer', models.CharField(max_length=5000, verbose_name='پاسخ')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
            },
        ),
        migrations.CreateModel(
            name='GalleryPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('thumb_image_origin', models.ImageField(upload_to='dashboard/images/GalleryPhoto/', verbose_name='تصویر')),
                ('image_origin', models.ImageField(upload_to='dashboard/images/GalleryPhoto/', verbose_name='تصویر')),
                ('priority', models.IntegerField(verbose_name='ترتیب')),
            ],
            options={
                'verbose_name': 'GalleryPhoto',
                'verbose_name_plural': 'GalleryPhotoes',
            },
        ),
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='عنوان')),
                ('body', models.CharField(blank=True, max_length=500, null=True, verbose_name='پیام')),
                ('image_origin', models.ImageField(upload_to='dashboard/images/HomeSlider/', verbose_name='تصویر')),
                ('action_link', models.CharField(blank=True, max_length=1100, null=True, verbose_name='لینک')),
                ('action_text', models.CharField(blank=True, max_length=50, null=True, verbose_name='متن دکمه')),
                ('priority', models.IntegerField(default=100, verbose_name='ترتیب')),
            ],
            options={
                'verbose_name': 'HomeSlider',
                'verbose_name_plural': 'HomeSliders',
            },
        ),
        migrations.CreateModel(
            name='MainPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('سایت', 'سایت'), ('سوالات', 'سوالات'), ('ویدیو', 'ویدیو'), ('درباره ما', 'درباره ما')], max_length=50, verbose_name='جای تصویر')),
                ('image_origin', models.ImageField(blank=True, null=True, upload_to='dashboard/images/MainPic/', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'MainPic',
                'verbose_name_plural': 'MainPics',
            },
        ),
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50, verbose_name='key')),
                ('value', models.CharField(max_length=50, verbose_name='value')),
                ('content', models.CharField(max_length=2000, verbose_name='content')),
            ],
            options={
                'verbose_name': 'MetaData',
                'verbose_name_plural': 'MetaDatas',
            },
        ),
        migrations.CreateModel(
            name='OurService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('icon', models.CharField(choices=[('account_circle', 'account_circle'), ('add_shopping_cart', 'add_shopping_cart'), ('alarm', 'alarm'), ('attach_file', 'attach_file'), ('attach_money', 'attach_money'), ('backup', 'backup'), ('build', 'build'), ('chat', 'chat'), ('dashboard', 'dashboard'), ('delete', 'delete'), ('description', 'description'), ('face', 'face'), ('favorite', 'favorite'), ('get_app', 'get_app'), ('home', 'home'), ('important_devices', 'important_devices'), ('link', 'link'), ('local_shipping', 'local_shipping'), ('lock', 'lock'), ('mail', 'mail'), ('notification_important', 'notification_important'), ('psychology', 'psychology'), ('publish', 'publish'), ('reply', 'reply'), ('schedule', 'schedule'), ('send', 'send'), ('settings', 'settings'), ('share', 'share'), ('sync', 'sync'), ('vpn_key', 'vpn_key')], default='settings', max_length=50, verbose_name='آیکون')),
                ('description', models.CharField(max_length=500, verbose_name='توضیحات')),
                ('priority', models.IntegerField(verbose_name='ترتیب')),
            ],
            options={
                'verbose_name': 'OurService',
                'verbose_name_plural': 'OurServices',
            },
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('job', models.CharField(max_length=100, verbose_name='سمت')),
                ('description', models.CharField(max_length=500, verbose_name='توضیحات')),
                ('priority', models.IntegerField(verbose_name='ترتیب')),
                ('image_origin', models.ImageField(upload_to='dashboard/images/OurTeam/', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'OurTeam',
                'verbose_name_plural': 'OurTeams',
                'db_table': 'OurTeam',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('درباره ما کوتاه', 'درباره ما کوتاه'), ('درباره ما کامل', 'درباره ما کامل'), ('موبایل', 'موبایل'), ('آدرس', 'آدرس'), ('شرح کوتاه', 'شرح کوتاه'), ('ایمیل', 'ایمیل'), ('عنوان', 'عنوان'), ('واحد پول', 'واحد پول'), ('زیرعنوان', 'زیرعنوان'), ('عنوان ویدیو', 'عنوان ویدیو'), ('لینک ویدیو', 'لینک ویدیو'), ('تلفن', 'تلفن'), ('ارتباط با ما', 'ارتباط با ما'), ('کد پستی', 'کد پستی'), ('لینک', 'لینک'), ('قوانین', 'قوانین'), ('عنوان تیم ما', 'عنوان تیم ما'), ('لینک تیم ما', 'لینک تیم ما'), ('پیام درخواست نامعتبر', 'پیام درخواست نامعتبر')], max_length=50, verbose_name='نام')),
                ('value', models.CharField(max_length=10000, verbose_name='مقدار')),
            ],
            options={
                'verbose_name': 'Parameter',
                'verbose_name_plural': 'Parameters',
            },
        ),
        migrations.CreateModel(
            name='ProfileTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_profile_id', models.IntegerField(verbose_name='از')),
                ('to_profile_id', models.IntegerField(verbose_name='به')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('amount', models.IntegerField(verbose_name='مبلغ')),
                ('cash_type', models.CharField(choices=[('CASH', 'CASH'), ('CHEQUE', 'CHEQUE'), ('CARD', 'CARD')], default='CASH', max_length=50, verbose_name='نوع پرداخت')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='شرح')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در ')),
            ],
            options={
                'verbose_name': 'ProfileTransaction',
                'verbose_name_plural': 'ProfileTransactions',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('خواف', 'خواف'), ('نشتیفان', 'نشتیفان'), ('سنگان', 'سنگان'), ('قاسم آباد', 'قاسم آباد'), ('تایباد', 'تایباد'), ('تربت جام', 'تربت جام'), ('فریمان', 'فریمان'), ('مشهد', 'مشهد'), ('تهران', 'تهران'), ('تربت حیدریه', 'تربت حیدریه')], default='خواف', max_length=50, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
            },
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('icon', models.CharField(choices=[('account_circle', 'account_circle'), ('add_shopping_cart', 'add_shopping_cart'), ('alarm', 'alarm'), ('attach_file', 'attach_file'), ('attach_money', 'attach_money'), ('backup', 'backup'), ('build', 'build'), ('chat', 'chat'), ('dashboard', 'dashboard'), ('delete', 'delete'), ('description', 'description'), ('face', 'face'), ('favorite', 'favorite'), ('get_app', 'get_app'), ('home', 'home'), ('important_devices', 'important_devices'), ('link', 'link'), ('local_shipping', 'local_shipping'), ('lock', 'lock'), ('mail', 'mail'), ('notification_important', 'notification_important'), ('psychology', 'psychology'), ('publish', 'publish'), ('reply', 'reply'), ('schedule', 'schedule'), ('send', 'send'), ('settings', 'settings'), ('share', 'share'), ('sync', 'sync'), ('vpn_key', 'vpn_key')], default='settings', max_length=50, verbose_name='آیکون')),
                ('link', models.CharField(max_length=50, verbose_name='لینک')),
                ('priority', models.IntegerField(verbose_name='ترتیب')),
            ],
            options={
                'verbose_name': 'شبکه اجتماعی',
                'verbose_name_plural': 'SocialLinks',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_origin', models.ImageField(upload_to='dashboard/images/Testimonial/', verbose_name='تصویر')),
                ('title', models.CharField(max_length=2000, verbose_name='عنوان')),
                ('body', models.CharField(max_length=2000, verbose_name='متن')),
                ('footer', models.CharField(max_length=200, verbose_name='پانوشت')),
                ('priority', models.IntegerField(verbose_name='ترتیب')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
            },
        ),
        migrations.AddField(
            model_name='link',
            name='color',
            field=models.CharField(choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('primary', 'primary'), ('secondary', 'secondary'), ('info', 'info')], default='primary', max_length=50, verbose_name='color'),
        ),
        migrations.AddField(
            model_name='link',
            name='icon',
            field=models.CharField(choices=[('account_circle', 'account_circle'), ('add_shopping_cart', 'add_shopping_cart'), ('alarm', 'alarm'), ('attach_file', 'attach_file'), ('attach_money', 'attach_money'), ('backup', 'backup'), ('build', 'build'), ('chat', 'chat'), ('dashboard', 'dashboard'), ('delete', 'delete'), ('description', 'description'), ('face', 'face'), ('favorite', 'favorite'), ('get_app', 'get_app'), ('home', 'home'), ('important_devices', 'important_devices'), ('link', 'link'), ('local_shipping', 'local_shipping'), ('lock', 'lock'), ('mail', 'mail'), ('notification_important', 'notification_important'), ('psychology', 'psychology'), ('publish', 'publish'), ('reply', 'reply'), ('schedule', 'schedule'), ('send', 'send'), ('settings', 'settings'), ('share', 'share'), ('sync', 'sync'), ('vpn_key', 'vpn_key')], default='link', max_length=50, verbose_name='icon'),
        ),
        migrations.AddField(
            model_name='link',
            name='image_origin',
            field=models.ImageField(blank=True, null=True, upload_to='dashboard/images/Link/', verbose_name='image'),
        ),
        migrations.AddField(
            model_name='link',
            name='priority',
            field=models.IntegerField(default=100, verbose_name='priority'),
        ),
        migrations.AddField(
            model_name='link',
            name='url',
            field=models.CharField(default='#', max_length=1100, verbose_name='url'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('فعال', 'فعال'), ('غیر فعال', 'غیر فعال')], default='فعال', max_length=50, verbose_name='وضعیت')),
                ('first_name', models.CharField(max_length=200, verbose_name='نام')),
                ('last_name', models.CharField(max_length=200, verbose_name='نام خانوادگی')),
                ('mobile', models.CharField(blank=True, max_length=50, null=True, verbose_name='موبایل')),
                ('bio', models.CharField(blank=True, max_length=500, null=True, verbose_name='درباره')),
                ('image_origin', models.ImageField(blank=True, max_length=1200, null=True, upload_to='dashboard/images/Profile/', verbose_name='تصویر')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.region', verbose_name='region')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('body', models.CharField(blank=True, max_length=500, null=True, verbose_name='توضیحات')),
                ('link', models.CharField(blank=True, max_length=1100, null=True, verbose_name='link')),
                ('seen', models.BooleanField(default=False, verbose_name='دیده شد')),
                ('priority', models.IntegerField(default=1000, verbose_name='اولویت')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('date_seen', models.DateTimeField(verbose_name='تاریخ دیده شده')),
                ('icon', models.CharField(default='notification_important', max_length=50, verbose_name='آیکون')),
                ('color', models.CharField(blank=True, choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('primary', 'primary'), ('secondary', 'secondary'), ('info', 'info')], default='info', max_length=500, null=True, verbose_name='رنگ')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.profile', verbose_name='پروفایل')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('file', models.FileField(upload_to='dashboard/images/Document', verbose_name='فایل ضمیمه')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date_added')),
                ('row_number', models.IntegerField(default=10000, verbose_name='row_number')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.profile', verbose_name='پروفایل')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
    ]
