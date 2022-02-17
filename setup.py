import setuptools

setuptools.setup(
    name="lab_3",
    version='0.0.1',
    packages=setuptools.find_packages(exclude=['*_notebooks', 'qa', '*-dev.sh']),
    install_requires=[
        'opencv-python',
        'Pillow',
        'tensorflow==2.4.1',
        'pycocotools==2.0.1',
    ],
)
