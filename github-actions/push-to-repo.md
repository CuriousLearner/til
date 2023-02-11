# Permissions for pushing to a repository

By default, the Github Action's bot has only read permission on the repository it is running the action on.

If you try to push to the repository through Github Actions' bot, [you'll get this error which I got on first build of my TIL repo](https://github.com/CuriousLearner/til/actions/runs/4153164170/jobs/7184624317): `remote: Permission to CuriousLearner/til.git denied to github-actions[bot].`

Under `Repository settings > Actions > General > Workflow permissions`, update permission scope to `Read and write permissions` which states `Workflows have read and write permissions in the repository for all scopes.`
