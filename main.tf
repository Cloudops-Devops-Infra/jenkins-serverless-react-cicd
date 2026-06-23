provider "aws" {
  region                      = "us-east-1"
  access_key                  = "mock_access_key"
  secret_key                  = "mock_secret_key"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    s3 = "http://host.docker.internal:4566"
  }
}

resource "aws_s3_bucket" "calc_bucket" {
  bucket        = "jenkins-serverless-react-cicd-bucket-v2"
  force_destroy = true
}

# ??? FIX 1: Enforce Private Access Controls (Fixes AWS-0091 & AWS-0093)
resource "aws_s3_bucket_public_access_block" "calc_bucket_privacy" {
  bucket                  = aws_s3_bucket.calc_bucket.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# ??? FIX 2: Enforce Default Server-Side Encryption (Fixes AWS-0132)
resource "aws_s3_bucket_server_side_encryption_configuration" "calc_bucket_crypto" {
  bucket = aws_s3_bucket.calc_bucket.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
