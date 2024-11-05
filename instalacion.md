# INSTALACION
## Requisitos
- Python version 3.9.13
- PostgreSQL: Crear el usuario odoo con permiso para login y crear base de datos
## PASOS EJECUTAR ODOO
1. Clonar el repositorio: https://github.com/DAVV422/odoo-sw1.git
2. Cambiar a la branch: sw1-agenda
3. Copiar el archivo `odoo-example.conf` y nombrarlo: `odoo.conf`
4. Colocar la ruta de los modulos en `odoo.conf` en la variable `addons_path` y colocar la contraseña del usuario de postgres odoo
5. Crear un entorno virtual de python: 
```bash
python -m venv bin
```
6. Activar el entorno virtual: 
```bash
.venv/Scripts/activate
```
7. Instalar los paquetes: 
```bash
pip install -r requirements.txt
```
8. Iniciar Odoo con el comando: 
```bash
python odoo-bin --conf=odoo.conf
```
NOTA: Si es la primera vez que se iniciará odoo usar el comando: 
```bash
python odoo-bin -i base --conf=odoo.conf
```