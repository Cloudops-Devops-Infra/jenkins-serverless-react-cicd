pipeline {
    agent any
    
    tools {
        nodejs 'Node18' 
    }
    
    environment {
        AWS_ACCESS_KEY_ID     = 'floci'
        AWS_SECRET_ACCESS_KEY = 'floci'
        AWS_DEFAULT_REGION    = 'us-east-1'
        AWS_ENDPOINT_URL      = 'http://host.docker.internal:4566' 
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling sample React application from GitHub...'
                git branch: 'master', url: 'https://github.com/ahfarmer/calculator.git'
            }
        }
        
        stage('Build Website') {
            steps {
                echo 'Installing dependencies...'
                sh 'npm install'
                
                echo 'Compiling the website...'
                sh 'export NODE_OPTIONS=--openssl-legacy-provider && export PUBLIC_URL=. && npm run build'
            }
        }
        
        stage('Archive Artifact') {
            steps {
                echo 'Saving the compiled files...'
                archiveArtifacts artifacts: 'build/**', allowEmptyArchive: false
            }
        }
        
        stage('Deploy to Floci (Step 4)') {
            steps {
                echo 'Deploying website to local Floci S3 bucket...'
                sh 'aws s3 sync build/ s3://my-local-website-bucket --endpoint-url=$AWS_ENDPOINT_URL'
            }
        }
    }
}
