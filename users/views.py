from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.db import connection

from users.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'user_course', 'user_primary_language', 'user_secondary_language','user_preferred_time','user_preferred_day', 'user_preferred_location']

def user_list(request, template_name='users/user_list.html'):

    user = User.objects.raw('SELECT * FROM users_user')
    data = {}
    data['object_list'] = user
    return render(request, template_name, data)

def user_view(request, pk, template_name='users/user_detail.html'):
    user = get_object_or_404(User, pk=pk)
    return render(request, template_name, {'object':user})

def user_create(request, template_name='users/user_form.html'):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('users:user_list')
    return render(request, template_name, {'form': form})

def user_update(request, pk, template_name='users/user_form.html'):
    user = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('users:user_list')
    
    return render(request, template_name, {'form':form})

def user_delete(request, pk, template_name='users/user_confirm_delete.html'):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users:user_list')
    return render(request, template_name, {'object': user})



def user_find_friends(request, template_name='users/user_find_friends.html'):
     # This function will find what groups accomdate their language
    course = request.POST
    data = {}
    if( len(course.keys())  == 0 ):
        return render(request,template_name, data)

    course = request.POST['course']
    print("\nSearching based off course\n")
    print("Result is:", course)
    print("End of result\n\n")
    question = 'SELECT * FROM (SELECT DISTINCT user_name as name FROM groups_group INNER JOIN users_user ON group_course = user_course WHERE group_course LIKE \'%' + course + '%\' UNION SELECT DISTINCT owner_name as name FROM groups_group INNER JOIN users_user ON group_course = user_course WHERE user_course LIKE  \'%' + course + '%\') AS n;'
    with connection.cursor() as cursor:
        cursor.execute(question)
        data = cursor.fetchall()
    result = {}
    output = []
    for element in data:
        print(element[0]) 
        temp = element[0]
        output.append(element[0])
        result.update({temp:0})
    print("")   
    if(len(data) != 0):
        print(data)
    
    print(output)

    return render(request, template_name, {'d':result})
