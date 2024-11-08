# INSTALACION
---
## Entorno local
### Requisitos
- Python version 3.12.x: https://www.python.org/downloads/release/
- PostgreSQL: Crear el usuario odoo con permiso para login y crear base de datos
### PASOS EJECUTAR ODOO
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

## Entorno dockerizado
## Inicialización del proyecto (Primera vez)

1. Clona el repositorio de Git:
   ```
   git clone https://github.com/DAVV422/odoo-sw1.git
   ```

2. Cambia al branch `sw1-agenda`:
   ```
   cd odoo-sw1
   git checkout sw1-agenda
   ```

3. Copia el archivo de configuración de ejemplo:
   ```
   cp odoo-example.conf odoo.conf
   ```

4. Edita el archivo `odoo.conf` y configura la ruta de los módulos en la variable `addons_path`. También debes ingresar la contraseña del usuario de PostgreSQL "odoo".

5. Construye las imágenes de Docker:
   ```
   docker-compose build --no-cache
   ```

6. Levanta los servicios de Docker:
   ```
   docker-compose up -d
   ```

7. Verifica los logs para asegurarte que todo haya iniciado correctamente:
   ```
   docker-compose logs -f
   ```

8. Accede a la interfaz web de Odoo en http://localhost:8069 y crea una nueva base de datos.

## Ejecución recurrente del proyecto

1. Asegúrate de estar en la rama `sw1-agenda`:
   ```
   git checkout sw1-agenda
   ```

2. Reconstruye las imágenes de Docker (solo si has realizado cambios en el código o la configuración):
   ```
   docker-compose build --no-cache
   ```

3. Levanta los servicios de Docker:
   ```
   docker-compose up -d
   ```

4. Verifica los logs para asegurarte que todo haya iniciado correctamente:
   ```
   docker-compose logs -f
   ```

5. Accede a la interfaz web de Odoo en http://localhost:8069.