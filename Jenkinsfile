pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies'
                sh 'python3 -m venv .venv'
                sh '.venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests'
                sh '.venv/bin/python -m unittest discover -s . -p "test_*.py"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Flask application'
                sh 'mkdir -p deployment'
                sh 'cp app.py requirements.txt deployment/'
                sh 'ls -l deployment/'
            }
        }
    }
}
