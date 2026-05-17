# 📋 Docket — Smart Task Management System

A full-stack web application for managing daily tasks, built with **Python (Django)** as a part of the **4th Semester Elective Python Full Stack Web Development** course at LNCT University, Bhopal.

---

## 🖼️ Overview

Docket is a beginner-friendly task manager that lets users **create, organize, and track tasks** with priorities, categories, and statuses. Every user gets their own private workspace after registering — no one else can see or edit their tasks.

---

## ✨ Features

- 🔐 **User Authentication** — Register, Login, Logout (each user's data is private)
- 📊 **Dashboard** — See total, pending, in-progress, and completed task counts at a glance
- ✅ **Task Management (Full CRUD)**
  - Create a new task with title, description, priority, due date, and category
  - View all tasks in a clean table with filters
  - Edit any task
  - Delete a task (with confirmation)
  - Toggle task status: To Do → In Progress → Done
- 🏷️ **Categories** — Create color-coded categories to group related tasks
- 🔍 **Search & Filter** — Filter tasks by status, priority, or search by title
- 👤 **Profile Page** — View account info and task statistics
- 🛠️ **Admin Panel** — Django's built-in admin at `/admin/`

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.x |
| **Framework** | Django 5 |
| **Database** | SQLite3 (built-in) |
| **Frontend** | HTML5, CSS3 |
| **Font** | Poppins (Google Fonts) |
| **Auth** | Django's built-in authentication system |

---

## 📁 Project Structure

```
docket_project/
│
├── manage.py                   # Django management script
├── db.sqlite3                  # SQLite database
│
├── docket_project/             # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tasks/                      # Tasks app (core functionality)
│   ├── models.py               # Task and Category models
│   ├── views.py                # All task-related views
│   ├── urls.py                 # Task URL routes
│   ├── forms.py                # Task and Category forms
│   └── admin.py                # Admin panel config
│
├── accounts/                   # Auth app (login, register, profile)
│   ├── views.py
│   └── urls.py
│
├── templates/                  # All HTML templates
│   ├── base.html               # Base layout with navbar
│   ├── home.html               # Landing page
│   ├── tasks/
│   │   ├── dashboard.html
│   │   ├── task_list.html
│   │   ├── task_form.html
│   │   ├── task_detail.html
│   │   ├── task_confirm_delete.html
│   │   ├── category_list.html
│   │   ├── category_form.html
│   │   └── category_confirm_delete.html
│   └── accounts/
│       ├── login.html
│       ├── register.html
│       └── profile.html
│
└── static/
    └── css/
        └── style.css           # All custom styles
```

---

## 🗄️ Database Models

### Task
| Field | Type | Description |
|---|---|---|
| `title` | CharField | Name of the task |
| `description` | TextField | Optional details |
| `priority` | CharField | Low / Medium / High |
| `status` | CharField | To Do / In Progress / Done |
| `due_date` | DateField | Optional deadline |
| `category` | ForeignKey | Linked category (optional) |
| `user` | ForeignKey | Owner of the task |
| `created_at` | DateTimeField | Auto-set on creation |

### Category
| Field | Type | Description |
|---|---|---|
| `name` | CharField | Category name |
| `color` | CharField | Hex color code |
| `user` | ForeignKey | Owner of the category |

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/SamShri16/Docket-Django---Smart-Task-Management-System.git
cd Docket-Django---Smart-Task-Management-System
```

### 2. Install Django
```bash
pip install django
```

### 3. Apply database migrations
```bash
cd docket_project
python manage.py makemigrations
python manage.py migrate
```

### 4. Create an admin account (optional)
```bash
python manage.py createsuperuser
```

### 5. Start the development server
```bash
python manage.py runserver
```

### 6. Open in your browser
```
http://127.0.0.1:8000/
```

---

## 🔗 URL Routes

| URL | Page |
|---|---|
| `/` | Home / Landing page |
| `/accounts/register/` | Register a new account |
| `/accounts/login/` | Login |
| `/accounts/logout/` | Logout |
| `/accounts/profile/` | User profile |
| `/dashboard/` | Dashboard with stats |
| `/tasks/` | All tasks (with filter) |
| `/tasks/create/` | Create a new task |
| `/tasks/<id>/` | View task details |
| `/tasks/<id>/edit/` | Edit a task |
| `/tasks/<id>/delete/` | Delete a task |
| `/tasks/<id>/toggle/` | Toggle task status |
| `/tasks/categories/` | View all categories |
| `/tasks/categories/create/` | Add a category |
| `/admin/` | Django admin panel |

---

## 📸 Screenshots



---

## 👨‍💻 Developer

**Samarth Shrivastava**  
B.Tech Computer Science Engineering — 4th Semester (171)
LNCT University (SOCST), Bhopal  

---

## 📝 Project Description

> Docket is a full-stack smart task management web application that solves the problem of organizing academic and personal tasks efficiently. It is built using Python (Django framework) for the backend, SQLite for database storage, and HTML5/CSS3 for the responsive frontend. The system supports user authentication (register/login), complete CRUD operations for tasks and categories, priority levels (High/Medium/Low), status tracking (To Do → In Progress → Done), search and filter functionality, and a visual statistics dashboard.

---

## 📄 License

This project is made for academic purposes as part of the LNCTU Python Full Stack Web Development course.
