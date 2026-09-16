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

        stage('DEV Approval') {
            steps {
                input message: 'Testing completed. Approve deployment to DEV?', ok: 'Deploy to DEV'
            }
        }

        stage('Deploy DEV') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dev-server-credential',
                        usernameVariable: 'DEV_USERNAME',
                        passwordVariable: 'DEV_PASSWORD'
                    )
                ]) {

                    powershell '''
                        $username = $env:DEV_USERNAME

                        $password = ConvertTo-SecureString `
                            $env:DEV_PASSWORD `
                            -AsPlainText `
                            -Force

                        $cred = New-Object System.Management.Automation.PSCredential(
                            $username,
                            $password
                        )

                        Write-Host "Connecting to DEV server..."

                        New-PSDrive `
                            -Name "DEV" `
                            -PSProvider FileSystem `
                            -Root "\\\\Lab-VM4\\C$" `
                            -Credential $cred

                        Write-Host "Copying artifact to DEV server..."

                        Copy-Item `
                            "calculator-build.zip" `
                            "DEV:\\CICD\\DEV\\calculator-build.zip" `
                            -Force

                        Write-Host "Artifact copied to Lab-VM4"

                        Remove-PSDrive -Name "DEV"
                    }
                }
            }
        }

        stage('Deploy DEV Application') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dev-server-credential',
                        usernameVariable: 'DEV_USERNAME',
                        passwordVariable: 'DEV_PASSWORD'
                    )
                ]) {

                    powershell '''
                        $username = $env:DEV_USERNAME

                        $password = ConvertTo-SecureString `
                            $env:DEV_PASSWORD `
                            -AsPlainText `
                            -Force

                        $cred = New-Object System.Management.Automation.PSCredential(
                            $username,
                            $password
                        )

                        Write-Host "Extracting artifact on DEV server..."

                        Invoke-Command `
                            -ComputerName Lab-VM4 `
                            -Credential $cred `
                            -Authentication Kerberos `
                            -ScriptBlock {

                                Expand-Archive `
                                    -Path "C:\\CICD\\DEV\\calculator-build.zip" `
                                    -DestinationPath "C:\\CICD\\DEV" `
                                    -Force

                                Write-Host "Calculator deployed to DEV"
                            }
                    '''
                }
            }
        }

        stage('QA Approval') {
            steps {
                input message: 'DEV testing completed. Approve deployment to QA?', ok: 'Deploy to QA'
            }
        }

        stage('Deploy QA') {
            steps {
                bat 'powershell -Command "Expand-Archive -Path calculator-build.zip -DestinationPath C:\\CICD\\QA -Force"'
            }
        }

    }
}