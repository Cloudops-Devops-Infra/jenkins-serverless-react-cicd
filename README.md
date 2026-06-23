# Pipeline: Automated IaC Provisioning, DevSecOps Security Gates & Full-Stack Observability

![Jenkins](https://img.shields.io/badge/CI%2FCD-Jenkins-blue?style=for-the-badge&logo=jenkins)
![Terraform](https://img.shields.io/badge/Infra-Terraform-7B42BC?style=for-the-badge&logo=terraform)
![Trivy](https://img.shields.io/badge/Security-Trivy-00A4A6?style=for-the-badge&logo=aquasecurity)
![AWS](https://img.shields.io/badge/Cloud-LocalStack%2FFloci-FF9900?style=for-the-badge&logo=amazon-aws)

An advanced, self-contained DevSecOps pipeline that emulates an enterprise cloud deployment workflow, security gate scanning compliance, and full-stack observability matrix completely on a local workstation. This project transitions traditional manual infrastructure deployment into a true GitOps lifecycle, utilizing Jenkins for orchestration, HashiCorp Terraform for Infrastructure as Code (IaC), Aquasecurity Trivy for vulnerability parsing, and Docker Compose to encapsulate target environments and time-series telemetry databases.

---

## Project Evolution Timeline (Day 1 to Present)

This repository tracks my engineering progression from cloud sandboxing to building production-grade, highly secure, and observable localized clusters:
* **Day 1: Public Cloud Exploration:** Initial design focused on building serverless patterns in public AWS (S3, API Gateway, Lambda, DynamoDB). Moved to a local stack execution model to guarantee strict cost-containment ($0.00 infrastructure bill lifecycle).
* **Day 2: Infrastructure as Code & Pipeline Decoupling:** Migrated to local cloud emulation layers (Floci/LocalStack). Wrote declarative Groovy pipelines to automate infrastructure provisioning via HashiCorp Terraform alongside Node.js asset generation frameworks.
* **Day 3: Full-Stack Observability Matrix:** Extended the runtime engine with deep telemetry collectors (Prometheus time-series scrapers) and performance monitoring panels (Grafana) to track pipeline and container resource consumption.
* **Day 4: Shift-Left DevSecOps & AI Native Remediation:** Hardened the pipeline by integrating a static analysis compliance gate. Overcame Docker-in-Docker encapsulation traps by deploying portable standalone binary runtimes, and engineered a native fault-interception engine that automatically parses misconfigured S3 blocks to write live engineering mitigation reports.

---

## System Architecture

The pipeline automates the journey from an infrastructure/code change in the repository to a live application hosted on an emulated cloud platform, while continuously validating security thresholds and streaming systems health telemetry to a centralized visualization deck.

```text
[ Developer Commit ] ──> [ GitHub Repository ]
                                │
                                ▼
                       [ Jenkins Automation ] ───(Exposes Vitals)───┐
                                │                                   │
        ┌───────────────────────┴───────────────────────┐           ▼
        ▼                                               ▼   [ Prometheus Database ]
[ Stage 1: Checkout & Pull ]                 [ Stage 2: Security Scan ]     │
  • Resets local workspace                     • Standalone Trivy Engine    │
  • Clones master Git tree                     • Blocks unsafe HCL code     ▼
        │                                               │   [ Grafana Desk ]
        ▼                                               ▼    (Dashboard UI)
[ Stage 3: Build Web Assets ]                [ Stage 4: Cloud Delivery ]
  • Compiles React components                  • Bypasses Loopback Ports
  • Unpacks production code                    • Syncs secure S3 targets
Tech Stack and Tooling
CI/CD Orchestration: Jenkins (Declarative Pipeline / Groovy Scripting)

Infrastructure Configuration: HashiCorp Terraform (v1.9.0)

Static Application Security Testing (SAST): Aquasecurity Trivy Engine

Time-Series Metric Ingestion: Prometheus (Scraping vitals via native exporter integrations)

Telemetry Visualization Matrix: Grafana (Data source linked over internal bridge networks)

Containerization & Networking: Docker & Docker Compose

Local Cloud Platform: Floci / LocalStack (Emulating Amazon S3 API structures)

Repository Layout
Plaintext
.
├── main.tf                 # Patched Terraform configuration declaring secure S3 architectures
├── Jenkinsfile             # Enterprise declarative multi-stage automation script with native AI fallbacks
├── docker-compose.yml      # Unified container orchestration manifest for the core systems stack
├── prometheus.yml          # Telemetry parsing config mapping targets and collection internals
└── README.md               # Comprehensive architecture and engineering documentation
Automated Pipeline Stages
1. Checkout Code
Dynamically pulls the latest repository tree from GitHub, ensuring clean version history state synchronization prior to code execution.

2. DevSecOps Security Scan (Shift-Left)
Downloads and runs a performance-isolated static analysis compiler. Evaluates main.tf files against global security vectors. If any high or critical flaws are uncovered (such as public bucket exposure or missing resting-state encryption algorithms), the security gate throws an exit code 1, automatically crashing the deployment line before a bad configuration goes live.

3. Build Website
Deploys a portable execution runtime inside the pipeline workspace, assembling code assets and packaging them into clean, optimized production-ready HTML elements.

4. Deploy to Floci S3
Instantiates the automated AWS CLI delivery layer, overrides global network routing paths to talk directly to the host container proxy network (host.docker.internal:4566), signs mock authorizations, and safely syncs the compiled distribution code to your bucket.

Automated Security Mitigation Metrics
Intentional Failure Interception
When unencrypted configurations are detected within the infrastructure tree, the workflow catches the error code and spins up a native post-mortem handler to print out clear remediation actions directly to the engineer:

Plaintext
====================================================
AI OPS AUTOMATED REMEDIATION REPORT             
====================================================
Status: PIPELINE CRASHED BY SECURITY GATE
Target Asset: S3 Bucket (calc_bucket)\n
[CRITICAL] Vulnerability Found: Public Access Allowed (AWS-0091)
Fix Recommendation: Add an explicit 'aws_s3_bucket_public_access_block' resource.
Verified Hardened State
Once compliant remediation blocks are written to the infrastructure tree, the compliance check gives a clean pass, running downstream deployments smoothly:

Plaintext
Running DevSecOps Security Scan engine...
[Pipeline] readFile
[Pipeline] echo
SECURITY GATE PASSED: All high/critical configurations are fully secure!
Real-World Engineering Roadblocks Overcome
Challenge 1: Docker-in-Docker (DinD) Nesting Constraint
The Symptom: Attempting to run docker run aquasecurity/trivy from inside a containerized Jenkins agent threw a terminating docker: not found error.

The Resolution: Avoided complex socket mount pathways by downloading the compiled standalone Linux binary package directly into the user-space workspace, running security tasks completely natively.

Challenge 2: Groovy Script Engine Compilation Collisions
The Symptom: Inserting Python-style scripting comments (#) into post-action script blocks caused immediate Jenkins syntax interpretation errors.

The Resolution: Adjusted commenting architecture to strict Java/Groovy standards (//), satisfying compiler restrictions.

Challenge 3: S3 DNS Hosted-Style Address Routing Failure
The Symptom: Default AWS configurations utilize virtual hosted subdomains which local container proxy DNS paths cannot resolve.

The Resolution: Enforced explicit path-style parameters (s3_use_path_style = true) within the Terraform provider payload configuration to guide lookups directly through linear URLs.

How to Run Locally
1. Launch Environment
PowerShell
docker start jenkins prometheus grafana floci-local
2. Run Pipeline
Access your Jenkins interface at http://localhost:8080, click Build Now inside your existing Website-Deployment-Pipeline workspace, and watch your validation pass cleanly!

Developed by Subash Patra — Associate Cloud Engineer