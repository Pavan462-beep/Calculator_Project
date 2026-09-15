pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Calculator project'
            }
        }

        stage('Install') {
            steps {
                bat '"C:\\Users\\M680499\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat '"C:\\Users\\M680499\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pytest test_calculator.py'
            }
        }

    }
}