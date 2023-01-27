import web
from datetime import datetime


urls = (
    '/', 'CookieSet'
    )

render = web.template.render('templates',base='layout')
app = web.application(urls, globals())


class CookieSet:
    def GET(self):
        try:
            cookie = web.cookies()
            
            user = "Jesus"
            
            fetch = datetime.today().strftime('%Y-%m-%d')
            hora = datetime.today().strftime('%H:%M')


            web.setcookie('usuario',user, expires="",domain=None)
            web.setcookie('fechaVisita',fetch, expires="",domain=None)
            web.setcookie('horaVisita',hora, expires="",domain=None)
        
            if cookie.get("visitas"):
                visitas = int(cookie.get("visitas"))
                visitas +=1
                web.setcookie("visitas", str(visitas), expires="",domain=None)
                return "visitas "+str(visitas)
            else:
                web.setcookie("visitas", str(1), expires="", domain=None)
                return "Visitas " + "1"
        except Exception as e:
            return "Error" + str(e.args)
    

if __name__ == "__main__":
    #web.config.debug = False
    app.run()
    

"""
         # No. de visitas, nombre de usuario (si lo pasa por url) si no guarda el nombre "anónimo", fecha de la visita, hora de la visita.
        web.setcookie('No.visitas', 0, 3600)
        user = "Jesus"
        fetch = datetime.today().strftime('%Y-%m-%d')
        hora = datetime.today().strftime('%H:%M')


        web.setcookie('usuario',user, 3600)
        web.setcookie('fechaVisita',fetch, 3600)
        web.setcookie('horaVisita',hora, 3600)
        
        return "Your age is: " + web.cookies().age + "fecha: "+ web.cookies().fechaVisita + " hora "+web.cookies().horaVisita
"""