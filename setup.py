import setuptools

setuptools.setup(
    name="django-wsgi-view",
    version="0.0.1",
    url="https://github.com/ratson/django-wsgi-view",

    author="Ratson",
    author_email="contact@ratson.name",

    description="Embed WSGI application as Django view.",
    long_description=open('README.rst').read(),
    keywords=[],

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
