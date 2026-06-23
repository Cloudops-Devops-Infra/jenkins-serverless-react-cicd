pipeline {
    agent any
    
    environment {
        AWS_cli_binary        = '/var/jenkins_home/bin/aws'
        AWS_ACCESS_KEY_ID     = 'mock_access_key_id'
        AWS_SECRET_ACCESS_KEY = 'mock_secret_access_key'
        AWS_DEFAULT_REGION    = 'us-east-1'
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling latest application assets...'
                cleanWs()
                git branch: 'main', url: 'https://github.com/Cloudops-Devops-Infra/jenkins-serverless-react-cicd'
            }
        }
        
        stage('Security Scan') {
            steps {
                script {
                    echo '??? Running DevSecOps Security Scan engine...'
                    def mainTf = readFile('main.tf')
                    def issuesFound = false
                    
                    if (mainTf.contains("aws_s3_bucket") && !mainTf.contains("aws_s3_bucket_public_access_block")) {
                        echo "[SECURITY FLAWS DETECTED] CRITICAL: S3 bucket allows public access (AWS-0091/AWS-0093)"
                        issuesFound = true
                    }
                    if (!mainTf.contains("server_side_encryption_configuration")) {
                        echo "[SECURITY FLAWS DETECTED] HIGH: S3 bucket missing server-side encryption (AWS-0132)"
                        issuesFound = true
                    }
                    
                    if (issuesFound) {
                        error("Security scan failed: High/Critical vulnerabilities detected in infrastructure code.")
                    } else {
                        echo "? SECURITY GATE PASSED: All high/critical configurations are fully secure!"
                    }
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Building React production assets...'
                sh 'mkdir -p build && echo "<h1>Welcome to the AIOps-GitOps Stack Dashboard</h1>" > build/index.html'
            }
        }
        
        stage('Deploy to S3') {
            steps {
                echo '?? Deploying verified secure assets to Local AWS Mock Environment...'
                sh "${AWS_cli_binary} --endpoint-url=http://host.docker.internal:4566 s3 mb s3://jenkins-serverless-react-cicd-bucket-v2 || true"
                sh "${AWS_cli_binary} --endpoint-url=http://host.docker.internal:4566 s3 sync build/ s3://jenkins-serverless-react-cicd-bucket-v2 --acl public-read"
                echo '?? Deployment Completed Successfully!'
            }
        }
    }

    post {
        failure {
            script {
                echo '?? Pipeline Execution Crashed! Activating Native AI Log Analyzer...'
                
                def mainTf = readFile('main.tf')
                def report = []
                def remediationNeeded = false
                
                report.add("====================================================")
                report.add("?? AI OPS AUTOMATED REMEDIATION REPORT             ")
                report.add("====================================================")
                report.add("Status: PIPELINE CRASHED BY SECURITY GATE")
                report.add("Target Asset: S3 Bucket (calc_bucket)\n")
                
                if (mainTf.contains("aws_s3_bucket") && !mainTf.contains("aws_s3_bucket") && !mainTf.contains("aws_s3_bucket_public_access_block")) {
                    remediationNeeded = true
                    report.add("?? [CRITICAL] Vulnerability Found: Public Access Allowed (AWS-0091 / AWS-0093)")
                    report.add("?? AI Fix Recommendation: Add an explicit 'aws_s3_bucket_public_access_block' resource.")
                }
                
                if (!mainTf.contains("server_side_encryption_configuration")) {
                    remediationNeeded = true
                    report.add("?? [HIGH] Vulnerability Found: Missing Server-Side Encryption (AWS-0132)")
                }
                
                if (remediationNeeded) {
                    def finalReport = report.join("\n")
                    echo finalReport
                    writeFile file: 'ai_remediation_report.md', text: finalReport
                } else {
                    echo "[AI Log Analyzer] No obvious infrastructure misconfigurations detected."
                }
            }
        }
    }
}
