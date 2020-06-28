import os

# __file__ refers to the file settings.py 
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')
 

APP_TEMPLATE = os.path.join(APP_ROOT, '..\\templates')

APP_CODE = os.path.join(APP_ROOT, '..\\code')

APP_UPLOADS = os.path.join(APP_ROOT, 'static\\uploads')




