Creating a simple blog app with Django, ORM, and PostgreSQL involves a few steps. Here's how you can build it step by step:
give me blog app in django and also orm and also postgres
### Prerequisites:
- Python (preferably 3.7+)
- Django installed (`pip install django`)
- PostgreSQL database installed and running
- `psycopg2` (PostgreSQL adapter for Python) installed (`pip install psycopg2`)

### Steps to Create the Blog App:

#### Step 1: Set up a Django project
First, start a new Django project.

1. **Create the Django project:**

```bash
django-admin startproject blog_project
cd blog_project
```

2. **Create a Django app called 'blog':**

```bash
python manage.py startapp blog
```

#### Step 2: Set up PostgreSQL Database

1. **Create a PostgreSQL Database:**

```bash
psql -U postgres
CREATE DATABASE blog_db;
```

2. **Update your PostgreSQL credentials in `settings.py`:**

In `blog_project/settings.py`, configure the DATABASES section for PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'your_postgres_user',  # replace with your PostgreSQL user
        'PASSWORD': 'your_postgres_password',  # replace with your PostgreSQL password
        'HOST': 'localhost',  # assuming it's hosted locally
        'PORT': '5432',
    }
}
```

3. **Install PostgreSQL adapter for Django:**

```bash
pip install psycopg2
```

#### Step 3: Define Models for the Blog App (ORM)

In `blog/models.py`, define the blog model for the posts.

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
```

#### Step 4: Create the Views

In `blog/views.py`, create views to display and create blog posts.

```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# View for the list of posts
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# View for creating a new post
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

# View for a single post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
```

#### Step 5: Create Forms for Post Creation

In `blog/forms.py`, create a form to create new blog posts.

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
```

#### Step 6: Define URLs

In `blog/urls.py`, define the URL patterns.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'),
]
```

In `blog_project/urls.py`, include the `blog` app's URLs.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

#### Step 7: Create Templates

1. **Create `blog/templates/blog/post_list.html`:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Blog</title>
</head>
<body>
    <h1>Blog Posts</h1>
    <ul>
        {% for post in posts %}
            <li>
                <a href="{% url 'post_detail' post.pk %}">{{ post.title }}</a>
                <p>{{ post.content|truncatewords:20 }}</p>
                <p>By {{ post.author }} on {{ post.created_at }}</p>
            </li>
        {% endfor %}
    </ul>
    <a href="{% url 'post_create' %}">Create a new post</a>
</body>
</html>
```

2. **Create `blog/templates/blog/post_create.html`:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Create a Post</title>
</head>
<body>
    <h1>Create a New Post</h1>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
</body>
</html>
```

3. **Create `blog/templates/blog/post_detail.html`:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ post.title }}</title>
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
    <p>By {{ post.author }} on {{ post.created_at }}</p>
    <a href="{% url 'post_list' %}">Back to list</a>
</body>
</html>
```

#### Step 8: Run Migrations

Now run the migrations to create the necessary database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### Step 9: Create a Superuser (Optional)

You can create a superuser to access the Django admin interface:

```bash
python manage.py createsuperuser
```

#### Step 10: Start the Server

Finally, start the development server:

```bash
python manage.py runserver
```

Now, visit `http://127.0.0.1:8000/` in your browser to view your blog app. You can create, view, and list posts, and also access the Django admin panel at `http://127.0.0.1:8000/admin/`.

### Conclusion

You now have a basic Django blog application using the PostgreSQL database with Django ORM for handling data models. This is just a starting point; you can further enhance the app by adding features such as authentication, comments, categories, tags, etc.





give me like live project with all the things

If you're looking for a fully functional live project for a Django blog with all the features—PostgreSQL, ORM, and templates—I'll outline a project structure with code that you can clone and run. You can either set this up on your local machine or deploy it on a platform like Heroku, DigitalOcean, or any cloud platform.

Here's a complete structure for your live Django Blog project:

### Step-by-Step Guide to Set Up a Complete Django Blog Project

### 1. **Create the Django Project**

Run the following commands in your terminal to create a new project and app:

```bash
django-admin startproject blog_project
cd blog_project
python manage.py startapp blog
```

### 2. **Install Required Packages**

Ensure you have `psycopg2` (PostgreSQL adapter) and other required dependencies:

```bash
pip install django psycopg2
```

### 3. **Set up PostgreSQL Database**

1. **Create a PostgreSQL Database**:
    First, create a PostgreSQL database for your project. You can run this in your terminal:

    ```bash
    psql -U postgres
    CREATE DATABASE blog_db;
    ```

2. **Update `settings.py` for PostgreSQL Configuration**:

   In `blog_project/settings.py`, modify the `DATABASES` setting for PostgreSQL.

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'blog_db',
           'USER': 'your_postgres_user',  # Replace with your PostgreSQL username
           'PASSWORD': 'your_postgres_password',  # Replace with your PostgreSQL password
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

3. **Migrate the Database**:

   ```bash
   python manage.py migrate
   ```

### 4. **Define the Models for Blog Post**

In `blog/models.py`, create a `Post` model:

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
```

### 5. **Create Forms for Blog Post Creation**

In `blog/forms.py`, create a form for adding new blog posts:

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
```

### 6. **Create Views for Blog Posts**

In `blog/views.py`, write views for listing posts, viewing a single post, and creating a new post:

```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# View for the list of posts
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# View for creating a new post
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

# View for a single post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
```

### 7. **Add URL Patterns**

In `blog/urls.py`, define URL patterns for the blog:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'),
]
```

In `blog_project/urls.py`, include the blog app URLs:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

### 8. **Create Templates for Blog Views**

Create the following templates inside `blog/templates/blog/`.

1. **`post_list.html`**:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Blog</title>
</head>
<body>
    <h1>Blog Posts</h1>
    <ul>
        {% for post in posts %}
            <li>
                <a href="{% url 'post_detail' post.pk %}">{{ post.title }}</a>
                <p>{{ post.content|truncatewords:20 }}</p>
                <p>By {{ post.author }} on {{ post.created_at }}</p>
            </li>
        {% endfor %}
    </ul>
    <a href="{% url 'post_create' %}">Create a new post</a>
</body>
</html>
```

2. **`post_create.html`**:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Create a Post</title>
</head>
<body>
    <h1>Create a New Post</h1>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
</body>
</html>
```

3. **`post_detail.html`**:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ post.title }}</title>
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
    <p>By {{ post.author }} on {{ post.created_at }}</p>
    <a href="{% url 'post_list' %}">Back to list</a>
</body>
</html>
```

### 9. **Run the Development Server**

Once all files are created, run the Django development server:

```bash
python manage.py runserver
```

Now, you should be able to visit `http://127.0.0.1:8000/` to view the blog. You can add new posts, view the post list, and view the details of individual posts.

### 10. **Optional: Set Up Admin Panel**

You can also set up the Django admin panel to manage blog posts. To do this, register the `Post` model in `blog/admin.py`:

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Then, you can access the admin panel at `http://127.0.0.1:8000/admin/` after creating a superuser:

```bash
python manage.py createsuperuser
```

### 11. **Deployment (Optional)**

To make this project live, you can deploy it using platforms like **Heroku** or **DigitalOcean**. For Heroku deployment, you can follow these basic steps:

1. **Install Heroku CLI** and log in.
2. **Create a `Procfile`**:

    ```bash
    echo "web: gunicorn blog_project.wsgi" > Procfile
    ```

3. **Install `gunicorn`**:

    ```bash
    pip install gunicorn
    ```

4. **Push the project to Heroku**:

    ```bash
    git init
    heroku create
    git add .
    git commit -m "Initial commit"
    git push heroku master
    ```

    After the app is deployed, you'll be provided with a Heroku URL where you can access the live project.

---

### Final Thoughts

This structure provides you with a fully working blog app using Django, PostgreSQL, and ORM. You can expand it by adding features like authentication (e.g., login/logout for users), user roles, categories/tags for posts, search functionality, or even deploying it to production using Heroku, AWS, or another cloud platform.

Let me know if you need more guidance on deploying or adding additional features!