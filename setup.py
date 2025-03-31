from setuptools import setup, find_packages

setup(
    name="fieldnotes-lm",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9,<3.10",
    install_requires=[
        "streamlit==1.32.0",
        "watchdog==3.0.0",
        "pydantic==2.6.3",
        "loguru==0.7.2",
        "langchain==0.1.9",
        "humanize==4.11.0",
        "streamlit-tags==1.2.8",
        "tiktoken==0.6.0",
        "pymupdf==1.24.0",
        "python-magic==0.4.27",
        "langdetect==1.0.9",
        "google-generativeai==0.3.2",
        "langchain-google-genai==0.0.11",
        "python-dotenv==1.0.1",
    ],
)