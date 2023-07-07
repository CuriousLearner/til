# Setup SSH Tunneling

One plausible use case is accessing database in private subnet by creating SSH tunnel through the EC2 in public subnet like:

```
ssh -L <local-port>:<database>.us-east-2.rds.amazonaws.com:<dbport> ec2-user@<host-ip>
```

Now you can access the DB on `local-port` in your system.
