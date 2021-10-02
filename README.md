# Data Processing for Nieves Observer

This repo contains the Jupyter Notebooks and Flask app that documents the ETL (extract-transform-load) process for the Nieves Observer application.

The app is continuously seeding new catalogues to the app depending on educators' and students' interests and requests.

## Data

### Deep Sky Objects (DSOs)

The app currently uses data from two catalogues:

1. Messier
1. Caldwell

The ETL process for each catalogue can be found in the `etl_<catalogue>.ipynb` files.

### Exoplanets

All exoplanet data are derived from NASA's exoplanet database, with observatory-specific constraints set to the extraction. E.g., objects must be bright than 12 mags, transit periods must not last longer than 8 hours, etc.

### Eclipsing Binaries

Coming soon.

## Development

Work on the files in a Python shell such as `pipenv`.

Clone the project

```
git clone git@github.com:weejerrick/nieves-observer-etl.git
cd nieves-observer-etl
```

Install all requisite libraries.

```
pipenv shell
pipenv install -r requirements.txt
```

Work on the ETL process with Jupyter Lab

```
jupyter lab
```

## Load

The `load` python files can actually be run inside a Jupyter Notebook. This will be updated in future improvements to the process.

For now, to load, first create a Postgres database (e.g., we give the database a name of nieves_observer)

```
createdb -U postgres nieves_observer
```

Update the database name in the `load` python files. For example in `load_dso.py`:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres@localhost/nieves_observer"
...
db_conn = psycopg2.connect(host="localhost", port="5432",
                           dbname="nieves_observer", user="postgres")
```

Once you're ready to load, run the load file.

```bash
python load_dso.py
```
