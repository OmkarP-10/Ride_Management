from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="ride_management",
    version="0.0.1",  # Replace with the actual version if available
    description="Ride Management System",
    author="Omkar P",
    author_email="omkarpangerkar10@gmail.com",  # Replace with the actual email
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
