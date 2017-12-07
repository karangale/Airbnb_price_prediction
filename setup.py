import os
from setuptools import setup, find_packages
PACKAGES = find_packages()

# Get version and release info, which is all stored in shablona/version.py
ver_file = os.path.join('Airbnb-price-prediction', 'version.py')
with open(ver_file) as f:
    exec(f.read())

opts = dict(name='Airbnb Price Prediction',
            description='Predicting Airbnb prices based on the number of restaurants',
            long_description=LONG_DESCRIPTION,
            url=URL,
            download_url=DOWNLOAD_URL,
            license=open('LICENSE').read(),
            classifiers=CLASSIFIERS,
            author='scarlettdias, anirao26, karangale, rjtgupta',
            platforms=PLATFORMS,
            version=VERSION,
            packages=PACKAGES,
            package_data={'Airbnb-price-prediction': ['Data/*.*']},
            install_requires=REQUIRES,
            requires=REQUIRES)


if __name__ == '__main__':
    setup(**opts)
