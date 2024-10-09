# Understanding Permissions in GitHub Actions

`permissions` in GitHub Actions control what a workflow can access and do within a repository. In your workflow file, you can define permissions like this:

```yaml
permissions:
  contents: read
  id-token: write
  deployments: write
```

* `contents: read`: Allows the workflow to read repository contents.
* `id-token: write`: Enables the workflow to request an OpenID Connect (OIDC) token for secure authentication with cloud providers.
* `deployments: write`: Permits the workflow to create or update deployment statuses in GitHub.

By setting precise permissions, you adhere to the principle of least privilege, enhancing the security of your workflows.
