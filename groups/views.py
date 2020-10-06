from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.db import connection

from groups.models import Group


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['owner_name', 'group_name', 'group_course', 'group_primary_language', 'group_secondary_language','meeting_time','meeting_day', 'meeting_location']

def group_list(request, template_name='groups/group_list.html'):
    #group = Group.objects.all()
    #group = Group.objects.raw('SELECT * FROM groups_group WHERE name = \'Please\'')
    group = Group.objects.raw('SELECT * FROM groups_group')
    data = {}
    data['object_list'] = group
    return render(request, template_name, data)
  


def group_search_course(request, template_name='groups/group_search_course.html'):
    query = request.POST
    data = {}
    if( len(query.keys())  == 0 ):
        return render(request,template_name, data)
    
    query = request.POST['query']
    print("\nSearching based off course\n")
    print("Result is:", query)
    print("End of result\n\n")

    group = Group.objects.raw('SELECT * FROM groups_group WHERE group_course = %s', [query])
    print(group)
    data['object_list'] = group
    return render(request, "groups/group_list.html", data)


def group_view(request, pk, template_name='groups/group_detail.html'):
    group = get_object_or_404(Group, pk=pk)
    return render(request, template_name, {'object':group})

def group_create(request, template_name='groups/group_form.html'):
    form = GroupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('groups:group_list')
    return render(request, template_name, {'form': form})

def group_update(request, pk, template_name='groups/group_form.html'):
    group = get_object_or_404(Group, pk=pk)
    form = GroupForm(request.POST or None, instance=group)
    if form.is_valid():
        form.save()
        return redirect('groups:group_list')
    
    return render(request, template_name, {'form':form})

def group_delete(request, pk, template_name='groups/group_confirm_delete.html'):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('groups:group_list')
    return render(request, template_name, {'object': group})


def search_availability (request,template_name='groups/search_availability.html'):
    time = request.POST.get('time')
    day = request.POST.get('day')
    course = request.POST.get("course")
    data = {}
    time_row = []
    suggested_times = []
    with connection.cursor() as cursor:
        cursor.execute('SELECT count(*) FROM(SELECT *  FROM groups_group  meeting_time WHERE meeting_time = %s and meeting_day = %s and group_course = %s) as yeet', [time, day, course])
        row = cursor.fetchone()
        if(row[0] > 0):
            group = Group.objects.raw('SELECT id  FROM groups_group WHERE  meeting_day = %s and group_course = %s',[ day, course])
            cursor.execute('SELECT meeting_time FROM groups_group WHERE  meeting_day = %s and group_course = %s',[day, course])
            time_row = cursor.fetchall()
            for i in range(9, 23):
                avv = 0
                for x in time_row:
                    if(x[0] == i):
                        avv = 1
                if(avv == 0):
                    suggested_times.append(i)
    d = dict.fromkeys(suggested_times, 0)

    print(d)

    return render(request, template_name, {'d':d})

def group_search_course_language(request, template_name='groups/group_search_course_language.html'):
    data = {}
    
    course = request.POST.get('course')
    lang = request.POST.get('lang')
  
    group = Group.objects.raw('SELECT * FROM groups_group WHERE (group_course = %s and (group_primary_language = %s) OR (group_course = %s and group_secondary_language = %s))', [course, lang, course, lang])
    data['object_list'] = group
    return render(request,template_name, data)




