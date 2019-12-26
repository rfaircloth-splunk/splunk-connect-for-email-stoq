from setuptools import setup, find_packages

setup(
    name="splunk",
    version="2.0.0",
    author="Ryan Faircloth (@rfaircloth)",
    url="https://github.com/splunk/splunk-connect-for-email",
    license="Apache License 2.0",
    description="Save results to Splunk using HTTP Event Collector",
    packages=find_packages(),
    include_package_data=True,
)