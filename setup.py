"""A setup for the Airbnb price prediction project."""

from setuptools import setup, find_packages
PACKAGES = find_packages()

opts = dict(name='Airbnb Price Prediction',
            description='Predicting Airbnb prices from the number of '
            'restaurants',
            long_description='Analyze the effect of restaurants and eateries '
            'on Airbnb listings in New York city',
            url='https://github.com/UWSEDS-aut17/uwseds-group-team-star',
            license=open('LICENSE').read(),
            classifiers=CLASSIFIERS,
            author='scarlettdias, karangale, anirao26, rjtgupta',
            version='0.1.0',
            packages=PACKAGES,
            package_data={'Airbnb-price-prediction': ['Data/*.*']},
            install_requires=REQUIRES,
            requires=REQUIRES)


if __name__ == '__main__':
    setup(**opts)
