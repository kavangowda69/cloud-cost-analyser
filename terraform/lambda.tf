resource "aws_iam_role" "lambda_exec_role" {
  name = "lambda_billing_role_tf"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action    = "sts:AssumeRole",
      Principal = {
        Service = "lambda.amazonaws.com"
      },
      Effect = "Allow",
      Sid     = ""
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_policy_attach" {
  role       = aws_iam_role.lambda_exec_role.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}

resource "aws_lambda_function" "billing_lambda" {
  function_name = "billing-fetcher-tf"
  filename      = "${path.module}/function.zip"   # This zip came from your lambda folder
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.10"
  role          = aws_iam_role.lambda_exec_role.arn
  timeout       = 10

  source_code_hash = filebase64sha256("${path.module}/function.zip")
}
