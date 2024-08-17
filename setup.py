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
    python_requires='>=3.6',  # Minimum Python version required
    install_requires=[
        # List of project dependencies
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
