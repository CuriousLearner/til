# Lifecycle Ignore changes

> `lifecycle` is a nested block that can appear within a resource block. The `lifecycle` block and its contents are meta-arguments, available for all resource blocks regardless of type.

> `ignore_changes` (list of attribute names) - By default, Terraform detects any difference in the current settings of a real infrastructure object and plans to update the remote object to match configuration.


This is helpful for example in `aws_ecs_service` resource when you want to avoid any changes in the task definition because the version number of the task definition will be out of terraform's cycle of managing the resource.

```bash
resource "aws_ecs_service" "example" {
  name            = "example-service"
  cluster         = aws_ecs_cluster.example.id
  task_definition = aws_ecs_task_definition.example.arn
  desired_count   = 1

  lifecycle {
    ignore_changes = [
        task_definition, desired_count
    ]
  }
}
```

This also ignore the `desired_count` which is useful when you've autoscaling setup. So, tf doesn't want to be concerned on the number of tasks running.
