pipeline {
    agent any

    environment {
        TF_VAR_aws_endpoint   = 'http://host.docker.internal:4566'
        AWS_ACCESS_KEY_ID     = 'mock-ops-key-id'     
        AWS_SECRET_ACCESS_KEY = 'mock-ops-secret-key' 
        AWS_DEFAULT_REGION    = 'us-east-1'           
    }

    tools {
        nodejs 'node18' 
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Cloudops-Devops-Infra/jenkins-serverless-react-cicd.git'
            }
        }

        stage('Infrastructure Provisioning') {
            steps {
                echo 'Setting up Terraform binary...'
                sh '''
                    if [ ! -f ./terraform ]; then
                        curl -fsSL -o terraform.zip https://releases.hashicorp.com/terraform/1.9.0/terraform_1.9.0_linux_amd64.zip
                        unzip -o terraform.zip
                        rm terraform.zip
                        chmod +x ./terraform
                    fi
                '''
                sh './terraform init'
                sh './terraform apply -auto-approve'
            }
        }

        stage('Build Website') {
            steps {
                dir('.') { 
                    echo 'Installing dependencies...'
                    sh 'npm install'
                    echo 'Compiling the website...'
                    sh 'npm run build'
                }
            }
        }

        stage('Deploy to Floci S3') {
            steps {
                echo 'Setting up AWS CLI binary inside container volume...'
                sh '''
                    if [ ! -f /var/jenkins_home/bin/aws ]; then
                        curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
                        unzip -o awscliv2.zip
                        ./aws/install -i /var/jenkins_home/aws-cli -b /var/jenkins_home/bin
                        rm -rf aws awscliv2.zip
                    fi
                '''
                
                echo 'Deploying website to local Floci S3 bucket...'
                sh "/var/jenkins_home/bin/aws --endpoint-url=http://host.docker.internal:4566 s3 sync build/ s3://jenkins-serverless-react-cicd-bucket-v2 --acl public-read"
            }
        }
    }
}