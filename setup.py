from setuptools import setup, find_packages

requires = [
    "selenium",
]

setup(
    name="selenium_qa_sandbox",
    version="0.0",
    description="selenium sandbox",
    long_description="",
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP functional/integration tests",
    ],
    author="",
    author_email="",
    url="",
    keywords="test tests",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite="",
    install_requires=requires,
    extras_require = {},
    entry_points="",
)
