from setuptools import setup, find_packages

NAME = "neo-api-client"
VERSION = "1.2.0"

# Updated requirements for Python 3.13 compatibility
REQUIRES = [
    'bidict>=0.23.1',
    'certifi>=2024.2.2',
    'idna>=3.7',
    'numpy>=1.26.4',
    'pyjsparser>=2.7.1',
    'PyJWT>=2.8.0',
    'python-dateutil>=2.9.0',
    'python-dotenv>=1.0.1',
    'requests>=2.31.0',
    'six>=1.16.0',
    'urllib3>=2.2.1',
    'websocket-client>=1.7.0',
    'websockets>=12.0',
    'pandas>=2.2.1'
    # Note: asyncio removed - it's built into Python 3.13
]

setup(
    name=NAME,
    version=VERSION,
    description="Neo Trade API - Python 3.13 Compatible",
    author="Neo API",
    author_email="",
    url="https://github.com/Kotak-Neo/kotak-neo-api",
    keywords=["Neo-Trade API", "Neo Trade API's", "Kotak Securities", "Trading API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    python_requires='>=3.10,<4.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    long_description="""
    Kotak Neo Trade API Client
    
    A Python client library for Kotak Securities Neo Trade API.
    Compatible with Python 3.10, 3.11, 3.12, and 3.13.
    
    Features:
    - Complete trading API implementation
    - WebSocket support for real-time data
    - Order management (place, modify, cancel)
    - Portfolio and position tracking
    - Market data and quotes
    - Scrip search functionality
    
    For detailed documentation, visit:
    https://github.com/Kotak-Neo/kotak-neo-api
    """,
    long_description_content_type="text/markdown",
)
