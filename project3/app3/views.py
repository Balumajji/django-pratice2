from django.http import HttpResponse

def showindex(request):
    message ='''
                <html>
                    <body bgcolor=pink>
                        <h1 style="color:yellow">
                             <font size="8">
                                 <u><b><i>Welcome to Django 10Am class</u></b></i>
                             </font>
                         </h1>
                    </body>
                </html>'''
    return HttpResponse(message)
    
