# flask-app-template

Flask app template with migrations and autoloader.
Based on Flask-SQLAlchemy and Flask-Migrate. 

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

   Then run `migrate`, `upgrade` and commit changes.
