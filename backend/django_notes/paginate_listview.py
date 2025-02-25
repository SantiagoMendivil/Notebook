"""Using a listview, in order to paginate the results you just need to 
    add the attribute of paginate_by. And in the html you have to call 
    the following attributes.
    
    <span class="step-links">
      {% if page_obj.has_previous %}
          <a href="?page=1">&laquo; first</a>
          <a href="?page={{ page_obj.previous_page_number }}">previous</a>
      {% endif %}

      <span class="current">
          Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
      </span>

      {% if page_obj.has_next %}
          <a href="?page={{ page_obj.next_page_number }}">next</a>
          <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
      {% endif %}
  </span> 
"""
from django.views.generic import ListView

class ListModel(ListView):
    paginate_by = 10
    # model = Model
    template_name = "template.html"
    context_object_name = "object_list"
    
    # Rest of the code 