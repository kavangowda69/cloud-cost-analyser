# Cloud Cost Analyser 

This project started off as a way to prove I could actually build something real using AWS — and it ended up becoming a full-fledged cloud billing analysis tool.

The idea?  
- Use AWS Lambda + Cost Explorer to fetch billing data.  
- Store that in S3.  
- Monitor it with CloudWatch.  
- Trigger alerts using SNS when costs cross limits.  


All of this is automated, serverless, and running clean.

---

## ⚙️ Tech Stack

- **Terraform** – Infra as Code to spin up everything neatly.  
- **AWS Lambda** – Python script to fetch billing data via Boto3.  
- **AWS S3** – Stores billing data in JSON/CSV.  
- **CloudWatch** – Monitors billing and triggers alerts.  
- **SNS** – Sends email alerts when budget crosses threshold.  
- **EventBridge Scheduler** – Triggers the Lambda function daily.  
- **Python (Boto3)** – For AWS API interactions.

---

## 🔨 What I Built

I handled the cloud automation part end-to-end. That includes:

- Writing and deploying Terraform config to set up the Lambda robot.  
- Creating IAM roles and setting up cost explorer permissions.  
- Making sure the billing data lands in the S3 bucket daily.  
- Setting up CloudWatch + SNS to send alerts when costs spike.  
- Fetching real billing data from my own AWS account (with the amount at 0 — because I’m too early in the game to rack up big bills 😉).  
- Organized everything cleanly for a recruiter or teammate to easily understand.



---

## 🖼️ Screenshots

Screenshots included for:

- Lambda Function Setup  
- S3 Bucket Uploads  
- EventBridge Trigger Rule  
- SNS Alert Setup  
- Billing Alarm in CloudWatch  

---

## 📂 Folder Structure

```bash
📁 sample-data/
    └── cloud_billing_dataset.csv

📁 terraform/
    ├── main.tf
    ├── provider.tf
    └── lambda.tf

📁 documentation/
    ├── lambda_setup1.png
    ├── lambda_setup2.png
    ├── s3_bucket_upload.png
    ├── eventbridge_rule.png
    └── billing_alarm.png

📁 lambda/
    ├── lambda_function.py

📄 README.md
