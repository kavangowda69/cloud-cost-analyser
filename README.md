# Cloud Cost Analyser (AWS)

A fully serverless AWS cost monitoring and alerting system designed to provide clear visibility into cloud spend and notify teams when costs cross defined thresholds.

This project demonstrates how to automate cloud billing analysis using native AWS services with Infrastructure as Code.

---

## 🔍 What This Project Does

- Fetches AWS billing data using **AWS Cost Explorer**
- Stores cost data in **Amazon S3** (JSON / CSV)
- Monitors usage using **Amazon CloudWatch**
- Triggers automated **email alerts via SNS** when cost thresholds are exceeded
- Runs on a **daily schedule** using EventBridge
- Fully automated, serverless, and reproducible using Terraform

---

## 🧱 Architecture Overview

AWS Lambda (Python)  
→ Fetches cost data via Boto3  
→ Stores data in Amazon S3  

Amazon CloudWatch  
→ Monitors billing metrics  
→ Triggers alarms  

Amazon SNS  
→ Sends email notifications  

Amazon EventBridge  
→ Invokes Lambda on a daily schedule  

---

## ⚙️ Tech Stack

- **Terraform** – Infrastructure as Code (end-to-end provisioning)
- **AWS Lambda** – Serverless cost data collection
- **Amazon S3** – Cost data storage
- **Amazon CloudWatch** – Monitoring and alarms
- **Amazon SNS** – Email notifications
- **Amazon EventBridge** – Scheduled execution
- **Python (Boto3)** – AWS API interactions

---

## 🔨 What I Implemented

- Designed and deployed the full infrastructure using **Terraform**
- Created secure **IAM roles and Cost Explorer permissions**
- Automated daily cost data collection and storage in S3
- Configured CloudWatch alarms and SNS notifications
- Structured the repository for easy understanding and handoff

> Note: Billing values are currently minimal as this was tested on a personal AWS account. The system is production-ready and scalable.

---

## 🖼️ Screenshots Included

- Lambda configuration
- S3 cost data uploads
- EventBridge scheduling rule
- CloudWatch billing alarm
- SNS alert setup


---

## 🎯 Use Cases

- AWS cost monitoring for startups and small teams
- Automated budget alerts
- Cloud cost visibility without third-party tools
