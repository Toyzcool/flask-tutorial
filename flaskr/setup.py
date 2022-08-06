from setuptools import find_packages, setup
# https://dormousehole.readthedocs.io/en/latest/tutorial/install.html

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_required=[
        'flask',
    ],
)
