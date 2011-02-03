import os

DOCUMENTATION_ROOT = os.path.join(os.path.dirname(__file__), '../../doc/')

def view(request, path):
    if path == '':
        path = 'index'
    
    if path.endswith('/'):
        path = path[:-1]
        
    print path
    
    fh = open(os.path.join(DOCUMENTATION_ROOT, path))
    data = fh.read()
    fh.close()

    return data.decode('utf-8')
