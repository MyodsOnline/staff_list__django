from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import auth, messages

from .models import Organization, Substation, Staff
from .forms import StaffForm, UserLoginForm, StaffUpdateForm, UserRegisterForm


class Staff_list(ListView):
    model = Staff
    fields = '__all__'


class Organization_list(ListView):
    model = Organization
    fields = '__all__'


class Substation_list(ListView):
    model = Substation
    fields = '__all__'


def get_staff(request):
    staff = Staff.objects.all().order_by('full_name')
    substations = Substation.objects.all().order_by('name')
    organizations = Organization.objects.all()
    context = {
        'staff': staff,
        'substations': substations,
        'organizations': organizations,
    }
    return render(request, 'staff_list/staff_list.html', context)


class SubstationDetailView(ListView):
    model = Staff
    template_name = 'staff_list/staff_detail.html'
    allow_empty = True

    def get_queryset(self):
        return Staff.objects.filter(job_id=self.kwargs['pk']).order_by('-is_active')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        substation = Substation.objects.get(pk=self.kwargs['pk'])
        substation_id = self.kwargs['pk']
        print(substation_id)
        context['title'] = substation
        return context


class SubststionUpdateView(UpdateView):
    model = Staff
    form_class = StaffUpdateForm
    success_url = reverse_lazy('staff_list')


class AddStaff(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = 'staff_list/add_staff.html'
    success_url = reverse_lazy('staff_list')

# class DeleteStaff(DeleteView):
#     model = Staff
#     success_url = reverse_lazy('staff_list')
#
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         success_url = self.get_success_url()
#         self.object.is_active = False
#         self.object.save()
#         return HttpResponseRedirect(success_url)


def deleteStaff(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.is_active = False
        staff.save()
        return HttpResponseRedirect(reverse_lazy('staff_list'))
    return render(request, 'staff_list/staff_confirm_delete.html', {'staff': staff})


def login(request):
    login_form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('staff_list'))
    context = {
        'login_form': login_form,
    }
    return render(request, 'staff_list/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('staff_list'))


def register(request):
    register_form = UserRegisterForm(data=request.POST)
    if request.method == 'POST':
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Вы успешно зарегестрировались')
            return HttpResponseRedirect(reverse('login'))
    else:
        register_form = UserRegisterForm()
    context = {
        'register_form': register_form,
    }
    return render(request, 'staff_list/register.html', context)
