from setuptools import find_packages, setup
from os.path import join, dirname

setup(
    name='common_instances',
    version='1.0',
    packages=find_packages(include=['common_instances']),
    include_package_data=True,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    test_suite='common_instances.tests',
    author='Serhii Sokhatskyi',
    author_email='sokhatsky.98@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        "Operating System :: OS Independent"
    ],
    keywords="education python django",
    project_urls={
        "Homepage": "https://git.foxminded.ua/foxstudent103969/common_instances",
        "Bug Tracker": "https://git.foxminded.ua/foxstudent103969/common_instances/-/issues"
    },
    python_requires='>=3.8'
)
