from setuptools import setup, find_packages

setup(
    name="redis-clone-python",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'redis-clone=redis_clone_python.main:main',
        ],
    },
    description="A Redis-like server implemented in Python with CLI",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Himalaya Gupta",
    author_email="himalaya.gupta3@gmail.com",
    url="https://github.com/Himalayagup/redis-clone-python",
    license="MIT",
)
