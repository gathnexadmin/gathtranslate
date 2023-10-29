from setuptools import setup

setup(
    name='Google Translater',  # Replace 'myproject' with your project name
    version='1.0.0',   # Specify the version of your project

    # Project description
    description='Free google translater',

    # Author information
    author='Gokul Raja',
    author_email='gathnexorg@gmail.com',

    # Project URL
    url='https://github.com/gathnexadmin/gathtranslate.git',

    # Packages to be included in the distribution
    packages=['gathtranslater'],

    install_requires=[
        "openai"
    ],

    # Other metadata such as license, classifiers, etc.
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
