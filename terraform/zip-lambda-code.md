# Zip Lambda code

You can configure terraform to zip-lambda function on triggers like:

```bash
# Zip the Lambda Function Code (local-exec example)
resource "null_resource" "zip_lambda" {
  provisioner "local-exec" {
    command = "zip lambda_function.zip lambda_function.py"
  }

  triggers = {
    always_run = "${timestamp()}"
  }
}
```
