import web
from datetime import datetime


urls = (
    '/(.*)', 'CookieSet'
    )

render = web.template.render('templates',base='layout')
app = web.application(urls, globals())


class CookieSet:
    def GET(self, user):
        try:
            cookie = web.cookies()
            visitas = "0"
            print(cookie)
            
            fetch = datetime.today().strftime('%Y-%m-%d')
            hora = datetime.today().strftime('%H:%M')
            web.setcookie('userr',user, expires="",domain=None)
            web.setcookie('fechaVisita',fetch, expires="",domain=None)
            web.setcookie('horaVisita',hora, expires="",domain=None)
            
            if user:
                web.setcookie("nombre",user,expires="",domain=None)
            else:
                user = "Anonimo"
                web.setcookie("nombre",user,expires="",domain=None)                

            if cookie.get("visitas"):
                visitas = int(cookie.get("visitas"))
                visitas +=1
                web.setcookie("visitas", str(visitas), expires="",domain=None)

            else:
                web.setcookie("visitas", str(1), expires="", domain=None)
                visitas = "1"
                
            return "Visitas: " + str(visitas) + " Nombre: " + user + " Hora: " + hora + " Fecha: " + fetch
                            
        except Exception as e:
            return "Error" + str(e.args)
        
        
    

if __name__ == "__main__":
    #web.config.debug = False
    app.run()
