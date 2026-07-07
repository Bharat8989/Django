from django.shortcuts import render
from datetime import datetime

# Create your views here.

class User:
  
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
def home(request):
    context = {
        'name': 'mohit kumar',
        'age': 24,
        'skills': ['python', 'django', 'react'],
        'user': User('kumar', 30),
        'blog': { 
            'title': 'Django template intro',
            'author': {
                'name': 'mohit kumar',
            },
            'content': '<b>This is Bold </b>',
            # 2. Fixed datetime syntax and 3. added the missing comma
            'create_at': datetime.now()
        },
        'empty_value': None,
    }
    # 4. Cleaned up the trailing query text from the return statement
    return render(request, 'blog/home.html', context)
