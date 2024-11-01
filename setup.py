from setuptools import setup, find_packages

setup(
    name="AlloLLMEval",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "typing;python_version<'3.7'",
    ],
    extras_require={
        "dev": [
            "black",
            "flake8",
        ],
    },
    python_requires=">=3.6",
    author="AlloBrain",
    author_email="contact@allobrain.com",
    description="A framework for evaluating LLM outputs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/allobrain/allollmeval",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
