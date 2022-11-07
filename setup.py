from setuptools import setup, find_packages

setup(
    name='FlaskCRUD',
    version='1.0.0',
    packages=find_packages(include=['flaskr', 'flaskr.*']),
    install_requires=[
        'flask',
        'psycopg2',
        'python-dotenv'
    ]
)