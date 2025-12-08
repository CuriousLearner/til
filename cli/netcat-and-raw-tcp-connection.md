# Netcat (`nc`) and Raw TCP Communication

**Netcat (`nc`)** is a powerful tool for working with raw TCP and UDP connections. Unlike higher-level tools like `curl` or `telnet`, `nc` communicates directly with a port without adding protocol-specific overhead, making it ideal for debugging low-level network issues.

---

### Using `nc` for Raw TCP Connections

A basic connection test:

```bash
nc -v 127.0.0.1 9092
```

- `-v` (verbose) shows connection success or failure.
- If a service (like Kafka) is running on `9092`, `nc` connects and waits for data.

---

### Sending Raw Data Over TCP

Netcat lets you send arbitrary data:

```bash
echo "Hello Server" | nc 127.0.0.1 9092
```

- Sends "Hello Server" over raw TCP to port `9092`.
- If the server expects a specific protocol (e.g., Kafka), it may not respond, but the connection still works.

---

### Why Netcat?

- Works with **raw TCP/UDP** (no HTTP, SSH, or extra formatting).
- Can act as a **server**:

  ```bash
  nc -l 9092
  ```

  - This makes Netcat **listen** on port `9092`, waiting for incoming connections.
  - Any data sent to this port by a client will be displayed in the terminal.
- Great for **port scanning**:

  ```bash
  nc -zv 127.0.0.1 9092
  ```

  (The `-z` option checks if the port is open without sending data.)

Netcat is a versatile network Swiss Army knife, especially useful for debugging services like **Kafka, Redis, or raw socket servers**!
