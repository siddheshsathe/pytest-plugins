from setuptools import setup

setup(
    name='pytest_sequence_markers',
    version='0.0.1',
    description="Testing plugin",
    author="Siddhesh Sathe",
    author_email="siddheshsathe@rediffmail.com",
    license="GNU",
    py_modules=['pytest_sequence_markers'],
    requires=['pytest'],
    entry_points={"pytest11": ["pytest_sequence_markers=pytest_sequence_markers",]}
)
