# Force unlock state file

If you're dealing with a locked state in Terragrunt, you can unlock it using the following command:

```bash
terragrunt force-unlock <LOCK_ID>
```

This action should be taken cautiously and only when you're certain that no ongoing `plan` or `apply` operations are running in Terragrunt.
