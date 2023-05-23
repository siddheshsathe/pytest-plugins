from setuptools import setup

setup(
    name='pytest_sequence_markers',
    version='1.0.0',
    description="Testing plugin",
    author="Siddhesh Sathe",
    author_email="temp@gmail.com",
    license="MIT",
    py_modules=['pytest_sequence_markers'],
    requires=['pytest'],
    entry_points={"pytest11": ["pytest_sequence_markers=pytest_sequence_markers",]}
)