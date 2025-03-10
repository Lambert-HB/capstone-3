# Capstone project - Old-school personal blog

## Description
This project is a website that allows users to create user profiles that allow them to create a user profile,
log in to the website, view a list of posts ordered by creation date and create a post that is viewable by others.

## Installation
1. Clone the repository:
    
    git clone [repository URL]
    
2. Navigate to the project directory:
    
    cd [repository directory]
    
3. Create a virtual environment:
    
    python -m venv env
    
4. Activate the virtual environment:
    - For Windows:
    
    .\env\Scripts\activate
    
    - For macOS/Linux:
    
    source env/bin/activate
    
5. Install the required dependencies:
    
    pip install -r requirements.txt
    

## Usage
1. Apply the migrations:
    
    python manage.py migrate
    
2. Start the development server:
    
    python manage.py runserver
    
3. Open your web browser and navigate to `http://127.0.0.1:8000`.

## Features
- Register for a user account
- View posts by yourself and other users 
- Make posts to be viewed by yourself and other users
- View a lis of all posts by all users ordered by date of creation 

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a Pull Request.

## License
[This project is licensed under the MIT License - see the LICENSE file for details.]

## Acknowledgements
- [Credit or references to helpful resources.]
