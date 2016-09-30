from setuptools import setup


setup(
    name='juno-bork',
    version='1.0',
    url='https://github.com/jeremy-cx/juno-bork/',
    license='MIT',
    author='Jeremy',
    author_email='jeremy@jeremy.cx',
    oescription='Get new releases from juno. Stream in Itunes',
    py_modules=['junobork'],
    platforms='any',
    install_requires=[
        'beautifulsoup4==4.3.2',
        'click==3.3',
        'requests==2.5.1',
    ],
    entry_points='''
        [console_scripts]
		junobork=junobork:main
    '''
)