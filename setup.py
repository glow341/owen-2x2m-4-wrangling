import setuptools

setuptools.setup(
    name = "cars",
    version = "0.0.1",
    author = "Owen",
    autor_email = "owenalbertoliem@gmail.com",
    url = "",
    packages = setuptools.find_packages(),
    classifier = ["Programming Language :: Python :: 3"],
    install_requires = [
        "pandas == 1.1.4"],
    python_requires = ">=3.7"
)