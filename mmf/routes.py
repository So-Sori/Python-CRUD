from flask import render_template,url_for,request,redirect,flash
from werkzeug.utils import secure_filename
import os
from mmf import app,db,bcrypt,login_manager
from mmf.models import Usuarios
from mmf.forms import Registro,Login,Cambiar,Plantilla_dos_tres,Plantilla_uno
# from mmf.config_session import session

from flask_login import login_user, current_user,logout_user,login_required

img = '/Users/Soribel/Desktop/Python Crud/mmf/img'
app.config["UPLOAD_FOLDER"] = img

@app.route('/home')
def home():
    return render_template('index.html',title = 'MMF')

# Formilarios, validacion ...
@app.route('/registro', methods = ['POST','GET'])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = Registro()
    if form.validate_on_submit():
        # hashed encripta la password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = Usuarios(nombre=form.nombre_user.data,email=form.email.data,password=hashed_password,imagen_perfil=url_for('static',filename='default.jpg'))

        db.session.add(user)
        db.session.commit()
        flash(f"Cuenta creada exitosamente para {form.nombre_user.data}!",'success')
        return redirect(url_for("login"))

    return render_template('registro.html',title = 'MMF Registro',form=form)

@app.route('/login',methods = ['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = Login()
    if form.validate_on_submit():
        user = Usuarios.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password,form.password.data):
            flash("Bienvenid@ De Nuevo Querida Estrella!!!")
            login_user(user,remember=form.rememberme.data)
            next_page = request.args.get('next')
            return redirect('next_page') if next_page else redirect(url_for('home'))
        else:
            flash("Hay un problema con el gmail o la contraseña", 'danger')

    return render_template('login.html',title = 'MMF Login',form=form)

@app.route('/uploader',methods = ['POST'])
def file():
    if request.method == 'POST':
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        return "<h1>Archivo subido exitosamente</h1>"

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account',methods=['GET','POST'])
@login_required
def account():
    """ Metodo que permite al usuario entrar a su peril (si esta registrado) permite actualizar el nombre del usuario mediante una consulta update"""
    form = Cambiar()
    if form.validate_on_submit:
        Users = Usuarios.query.all()
        data = None
        for user in Users:
            data = user.nombre
            if data == form.nombre_viejo:
                data.nombre = form.nuevo_nombre.data
                db.session.add(data)
                db.session.commit()
        return render_template('account.html',title= 'MMF Account',form=form)

@app.route('/famosos')
def famosos():
    return render_template('famosos.html',title='Famosos')

@app.route('/crear')
def crear():
    return render_template('crear.html',title='Famosos')

@app.route('/plantilla1')
def plantilla():
    form = Plantilla_uno
    return render_template('plantilla.html',title='Famosos',form=form)
@app.route('/plantillas')
def plantillas():
    form = Plantilla_dos_tres()
    return render_template('plantillas.html',title='Famosos',form=form)


@app.route('/forgot')
def forgot():
    return render_template('contra.html',title= 'La maco\'')