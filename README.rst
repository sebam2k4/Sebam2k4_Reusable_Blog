====================================
Reusable Django Blog App by sebam2k4
====================================

NEED FIX: currently getting an error after loading the app and making migrations: Exception Type: TemplateDoesNotExist, Exception Value: blog/blogposts.html

Working on Fix

Basic reusable Blog App for your Django project

App Name: sebam2k4_reusable_blog

Views:

- Post List
- Post Detail
- Top Posts
- New Post
- Edit Post

Forms:

- BlogPostForm with fields: title, content, image, tag, and published_date

dependencies:

- django-disqus
- pillow

Quick start
-----------

1. Make sure you have a virtualenv active for your project. You'll have to update the requirements.txt file by adding the following::

    git+https://github.com/sebam2k4/sebam2k4_reusable_blog.git

2. Run to install the dependencies::

    pip install -r requirements.txt

3. Add 'sebam2k4_reusable_blog' to your INSTALLED_APPS in your settings.py like this::

    INSTALLED_APPS = (
        ...
        'sebam2k4_reusable_blog',
    )

4. Include the polls URLconf in your project urls.py like this::

    url(r'^blog/', include('sebam2k4_reusable_blog.urls')),

5. Run `python manage.py migrate` to create the blog models.

6. Add a link to the Blog page in your project's base.html::

    <li><a href="{% url 'post_list' %}">Our Blog</a></li>

7. Visit http://127.0.0.1:8000/blog/ to view the blog.

8. Note: EDIT POST buttons in the postdetail.html template is hidden if user is not authenticated. Log in as superuser or any user to reavel the button in the UI.

Disqus Setup
------------

1. Set your Disqus shortcode and id constants in your project's settings.py::

    DISQUS_WEBSITE_SHORTNAME = 'your-shortcode'
    SITE_ID = 'your-id'

Media files
-----------

1. Add 'django.template.context_processors.media' to your TEMPLATES' context_processors in your settings.py::

    TEMPLATES = [
        {
            ...
            'OPTIONS': {
                'context_processors': [
                    ...
                    'django.template.context_processors.media',
                ],
            },
        },
    ]

2. Set media root and url in your settings.py. This is where images uploaded to posts will be saved. For example::

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
