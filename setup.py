import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="astro-virgo",
    version="3.8.2",
    author="Apostolos Spanakis-Misirlis",
    author_email="0xcoto@protonmail.com",
    description="A Versatile Spectrometer for Radio Astronomy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/0xCoto/Virgo",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['virgo=virgo.virgo:main']
    },
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy', 'matplotlib', 'astropy'],
    python_requires='>=2.7',
    include_package_data=True
)
