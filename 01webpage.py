from fasthtml.common import *

app,rt = fast_app()

@rt('/')
def get(): return Title('Welcome to my website'), Div(
    H1('Hello everyone!'), 
    P("Can you guess my feeling?", hx_get="/change")
    )

@rt('/change')
def get(): return P('I am so happy to be here!')

serve()