import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='snowflake',
    version='0.0.3',
    author='Arnold Abraham',
    author_email='arnoldabraham0@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/arnoldabraham0/Project_hw5',
    license='MIT',
    packages=['snowflake'],
    install_requires=['requests'],
)