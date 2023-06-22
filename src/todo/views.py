from django.utils.html import escape
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from todo.models import Collection, Taches
from django.utils.text import slugify
from django.template.loader import render_to_string


# Create your views here.


def index(request):
    context = {}

    collection_slug = request.GET.get('collection')
    collection = Collection.get_default_collection()

    if collection_slug:
        collection = get_object_or_404(Collection, slug=collection_slug)
    
    context["collections"] = Collection.objects.order_by('slug')
    taches = collection.taches_set.order_by('description')
    context["taches"] = render_to_string('todo/taches.html', context={'taches':taches}) 
    
    return render(request, 'todo/index.html', context=context)



def add_collections(request):
    collection_name = escape(request.POST.get("collection-name"))
    collection, created = Collection.objects.get_or_create(nom=collection_name, slug=slugify(collection_name))
    if not created:
        return HttpResponse("La collection existe déjà",) #status=409)
    
    return redirect(f'<h2>{collection_name}</h2>')



def add_taches(request):
    collection = Collection.get_default_collection()
    description = escape(request.POST.get('taches-description'))

    Taches.objects.create(description=description, collection=collection)
    
    return HttpResponse(description)


def get_taches(request, collection_pk):
    
    collection = get_object_or_404(Collection, pk=collection_pk)
    taches = collection.taches_set.order_by('description')
    
    #return HttpResponse("<br>".join(tache.description for tache in taches))
    return render(request, 'todo/taches.html', context={"taches":taches})
