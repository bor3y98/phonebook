from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Contact, ContactPhone


class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list.html'
    context_object_name = 'contacts'  # Name to access the list in the template


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact_detail.html'
    context_object_name = 'contact'  # Set the context variable name for the Contact object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the related ContactPhone objects to the context
        context['contact_phones'] = self.object.contact_phone.all()
        return context


class AddContactView(CreateView):
    model = Contact
    template_name = 'add_contact.html'
    fields = ['name', 'email', 'address']

    def form_valid(self, form):
        # Check if at least one phone number is provided
        phone_numbers = self.request.POST.getlist('phone_numbers')
        if not any(phone_numbers):
            form.add_error(None, 'At least one phone number is required.')
            return self.form_invalid(form)

        contact = form.save()
        for phone_number in phone_numbers:
            if not phone_number:
                form.add_error(None, 'Phone numbers can not be empty')
                return self.form_invalid(form)

            ContactPhone.objects.create(contact=contact, phone=phone_number)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contact_detail', kwargs={'pk': self.object.pk})
