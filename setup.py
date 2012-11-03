import setuptools


setuptools.setup(
    name='myapp',
    version='0.1',
    url='<URL TO YOUR PROJECT HERE>',
    license='<YOUR LICENSE>',
    author='<YOUR NAME>',
    author_email='<YOUR EMAIL>',
    description='Skeleton project for a Flask app deployed to Heroku using'
                ' Twitter Bootstrap',
    long_description=__doc__,
    packages=setuptools.find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
