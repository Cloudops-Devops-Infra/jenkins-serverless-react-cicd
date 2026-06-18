# 🚀 Enterprise-Grade GitOps Pipeline: Automated IaC Provisioning, React Deployment & Full-Stack Observability

An advanced, self-contained DevOps pipeline that emulates an enterprise cloud deployment workflow and full-stack observability matrix completely on a local workstation. This project transitions traditional manual infrastructure deployment into a true GitOps lifecycle, utilizing Jenkins for orchestration, HashiCorp Terraform for Infrastructure as Code (IaC), and Docker to encapsulate the continuous integration runners, target cloud environments, and time-series telemetry databases.

---

## 🏗️ System Architecture

The pipeline automates the journey from an infrastructure/code change in the repository to a live application hosted on an emulated cloud platform, while continuously streaming server health telemetry to a centralized visualization deck.

```plaintext
[ Developer Commit ] ──> [ GitHub Repository ]
                                │
                                ▼
                       [ Jenkins Automation ] ───(Exposes Vitals)───┐
                                │                                   │
        ┌───────────────────────┴───────────────────────┐           ▼
        ▼                                               ▼   [ Prometheus Database ]
[ Stage 1: IaC Provisioning ]               [ Stage 2: App Compilation ]    │
  • Downloads Standalone Terraform            • Downloads isolated Node.js  │
  • Forces Path-Style Routing                 • Installs dependencies       ▼
  • Provisions Local S3 Bucket (v2)           • Compiles optimized React [ Grafana Desk ]
        │                                               │             (Dashboard ID: 9964)
        └───────────────────────┬───────────────────────┘
                                ▼
                   [ Stage 3: Cloud Delivery ]
                     • Injects dummy AWS payload variables
                     • Syncs binary assets via AWS CLI
                     • Targets Local Cloud Emulator Network
🛠️ The DevOps Tech Stack
CI/CD Orchestration: Jenkins (Declarative Pipeline / Groovy Scripting)

Infrastructure as Code (IaC): HashiCorp Terraform (v1.9.0)

Time-Series Metric Ingestion: Prometheus (Scraping vitals via custom background collection threads)

Telemetry Visualization Matrix: Grafana (Data source linked over internal bridge proxies)

Containerization & Networking: Docker (Isolated virtual networks bridging host runners)

Application Framework: React.js (Node.js 18 compilation runtime environments)

Local Cloud Platform: Floci / LocalStack (Emulating Amazon S3 API structures)

Command Line Interface: AWS CLI (Configured with dynamic virtual key signing)

📂 Repository Layout
Plaintext
.
├── main.tf               # Terraform configuration declaring the S3 infrastructure blueprint
├── Jenkinsfile           # Enterprise declarative multi-stage automation script
├── prometheus.yml        # Telemetry parsing config mapping targets and collection internals
└── README.md             # Comprehensive architecture and engineering documentation
💡 Note: The React application source code (package.json, src/) is systematically cloned into a transient sandbox directory (/app) during runtime execution to maintain strict structural boundary isolation between platform code and application business logic.

⚙️ Automated Pipeline Stages
1. Checkout Code
Dynamically pulls the infrastructure declarative configurations from GitHub and immediately triggers an isolated horizontal clone of the target functional React source directory into a decoupled subfolder.

2. Infrastructure Provisioning (IaC)
Bootstraps a self-contained, user-space Terraform binary within the workspace. Initializes provider subsystems and evaluates configuration state against the environment. It then executes an automated, hands-free provisioning run (terraform apply -auto-approve) to guarantee that the required target cloud architecture exists before application transport begins.

3. Build Website
Deploys a portable Node.js execution runtime directly inside the pipeline. Isolates package structures, processes npm install, injects OpenSSL backward-compatibility flags, and compiles a highly compact, production-optimized compilation artifact ready for edge-network delivery.

4. Deploy to Floci S3
Instantiates the AWS CLI delivery layer, overrides global routing variables to map directly onto the internal Docker container proxy matrix (host.docker.internal), and standardizes cross-directory synchronization, moving the React frontend static layers directly into the provisioned bucket.

📊 Live System Observability Matrix (Day 3 Expansion)
To ensure the automation engine is monitored like a high-availability production asset, the pipeline integrates real-time systems telemetry scraping.

Metric Extraction: The Jenkins engine hooks directly into a Prometheus metrics extension endpoint at /prometheus/, broadcasting raw JVM application metrics.

Scrape Interval: Prometheus sweeps the endpoint every 5 seconds, compiling system trends into a local database volume.

Visual Control Deck: Grafana consumes the time-series data and populates an official Jenkins Performance and Health Overview Dashboard (ID: 9964), exposing real-time dials for JVM memory usage, executor queue allocations, container CPU load, and stage build durations.

🖼️ Pipeline Visual Verification
1. Jenkins Automation Stage View
Below is the validated proof execution showing the entire declarative orchestration pipeline passing with a clean, consecutive green metrics state:

2. Live Cloud-Hosted Application
The React frontend application running perfectly, hosted directly out of the code-defined, path-routed emulated Amazon S3 bucket instance:

3. Centralized Grafana Telemetry Dashboard (Day 3 Update)
The real-time time-series logging output showing active telemetry aggregation, container load indexes, JVM allocations, and live background scraping:

💡 Real-World Engineering Roadblocks Overcome
Building an automated pipeline from scratch exposes classic architectural challenges. Below are the design hurdles resolved during engineering:

🛡️ Challenge 1: Docker Container Loopback Networking Breakdown
The Symptom: Jenkins executing commands inside a container interpreted localhost as its own internal filesystem, rendering it blind to the cloud emulator running on the host machine.

The Resolution: Abstracted network paths by implementing a custom variable layer in the Terraform configuration, routing Jenkins traffic out of the container boundary using the host bridge endpoint (http://host.docker.internal:4566).

🌐 Challenge 2: S3 DNS Hosted-Style Address Routing Failure
The Symptom: By default, the AWS Terraform provider uses Virtual Hosted-Style bucket structures (e.g., http://bucket-name.localhost:4566). The internal container proxy DNS could not resolve these custom ad-hoc subdomains, leading to immediate no such host crashes.

The Resolution: Enforced Path-Style Addressing inside the AWS provider configuration block by setting s3_use_path_style = true. This forced Terraform to communicate over structural URL paths (http://host.docker.internal:4566/bucket-name), bypassing container DNS layout limitations.

🔑 Challenge 3: AWS CLI Credential Initialization Trap
The Symptom: The automated deployment agent threw a terminating error Unable to locate credentials, blocking asset transport despite communicating with a local mock emulator that required no authentication.

The Resolution: Configured a global environment {} block directly within the declarative Jenkinsfile, injecting persistent dummy cryptographic payloads (AWS_ACCESS_KEY_ID = 'mock_access_key'). This satisfied the security validator check inside the AWS CLI utility wrapper without exposing sensitive production keys.

📦 Challenge 4: OCI Runtime File-vs-Directory Bind-Mount Conflict
The Symptom: When deploying the telemetry database, the container threw an OCI runtime exception (runc create failed: not a directory), immediately crashing Prometheus at startup.

The Resolution: Diagnosed that executing Docker commands from incorrect directories caused Windows to auto-generate an empty placeholder folder named prometheus.yml instead of pointing to the flat configuration text file. Resolved by purging container states, removing the corrupted folder path, and using programmatic PowerShell scripting (Set-Content) to force-write clean configurations directly inside the active project directory.

🔄 Challenge 5: Internal Web UI Container Termination Crash
The Symptom: Forcing a Jenkins plug-in restart from inside the web control panel successfully stopped core automation tasks but killed the underlying Docker container process daemon entirely, dropping port 8080 offline.

The Resolution: Intercepted the crash lifecycle via terminal stream tracing (docker logs -f jenkins), bypassed the broken browser UI state, and executed low-level CLI container restoration steps (docker start jenkins) to safely load the new plugin extensions back into active memory.

🚀 How to Run Locally
Prerequisites
Docker & Docker Desktop active on your system.

Windows PowerShell or Linux Bash terminal shell.

Step 1: Spin up the Local Cloud & Automation Containers
Open your terminal and run the core infrastructure daemons:

PowerShell
docker start jenkins
docker start floci
Step 2: Initialize the Observability Stack
Navigate directly into your local repository directory and spin up the timeseries metrics cluster:

PowerShell
cd .\jenkins-github-project\

# Run the Prometheus collector engine
docker run -d --name prometheus -p 9090:9090 -v "C:\Users\Dell.DESKTOP-FG6ABS7\jenkins-github-project\prometheus.yml:/etc/prometheus/prometheus.yml" prom/prometheus

# Run the Grafana interface dashboard
docker run -d --name grafana -p 3000:3000 grafana/grafana
Step 3: Configure the Jenkins Automation Job
Access the Jenkins UI at http://localhost:8080.

Select New Item -> Create a Pipeline named Website-Deployment-Pipeline.

Scroll to the Pipeline configuration section, change the definition to Pipeline script, paste the repository Jenkinsfile, and click Build Now.

Step 4: Access Your Observability Dashboards
Raw Telemetry Stream: http://localhost:8080/prometheus/

Prometheus Target State: http://localhost:9090 (Verify under Status -> Targets)

Grafana Visual Interface: http://localhost:3000 (Log in with credentials admin / admin, link data source to http://host.docker.internal:9090, and import Dashboard ID 9964).

Developed by Subash Patra — Associate Cloud Engineer

---