import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gym_deepmindlab",
    version="0.1.2",
    author="Jonáš Kulhánek",
    author_email="jonas.kulhanek@live.com",
    description="Gym interface to deepmind_lab environment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jkulhanek/gym-deepmindlab-env",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
