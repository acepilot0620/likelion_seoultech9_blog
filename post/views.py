from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.
post_list = ListView.as_view(model=Post,paginate_by=10)

post_detail = DetailView.as_view(model=Post,pk_url_kwarg = 'id')
