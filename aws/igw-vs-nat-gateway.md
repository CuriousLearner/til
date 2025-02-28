# IGW vs. NAT – Understanding Private to Public IP Mapping

In AWS networking, Internet Gateway (IGW) and NAT Gateway (NAT) handle private-to-public IP mapping differently:

- **Internet Gateway (IGW)**:

    - Facilitates direct communication between instances in a public subnet and the internet.
    - Each instance must have a public IP (assigned dynamically or via an Elastic IP (EIP)) to be directly accessible.
    - Uses 1:1 private-to-public IP mapping, meaning each instance with a public IP has a unique public identity.

- **NAT Gateway (NAT):**

    - Used for instances in a private subnet to access the internet without being directly reachable from the outside.
    - Implements IP masquerading (N:1), meaning multiple instances can share a single public IP to make outbound connections.
    - Only supports outbound connections; inbound traffic is not directly possible.

## 📌 Key takeaway:

- Use IGW when instances need both inbound and outbound internet access.
- Use NAT when private instances only need outbound internet access while remaining hidden from the public internet.
