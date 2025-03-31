# CONTA SYSTEM


## Iniciar entorno virtual
```bash
python -m venv venv # crear entorno virtaul

# en linux
source venv/bin/activa

# en powershell
venv/Scripts/activate

# instalar dependencias
pip install -r requirements.txt
```

## Correr proyecto
Utiliza este comando para iniciar el servidor, cada cambio realizado se aplica al recargar la página.
```bash
python manage.py runserver
```


## Crear y aplicar migraciones
Este comando se utiliza para crear migraciones de los modelos creado con el **ORM** y son reflejado en la base de datos.

```bash
#app name indica en que aplicación se van a guardar las migraciones
python manage.py makemigration "app_name" # crear migraciones

python manage.py migrate # aplicar migraciones en la base de datos
```

