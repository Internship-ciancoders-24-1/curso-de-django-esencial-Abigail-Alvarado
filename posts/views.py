from django.http import HttpResponse
from datetime import datetime

posts = [
    {
        'name':'Mont Blanc',
        'user': 'Abigail ALvarado',
        'timestamp':   datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=1036',
    },
        {
        'name':'Via Lactea',
        'user': 'Vander',
        'timestamp':   datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=1036',
    },
        {
        'name':'Nuevo Auditorio',
        'user': 'Abigail ALvarado',
        'timestamp':   datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=1036',
    },

]

def list_post(request):
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i> {timestamp} </i> </small></p>  
            <figure><img src="{picture}"/></figure>         
    """.format(**post))

    return HttpResponse('<br>'.join(content) )