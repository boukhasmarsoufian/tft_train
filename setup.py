import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tftlibrary",
    version="0.0.1",
    author="Soufian",
    author_email="soufianboukhasmar@gmail.com",
    description="Temporal Fusion transformer multiple multivariate forecasting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/boukhasmarsoufian/tft_train",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)