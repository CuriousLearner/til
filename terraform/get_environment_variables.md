# Reading directly from environment variables

We can use `get_env` function to directly read environment variables present. This means that the variables don't need to have `TF_VAR_` prefix. We are directly reading `TF_STATE_ROLE_ARN` if present in the env, and if not, then using the default value.


```tf
locals {
  # This will check the regular environment variable "TF_CI_ROLE_ARN"
  tf_state_role_arn = get_env("TF_STATE_ROLE_ARN", "arn:aws:iam::XXXXXXXXX:role/terraform-state")
}

remote_state {
  backend = "s3"

  config = {
    bucket         = local.bucket
    region         = local.region
    key            = local.key
    dynamodb_table = local.dynamodb_table
    encrypt        = true
    role_arn       = local.tf_state_role_arn
  }
}
```
