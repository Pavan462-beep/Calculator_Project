pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Calculator project'
            }
        }

        stage('Test') {
            steps {
                bat '"C:\\Users\\M680499\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pytest test_calculator.py'
            }
        }

    }
}