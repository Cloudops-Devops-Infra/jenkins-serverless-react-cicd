import os
import sys

def analyze_infrastructure():
    print("\n[AI Log Analyzer] ?? Scanning project configuration for remediation patterns...")
    
    main_tf_path = "main.tf"
    if not os.path.exists(main_tf_path):
        print("[AI Error] main.tf not found in current directory.")
        sys.exit(1)
        
    with open(main_tf_path, "r") as file:
        content = file.read()

    remediation_needed = False
    report = []

    report.append("====================================================")
    report.append("?? AI OPS AUTOMATED REMEDIATION REPORT             ")
    report.append("====================================================")
    report.append("Status: PIPELINE CRASHED BY SECURITY GATE (TRIVY)")
    report.append("Target Asset: S3 Bucket (calc_bucket)\n")

    if "aws_s3_bucket" in content and "aws_s3_bucket_public_access_block" not in content:
        remediation_needed = True
        report.append("?? [CRITICAL] Vulnerability Found: Public Access Allowed (AWS-0091 / AWS-0093)")
        report.append("?? AI Fix Recommendation:")
        report.append("   Add an explicit 'aws_s3_bucket_public_access_block' resource linked to your bucket.")
        report.append("   Code Blueprint to append to main.tf:")
        report.append("   ```hcl")
        report.append("   resource \"aws_s3_bucket_public_access_block\" \"calc_bucket_privacy\" {")
        report.append("     bucket                  = aws_s3_bucket.calc_bucket.id")
        report.append("     block_public_acls       = true")
        report.append("     block_public_policy     = true")
        report.append("     ignore_public_acls      = true")
        report.append("     restrict_public_buckets = true")
        report.append("   }")
        report.append("   ```\n")

    if "server_side_encryption_configuration" not in content:
        remediation_needed = True
        report.append("?? [HIGH] Vulnerability Found: Missing Server-Side Encryption (AWS-0132)")
        report.append("?? AI Fix Recommendation:")
        report.append("   Secure the bucket's resting state by enforcing SSE-S3 default encryption.")
        report.append("   Code Blueprint to append to main.tf:")
        report.append("   ```hcl")
        report.append("   resource \"aws_s3_bucket_server_side_encryption_configuration\" \"calc_bucket_crypto\" {")
        report.append("     bucket = aws_s3_bucket.calc_bucket.id")
        report.append("     rule {")
        report.append("       apply_server_side_encryption_by_default {")
        report.append("         sse_algorithm = \"AES256\"")
        report.append("       }")
        report.append("     }")
        report.append("   }")
        report.append("   ```\n")

    if remediation_needed:
        with open("ai_remediation_report.md", "w") as f:
            f.write("\n".join(report))
        print("\n".join(report))
        print("[AI Log Analyzer] ? Remediation report generated: ai_remediation_report.md")
    else:
        print("[AI Log Analyzer] No obvious infrastructure misconfigurations detected.")

if __name__ == "__main__":
    analyze_infrastructure()
