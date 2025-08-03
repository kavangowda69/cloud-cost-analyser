resource "aws_s3_bucket" "billing_data" {
  bucket = "billing-data-gowda"  
  acl    = "private"

  tags = {
    Name        = "Billing Data Bucket"
    Environment = "Dev"
  }
}
