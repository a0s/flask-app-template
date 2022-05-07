# flask-app-template

App template supported separated models (Flask-SQLAlchemy) and 
migrations (Flask-Migrate) 

## How to use

1. Clone the repo
2. Install requirement

    ```shell
    pip install -r requirement.txt
    ```
   
3. Init migrations dir

   ```shell
   flask db init
   ```

4. Generate first migration for User class (`app/models/user.py`) and apply it

   ```shell
   flask db migrate -m "Add User"
   flask db upgrade
   ```

5. Create new class `app/models/product.py`
   ```python
   from . import db
   
   class Product(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(128))
   ```
   
   Add into `app/models/__init__.py`
   ```python
   from .product import Product
   ```
   
   Then run `migrate` and `upgrade`
   
6. And so on..
