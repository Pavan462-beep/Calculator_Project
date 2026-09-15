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

        stage('Create Artifact') {
            steps {
                bat 'powershell -Command "Compress-Archive -Path calculator.py,test_calculator.py,requirements.txt,pipeline.py,README.md -DestinationPath calculator-build.zip -Force"'
            }
        }

        stage('Deploy DEV') {
            steps {
                bat 'powershell -Command "Expand-Archive -Path calculator-build.zip -DestinationPath C:\\CICD\\DEV -Force"'
            }
        }

        stage('DEV Approval') {
            steps {
                input message: 'DEV testing completed. Deploy to QA?', ok: 'Proceed'
            }
        }

        stage('Deploy QA') {
            steps {
                bat 'powershell -Command "Expand-Archive -Path calculator-build.zip -DestinationPath C:\\CICD\\QA -Force"'
            }
        }

    }
}

