import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarization-Project"
AUTHOR_USER_NAME = "nethmii98"
SRC_REPO = "textSummarization"
AUTHOR_EMAIL = "nethminagodawithane777@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    description="A project to summarize text using NLP app.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    url="https://github.com/" + AUTHOR_USER_NAME + "/" + REPO_NAME,
    project_urls={"Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"}
)