"""Environment Setup for CMSC206: Data Analysis Project"""
# Author: Asmaa Abdul-Amin
# Date: 2021-07-25
# Requirements: pip, numpy, pandas, matplotlib, scikit-learn, tensorflow, keras, yfinance, PyPortfolioOpt
# Usage: python install_libraries.py
# Notes: This script will install the required libraries if they are not already installed.

import sys
import subprocess
import platform
import os
import shutil

# Required Python version
REQUIRED_PYTHON_MAJOR = 3
REQUIRED_PYTHON_MINOR = 8

# List of required libraries
REQUIRED_LIBRARIES = [
    "pandas",
    "numpy",
    "matplotlib",
    "yfinance",
    "PyPortfolioOpt",
    "jupyter"
]

VENV_DIR = "project-env"

def check_python_version():
    """
    Checks if Python is installed and if it meets the minimum version requirement.
    """
    current_version = sys.version_info
    version_str = f"{current_version.major}.{current_version.minor}.{current_version.micro}"
    
    print(f"🔍 Detected Python version: {version_str}")

    if (current_version.major, current_version.minor) < (REQUIRED_PYTHON_MAJOR, REQUIRED_PYTHON_MINOR):
        print(f"❌ Python {REQUIRED_PYTHON_MAJOR}.{REQUIRED_PYTHON_MINOR} or higher is required.")
        suggest_python_install()
        sys.exit(1)
    else:
        print(f"✅ Python version is sufficient (>= {REQUIRED_PYTHON_MAJOR}.{REQUIRED_PYTHON_MINOR}).")

def suggest_python_install():
    """
    Provides installation instructions or automates installation for Python >=3.8.
    """
    os_name = platform.system()

    print("\n⚠️ Python 3.8+ is required but not detected.")
    
    if os_name == "Linux":
        print("👉 Attempting to install Python 3.8+ on Linux...")

        try:
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", "software-properties-common"], check=True)
            subprocess.run(["sudo", "add-apt-repository", "-y", "ppa:deadsnakes/ppa"], check=True)
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", "python3.8", "python3.8-venv", "python3.8-distutils"], check=True)
            print("\n✅ Python 3.8+ installed. Run the script again using:")
            print("   python3.8 env_setup.py\n")
        except subprocess.CalledProcessError:
            print("❌ Failed to install Python 3.8+ automatically.")
            print("👉 Please install it manually: https://www.python.org/downloads/")
    
    elif os_name == "Darwin":  # macOS
        print("👉 Attempting to install Python 3.8+ on macOS with Homebrew...")

        if shutil.which("brew") is None:
            print("❌ Homebrew is not installed. Please install Homebrew first: https://brew.sh/")
        else:
            try:
                subprocess.run(["brew", "update"], check=True)
                subprocess.run(["brew", "install", "python@3.11"], check=True)
                print("\n✅ Python 3.11 installed. Run the script again using:")
                print("   python3.11 env_setup.py\n")
            except subprocess.CalledProcessError:
                print("❌ Failed to install Python 3.11 automatically.")
                print("👉 Please install it manually: https://www.python.org/downloads/")
    
    elif os_name == "Windows":
        print("👉 On Windows, please install Python 3.8+ manually:")
        print("   Download Python 3.8+ from https://www.python.org/downloads/windows/")
    
    else:
        print(f"❌ Unsupported OS: {os_name}")
        print("👉 Please install Python 3.8+ manually from https://www.python.org/downloads/")

def create_virtual_environment():
    """
    Creates a virtual environment in the project directory.
    """
    if os.path.exists(VENV_DIR):
        print(f"✅ Virtual environment '{VENV_DIR}' already exists.")
    else:
        print(f"⏳ Creating virtual environment '{VENV_DIR}'...")
        subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])
        print(f"✅ Virtual environment '{VENV_DIR}' created.")

def install_requirements():
    """
    Installs and verifies required libraries in the virtual environment.
    """
    if platform.system() == "Windows":
        pip_path = os.path.join(VENV_DIR, "Scripts", "pip")
    else:
        pip_path = os.path.join(VENV_DIR, "bin", "pip")

    print("⏳ Installing required libraries...")

    for lib in REQUIRED_LIBRARIES:
        subprocess.check_call([pip_path, "install", lib])
        print(f"✅ {lib} installed.")

def main():
    os_name = platform.system()
    print(f"🛠️  CMSC206 Environment Setup ({os_name} OS) 🛠️")
    
    # Step 1: Check Python version
    check_python_version()

    # Step 2: Create virtual environment
    create_virtual_environment()

    # Step 3: Install and verify required libraries in venv
    install_requirements()

    print("\n✅ Environment setup complete. Activate your virtual environment and start analyzing data! 🚀📊")
    if os_name == "Windows":
        print(f"   {VENV_DIR}\\Scripts\\activate")
    else:
        print(f"   source {VENV_DIR}/bin/activate")

    print("\n✅ Environment setup complete. You're ready to analyze data! 🚀📊\n")
    print("\nTo run the main script run: 'jupyter notebook' in the terminal, then select 'aerospace.ipynb' in the new Jupyter notebook interface.\n")

if __name__ == "__main__":
    main()