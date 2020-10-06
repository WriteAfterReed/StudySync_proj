from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse, StreamingHttpResponse
from collections import namedtuple
from wsgiref.util import FileWrapper


from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter

from groups.models import Group

def analysis(request, template_name='analysis/display.html'):
    meeting_days_analysis()
    meeting_times_analysis()
    popular_courses_analysis()
    return render(request, template_name)


def meeting_times_analysis():
    times = []

    for i in Group.objects.raw('SELECT * FROM groups_group'):
        times.append(i.meeting_time)

    fig, ax = plt.subplots()

    labels = []

    for i in range(min(times), max(times)+1):
        labels.append(i)

    sizeOfCount = max(times) + 1 - min(times)

    countTimes = [0] * sizeOfCount
        
    for i in range(len(times)):
        for j in range(len(labels)):
            if times[i] == labels[j]:
                countTimes[j] = countTimes[j] + 1
                
    plt.bar(labels, countTimes, align='center', alpha=1, edgecolor='black')
    plt.ylabel("Amount of Groups Studying at that Time")
    plt.title("Times of the Day by Amount of Groups Studying") 
    plt.xlabel("Times - 24 hours clock")
    plt.savefig("static/images/meeting_times_graph.png")

def meeting_days_analysis():
    days = []

    figurine, axxx = plt.subplots()

    for i in Group.objects.raw('SELECT * FROM groups_group'):
        days.append(i.meeting_day)

    count = [0,0,0,0,0,0,0]

    for i in range(len(days)):
        if days[i] == 1:
            count[0] = count[0] + 1
        elif days[i] == 2:
            count[1] = count[1] + 1
        elif days[i] == 3:
            count[2] = count[2] + 1
        elif days[i] == 4:
            count[3] = count[3] + 1
        elif days[i] == 5:
            count[4] = count[4] + 1
        elif days[i] == 6:
            count[5] = count[5] + 1
        elif days[i] == 7:
            count[6] = count[6] + 1

    DAYS_OF_WEEK = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
    n = np.arange(len(DAYS_OF_WEEK))

    axxx.bar(DAYS_OF_WEEK, count, align='center', alpha=1, edgecolor='black')
    plt.ylabel("Amount of Groups Studying on the Day")
    plt.title('Days of the Week by Number Groups Studying')
    plt.savefig("static/images/meeting_days_graph.png")

def popular_courses_analysis():
    courses = []

    figure, axx = plt.subplots()

    for i in Group.objects.raw('SELECT * FROM groups_group'):
        courses.append(i.group_course)

    myset = set(courses)
    mylist = list(myset)

    countCourses = [0] * len(myset)

    
    for i in range(len(courses)):
        for j in range(len(mylist)):
            if courses[i] == mylist[j]:
                countCourses[j] = countCourses[j] + 1

    axx.bar(mylist, countCourses, align='center', alpha=1, edgecolor='black')
    plt.xlabel("Courses Of Groups")
    plt.xticks(rotation=90)
    plt.gcf().subplots_adjust(bottom=0.25, left=0.15)
    plt.ylabel("Number of Groups Studying Course")
    plt.title("Courses of Groups by Amount of Groups Studying") 
    plt.savefig("static/images/popular_courses_graph.png")


def meeting_times(request):
    return StreamingHttpResponse(FileWrapper(open('static/images/meeting_times_graph.png', 'rb')), content_type='image/png')

def meeting_days(request):
    return StreamingHttpResponse(FileWrapper(open('static/images/meeting_days_graph.png', 'rb')), content_type='image/png')

def popular_courses(request):
    return StreamingHttpResponse(FileWrapper(open('static/images/popular_courses_graph.png', 'rb')), content_type='image/png')

def __str__(self):
    return self.meeting_time



