from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, TemplateView

from orders.models import Order
from .forms import EditProfileForm, UserRegistrationForm, UserCreationForm, ProfileForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.models import User
from .models import Profile

""" 
Defines a set of views for handling user authentication, profile management, and other related functionalities.
"""


class HomeView(View):
    """
    Displays the home page.
    """
    template_name = 'home/home.html'

    def get(self, request):
        return render(request, self.template_name)


class UserLoginView(LoginView):
    """
    Handles user login.
    """
    template_name = 'profile/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')

    def form_valid(self, form):
        """
        Add a success message after successful login.
        """
        response = super().form_valid(form)
        if self.request.user.profile.phone_number and self.request.user.profile.full_name:
            messages.success(self.request, 'You have logged in successfully.', extra_tags='success')
        else:
            messages.error(self.request,
                           'You have not registered your phone number and full name yet. Please complete your profile.',
                           extra_tags='error')
            return redirect('creat_profile')
        return response

    def dispatch(self, request, *args, **kwargs):
        """
        Redirects authenticated users to the home page with a success message.
        """
        if request.user.is_authenticated:
            messages.success(
                request, 'You have already login successfully', extra_tags='success'
            )
            return redirect('home')

        else:
            return super().dispatch(request, *args, **kwargs)


class UserLogoutView(LoginRequiredMixin, View):
    """
    Handles user logout.
    """
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        """
        Redirects non-authenticated users to the home page with a success message.
        """
        if not request.user.is_authenticated:
            messages.success(
                request,
                'You have already logged out successfully',
                extra_tags='success',
            )
            return redirect('home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Logs out the user and redirects to the home page with a success message.
        """
        if request.user.profile.phone_number and request.user.profile.full_name:
            logout(self.request)
            messages.success(request, 'Logout successfully', extra_tags='success')
            return redirect('home')
        else:
            messages.error(request,
                           'You have not registered your phone number and full name yet must be seat after logout',
                           extra_tags='error')
            return redirect('creat_profile')


class EditeUserView(LoginRequiredMixin, View):
    """
    Handles user profile editing.
    """
    form_class = EditProfileForm

    def get(self, request):
        """
        Renders the form for editing the user profile.
        """
        form = self.form_class(
            instance=request.user.profile, initial={'email': request.user.email}
        )
        return render(request, 'profile/change_profile.html', {'form': form})

    def post(self, request):
        """
        Processes the form submission for editing the user profile.
        """
        form = self.form_class(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            request.user.email = form.cleaned_data.get('email')
            request.user.save()
            messages.success(
                request,
                'Your profile has been updated successfully',
                extra_tags='success',
            )
            return redirect('home')
        else:
            messages.error(
                request,
                'Your profile has not been updated successfully',
                extra_tags='error',
            )
            return redirect('edit_user')


class CreateUserView(View):
    """
    Handles user registration.
    """
    form_class = UserRegistrationForm
    template_name = 'profile/create_user.html'

    def get(self, request):
        """
        Renders the registration form.
        """
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """
        Processes the form submission for user registration.
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            new_user = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name,
                                                last_name=last_name)
            messages.success(
                request, f'Account created for {username}', extra_tags='success'
            )
            Order.objects.create(user=new_user)
            return redirect('login')
        else:
            return render(request, self.template_name, {'form': form})


class CreateProfileView(View):
    """
    Handles user profile creation.
    """
    template_name = 'profile/create_profile.html'

    def get(self, request):
        """
        Renders the form for creating a user profile.
        """
        form = ProfileForm(instance=request.user.profile)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """
        Processes the form submission for creating a user profile.
        """
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(
                request,
                f'Profile created for phone: {request.user.profile.phone_number} and '
                f'full name: {request.user.profile.full_name}',
                extra_tags='success'
            )
            return redirect('home')
        return render(request, self.template_name, {'form': form})


class ChangePasswordView(PasswordChangeView):
    """
    Handles changing user password.
    """
    form_class = UserCreationForm
    template_name = 'profile/change_password.html'
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
        """
        Adds the current user to the form's keyword arguments.
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class RegisterView(View):
    """
    Handles user registration.
    """
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'

    def get(self, request):
        """
        Renders the registration form.
        """
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """
        Processes the form submission for user registration.
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('registration_success')
        return render(request, self.template_name, {'form': form})


class ProfileDetailView(LoginRequiredMixin, DetailView):
    """
    Displays user profile details.
    """
    model = Profile
    template_name = 'profile/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        """
        Retrieves the profile object for the currently logged-in user.
        """
        profile_get_object = Profile.objects.get(user=self.request.user)
        return get_object_or_404(User, pk=self.kwargs['pk']) and profile_get_object


