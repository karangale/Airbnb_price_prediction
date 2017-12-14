"""A setup for the Airbnb price prediction project."""

from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

opts = dict(name='airbnb_price_prediction',
            description='Predicting Airbnb prices from the number of '
            'restaurants',
            long_description=long_description,
            url='https://github.com/UWSEDS-aut17/uwseds-group-team-star',
            license=open('LICENSE').read(),
            author='scarlettdias, karangale, anirao26, rjtgupta',
            version='0.1.0',
            packages=['airbnb_price_prediction'],
            package_data={'Airbnb-price-prediction': ['Data/*.*']},
            install_requires=['flask', 'numpy', 'math', 'os', 'pandas',
                              'sklearn', 'scipy', 'matplotlib', 'geopy'])


if __name__ == '__main__':
    setup(**opts)
