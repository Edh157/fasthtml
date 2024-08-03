from fasthtml.common import *

# app = FastHTMLWithLiveReload()
# rt = app.route

app,rt = fast_app(live=True)
# fast_app() is a utility function that provides useful defaults
# live reloading turned on

@rt('/')
def get(): return Title('My website'), Titled(
    "Welcome visitor!", 
    P("Do you know what?", hx_get="/change")
    )

text = """
Hegel fait quelque part cette remarque que tous les grands événements \
et personnages historiques se répètent pour ainsi dire deux fois. \
Il a oublié d'ajouter : la première fois comme tragédie, la seconde fois comme farce. \
Caussidière pour Danton, Louis Blanc pour Robespierre, la Montagne de 1848 à 1851 \
pour la Montagne de 1793 à 1795, le neveu pour l'oncle. Et nous constatons la même \
caricature dans les circonstances où parut la deuxième édition du 18 Brumaire."""

@rt('/change')
def get(): return P(text)

serve() # wrapper around a uvicorn call -> type python filename.py to launch the webserver