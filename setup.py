import setuptools

setuptools.setup(
    name="san",
    version="1.0.0",
    python_requires=">3.6",
    packages=setuptools.find_packages(),
    install_requires=[],
    setup_requires=["numpy", "cupy"],
    classifiers=["Programming Language :: Python :: 3.6",],
)
