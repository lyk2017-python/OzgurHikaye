from django.shortcuts import render, get_object_or_404
from ozgur_modul.models import Storys, Contributions
from ozgur_modul.forms import StoryNewForm, ContribituonsNewForm

from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.


def story_list(request):
    storys = Storys.objects.all()
    return render(request, 'ozgur_modul/story_list.html', {'storys': storys})


def story_create(request):
    if request.method == 'POST':
        form = StoryNewForm(request.POST)
    else:
        form = StoryNewForm()
    return save_story_form(request, form, 'ozgur_modul/includes/partial_story_create.html')


def save_story_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            storys = Storys.objects.all()
            data['html_story_list'] = render_to_string('ozgur_modul/includes/partial_story_list.html', {
                'storys': storys
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def story_update(request, pk):
    pass


def story_delete(request, pk):
    pass


def story_like(request, pk):
    pass


def story_view(request, pk):
    data = dict()
    story = get_object_or_404(Storys, id=pk)
    context = {'story_contributions': story.contributions_set.all(), 'story':story}
    data['html_form'] = render_to_string('ozgur_modul/includes/partial_story_cont_view.html',context, request=request )
    return JsonResponse(data)


def cont_create(request, pk):
    if request.method == 'POST':
        form = ContribituonsNewForm(request.POST)
    else:
        form = ContribituonsNewForm()
    return save_cont_form(request, form, 'ozgur_modul/includes/partial_cont_create.html')


def save_cont_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            conts = Contributions.objects.all()
            data['html_story_list'] = render_to_string('ozgur_modul/includes/partial_story_list.html', {
                'conts': conts
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)