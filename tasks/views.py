from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Task, Category
from .forms import TaskForm, CategoryForm

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    total = tasks.count()
    todo = tasks.filter(status='todo').count()
    in_progress = tasks.filter(status='in_progress').count()
    done = tasks.filter(status='done').count()
    high_priority = tasks.filter(priority='high', status__in=['todo','in_progress'])[:5]
    recent_tasks = tasks[:5]
    context = {
        'total': total, 'todo': todo, 'in_progress': in_progress,
        'done': done, 'high_priority': high_priority, 'recent_tasks': recent_tasks,
    }
    return render(request, 'tasks/dashboard.html', context)

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    # Filters
    status = request.GET.get('status', '')
    priority = request.GET.get('priority', '')
    category = request.GET.get('category', '')
    search = request.GET.get('search', '')
    if status:
        tasks = tasks.filter(status=status)
    if priority:
        tasks = tasks.filter(priority=priority)
    if category:
        tasks = tasks.filter(category__id=category)
    if search:
        tasks = tasks.filter(Q(title__icontains=search) | Q(description__icontains=search))
    categories = Category.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks, 'categories': categories,
        'selected_status': status, 'selected_priority': priority,
        'selected_category': category, 'search': search,
    })

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(user=request.user, data=request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(user=request.user)
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Create'})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(user=request.user, data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(user=request.user, instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Update', 'task': task})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted.')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@login_required
def task_toggle_status(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if task.status == 'todo':
        task.status = 'in_progress'
    elif task.status == 'in_progress':
        task.status = 'done'
    else:
        task.status = 'todo'
    task.save()
    messages.success(request, f'Task marked as {task.get_status_display()}')
    return redirect(request.META.get('HTTP_REFERER', 'task_list'))

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'tasks/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.user = request.user
            cat.save()
            messages.success(request, 'Category created!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'tasks/category_form.html', {'form': form, 'action': 'Create'})

@login_required
def category_delete(request, pk):
    cat = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        cat.delete()
        messages.success(request, 'Category deleted.')
        return redirect('category_list')
    return render(request, 'tasks/category_confirm_delete.html', {'category': cat})
