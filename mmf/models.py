from mmf import db,login_manager
from flask_login import UserMixin

#Login buscando por id
@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))

class Usuarios(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key  = True)
    nombre = db.Column(db.String(50),nullable = False,unique = True)
    email = db.Column(db.String(120),unique = True,nullable = False)
    password = db.Column(db.String(20),nullable = False)
    imagen_perfil = db.Column(db.String(20),nullable = False, default = 'default.jpg')
    posts = db.relationship('Post',backref = 'nombre', lazy = True)
    # redes = db.relationship('Redes',backref = 'nombre', lazy = True)

    def __repr__(self):
        return f' User ({self.user_name},{self.email},{self.image_file})'

class Post(db.Model):
    id = db.Column(db.Integer,primary_key  = True)
    p1 = db.Column(db.Text,nullable = False)
    p2 = db.Column(db.Text,nullable = False)
    p3 = db.Column(db.Text,nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable = False)

    def __repr__(self):
        return f' Post ({self.title},{self.date_post})'

# class Redes(db.Model):
#     id = db.Column(db.Integer,primary_key  = True)
#     insta = db.Column(db.String(200) ,default = '#')
#     face = db.Column(db.String(200) ,default = '#')
#     link = db.Column(db.String(200) ,default = '#')
#     github = db.Column(db.String(200) ,default = '#')
#     otro = db.Column(db.String(200) ,default = '#')
#     user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable = False)

