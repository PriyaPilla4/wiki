from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import util
import markdown2
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):

    md_str = util.get_entry(title)
    if md_str is None:
        return HttpResponse("Requested page not found")

    
    block_body = markdown2.markdown(md_str)
    block_title = title
    html = block_body

    return HttpResponse(html)

def search(request):
    if request.method == 'POST':
        q = request.POST.get('q')

    md_str = util.get_entry(q)

    if md_str is None:
        substring = request.POST.get('q')
        entriesarray = []
        
        for entry in util.list_entries():
            fullstring = entry
            if substring.lower() in fullstring.lower():
                entriesarray.append(fullstring)

        return render(request, "encyclopedia/searchresults.html", {
            "entries": entriesarray 
        })

    
    block_body = markdown2.markdown(md_str)
    block_title = title
    html = block_body

    return HttpResponse(html)


def newpage(request):
    return render(request, "encyclopedia/newpage.html",{
        "error": " "
    })

def savepage(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

    content1 = content+"<br><br>Click [HERE](/wiki/edit/"+title+") to edit this page."
    
        
    
    for entry in util.list_entries():
        if entry == title:
            
            return render(request, "encyclopedia/newpage.html",{
                "error": "Error: Page with the same title already exists. Enter a new title."
            })
            

    util.save_entry(title, content1)

    md_str = util.get_entry(title)

    if md_str is None:
        return HttpResponse("Page not saved properly")
    else:
        
        full_str = md_str
        block_body = markdown2.markdown(full_str)
        block_title = title
        html = block_body
        return HttpResponse(html)
    

def edit(request, title):
    
    print(f"title: {title}")
     
    md_str = util.get_entry(title)
    block_body = markdown2.markdown(md_str)
    block_title = title
    html = block_body

    return render(request, "encyclopedia/edit.html", {
        "content": html,
        "title": title
    })

def save_edited_page(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
    
    util.save_entry(title, content)

    md_str = util.get_entry(title)

    if md_str is None:
        return HttpResponse("Page not saved properly")
    else:
        
        full_str = md_str
        block_body = markdown2.markdown(full_str)
        block_title = title
        html = block_body
        return HttpResponse(html)

def randompage(request):
    entries = util.list_entries()

    size = len(entries)
    x = random.randrange(1, size)
    
    md_str = util.get_entry(entries[x])

    block_body = markdown2.markdown(md_str)
    block_title = title
    html = block_body
    return HttpResponse(html)
