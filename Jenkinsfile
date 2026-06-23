pipeline {
    agent any
    
    environment {
        AWS_ACCESS_KEY_ID     = 'mock-ops-key-id'
        AWS_SECRET_ACCESS_KEY = 'mock-ops-secret-key'
        AWS_DEFAULT_REGION    = 'us-east-1'
    }

    stages {
        stage('Checkout') {
            steps {
                cleanWs()
                checkout scm
            }
        }
        
        stage('Security Scan') {
            steps {
                script {
                    echo '??? Running DevSecOps Security Scan...'
                    sh 'docker run --rm -v ${WORKSPACE}:/apps aquasec/trivy:latest fs --scanners vuln,secret,config --severity HIGH,CRITICAL --exit-code 1 /apps'
                }
            }
        }
    }

    post {
        failure {
            script {
                echo '?? Build failed! Activating AI Log Analyzer...'
                sh 'python3 ai_log_analyzer.py'
            }
        }
    }
}
