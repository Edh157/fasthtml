from fasthtml.common import *

#app,rt = fast_app(live=True)
# live reloading turned on

app = FastHTMLWithLiveReload()
rt = app.route

@rt('/')
def get(): return Title('My website'), Div(
    H1('Welcome visitor!'), 
    P("Do you know what?", hx_get="/change")
    )

@rt('/change')
def get(): return P('This page has been watched XXX times!')

serve() # wrapper around a uvicorn call -> type python filename.py to launch the webserver