from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,PasswordField,BooleanField,SubmitField
# from flask_uploads import UploadSet, IMAGES
# from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms.validators import Length,Email,DataRequired,EqualTo,ValidationError
from mmf.models import Usuarios

class Registro(FlaskForm):
    nombre_user = StringField('Nombre',validators=[DataRequired(),Length(min=3,max=50)])
    email = EmailField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Contraseña',validators=[DataRequired()])
    comfir_password = PasswordField('Confirma Contraseña', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Registrar')
    
    def validate_nombre_user(self, nombre_user):
        user = Usuarios.query.filter_by(nombre=nombre_user.data).first()
        if user:
            raise ValidationError('Este nombre ya existe, Por favor elija uno diferente.')

    def validate_email(self, email):
        user = Usuarios.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Este email ya existe, Por favor elija uno diferente.')


class Login(FlaskForm):

    email = EmailField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Contraseña',validators=[DataRequired()])
    rememberme = BooleanField("Recuerdame")
    submit = SubmitField('Iniciar Sesion')

class Cambiar(FlaskForm):

    # images = UploadSet('images', IMAGES)

    # upload = FileField('image', validators=[
    #     FileRequired(),
    #     FileAllowed(images, 'Images only!')
    # ])
    nombre_viejo = StringField('Nombre Viejo',validators=[Length(min=3,max=50)])

    nuevo_nombre = StringField('Nuevo Nombre',validators=[Length(min=3,max=50)])

    submit = SubmitField('Guardar')


class Plantilla_uno(FlaskForm):

    crear_name = StringField('Nombre',validators=[Length(min=3,max=10000)])

    crear_datos = StringField('Agregar datos',validators=[Length(min=3,max=10000)])

    crear_parrafo = StringField('Agregar descripcion',validators=[Length(min=3,max=10000)])

    submit = SubmitField('Guardar')


class Plantilla_dos_tres(FlaskForm):

    crear_name = StringField('Nombre',validators=[Length(min=3,max=10000)])

    crear_datos = StringField('Agregar datos',validators=[Length(min=3,max=10000)])

    submit = SubmitField('Guardar')


