#!/bin/bash 

# Create main project files 
python3 -m venv .venv
touch config.py 
touch main.py 
touch requirements.txt 

# Data directory and files 
mkdir -p data/cleaned 
touch data/cleaned/cleaneddata.csv 
mkdir -p data/raw 
touch data/raw/rawdata.csv 
# Images directory 
mkdir -p images 
# Source directory structure 
mkdir -p src/components 
touch src/components/__init__.py 
touch src/components/component1.py 
touch src/components/component2.py 
touch src/components/footer.py 
touch src/components/header.py 
touch src/components/navbar.py 
# Pages directory and subdirectories 
mkdir -p src/pages 
touch src/pages/__init__.py 
touch src/pages/simple_page.py

mkdir -p src/pages/more_complex_page
touch src/pages/more_complex_page/__init__.py 
touch src/pages/more_complex_page/layout.py 
touch src/pages/more_complex_page/page_specific_component.py 
touch src/pages/home.py 
touch src/pages/about.py 
# Utils directory 
mkdir -p src/utils 
touch src/utils/__init__.py 
touch src/utils/common_functions.py 
touch src/utils/get_data.py 
touch src/utils/clean_data.py 
echo "Project structure created successfully."
