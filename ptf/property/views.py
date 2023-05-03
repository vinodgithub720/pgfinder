# from django.shortcuts import render
# from django.views.generic import CreateView
# from .forms import *
# from django.views.generic import ListView,DetailView
# from django.views.generic import DeleteView,UpdateView
# from .models import *

# # Create your views here.

# class PropertyCreateView(CreateView):
#     form_class =AddpropertyForm
#     model = Property_info
#     template_name = 'property/addproperty.html'
#     success_url = '/property1/property_list/'

#     def form_valid(self, form):
#         return super().form_valid(form)

# class PropertyUpdateView(UpdateView):
#     model = Properties
#     form_class = AddpropertyForm
#     template_name = 'property/addproperty.html'
#     success_url = '/'


# class PropertyDeleteView(DeleteView):
#     model = Properties
#     def get(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)
    
#     success_url = '/'   

# class PropertyDetailView(DetailView):
#     model = Properties
#     template_name = 'property/property_detail.html'
#     context_object_name = 'property_detail'
    
#     def get(self, request, *args, **kwargs):
#         team = Properties.objects.filter(Project_id=self.kwargs['pk'])
#         return render(request, self.template_name, {'property_detail': self.get_object(),'team':team})
    

# class PropertyListView(ListView):
#     model = Properties

#     template_name = 'property/project_list.html'
#     context_object_name = 'property_list'
    
#     def get_queryset(self):
#         return super().get_queryset()    

# class Create_Project_team(CreateView):
#     form_class =AddpropertyForm
#     template_name = 'project/project_team_create.html'
#     success_url = '/project/list_project/'

# class ProjectTeamListView(ListView):
#     model = Property_info
#     template_name = 'property/project_list.html'
#     context_object_name = 'project_team_list'
    
# class ProjectTeamByProject(ListView):
#     model = Property_info
#     template_name = 'property/property_list.html'
#     context_object_name = 'project_team_list'
    
#     def get_queryset(self):
#         return super().get_queryset().filter(Property_info_id=self.kwargs['pk'])    

from django.shortcuts import render
from django.views.generic import CreateView
from .forms import *
from django.views.generic import ListView,DetailView
from django.views.generic import DeleteView,UpdateView
from .models import *


# Create your views here.


class ProjectCreationView(CreateView,):
    form_class =ProjectCreationForm
    model = Property_info
    # context_object_name = 'create_project'
    template_name = 'project/project_create.html'
    success_url = '/property/list_project/'
    
    
    def form_valid(self, form):
        return super().form_valid(form)

class AddpropertyView(CreateView):
    form_class =AddpropertyForm
    model = Property_info
    template_name = 'project/Add_property.html'
    success_url = '/property/list_project/'
    
     
    def form_valid(self, form):
        return super().form_valid(form)



class ProjectListView(ListView):
    model = Property_info
    template_name = 'project/project_list.html'
    context_object_name = 'project_list'
    
    def get_queryset(self):
        return super().get_queryset()    

class ProjectList1View(ListView):
    model = Property_info
    template_name = 'project/buyproperty.html/'
    context_object_name = 'project_list1'
    
    def get_queryset(self):
        return super().get_queryset()   

class PropertyListView(ListView):
    model = Property_info
    template_name = 'project/list_property.html'
    context_object_name = 'property_list'
    
    def get_queryset(self):
        return super().get_queryset()       

class ProjectUpdateView(UpdateView):
    model = Property_info
    form_class = ProjectCreationForm
    template_name = 'project/project_create.html'
    success_url = '/property/list_project/'
    
# class ProjectDetailView(ListView):
#     model = Property_info
#     template_name = 'project/project_detail.html'
#     context_object_name = 'project_detail'
    
    # def get(self, request, *args, **kwargs):
    #     team = Property_info.objects.filter(property_id=self.kwargs['pk'])
    #     return render(request, self.template_name, {'project_detail': self.get_property(),'team':team})

class ProjectDetailView(DetailView):
    model = Property_info
    template_name = 'project/projectdetail.html'
    context_object_name = 'project_details' 
    
    def get(self, request, *args, **kwargs):
        team = ProjectTeam.objects.filter(Project_id=self.kwargs['pk'])

        return render(request, self.template_name, {'project_details': self.get_object(),'team':team}) 

     
class ProjectDeleteView(DeleteView):
    model = Property_info
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/property/list_project/'    
    
class Create_Project_team(CreateView):
    form_class =ProjectTeamCreationForm
    template_name = 'project/project_team_create.html'
    success_url = '/property/list_project/'

class ProjectTeamListView(ListView):
    model = ProjectTeam
    template_name = 'project/project_team_list.html'
    context_object_name = 'project_team_list'
    
class ProjectTeamByProject(ListView):
    model = ProjectTeam
    template_name = 'project/project_team_list.html'
    context_object_name = 'project_team_list'
    
    def get_queryset(self):
        return super().get_queryset().filter(id=self.kwargs['pk'])    

