# Server-Sent Events (SSE)

Server-Sent Events is an HTTP-based protocol for pushing real-time updates from server to client over a single, long-lived connection. Unlike WebSockets, SSE is one-directional (server → client), uses plain HTTP, and works through proxies and load balancers without special configuration.

## How it works

1. The client opens a connection using the `EventSource` API
2. The server responds with `Content-Type: text/event-stream` and keeps the connection open
3. The server sends messages as plain text frames whenever it has new data
4. If the connection drops, the browser automatically reconnects

## Message format

Each message is a block of `field: value` lines, separated by a blank line:

```
data: Hello world

data: {"user": "alice", "message": "hi"}

event: status_update
data: {"online": 42}

id: 15
data: This message has an ID for resuming
```

- `data:` — the payload (required)
- `event:` — custom event type (default is `message`)
- `id:` — sets the last event ID; on reconnect the browser sends `Last-Event-ID` header so the server can resume from where it left off
- `retry:` — tells the browser how many milliseconds to wait before reconnecting

## Client side (browser)

```javascript
const source = new EventSource("/events");

// Default "message" events
source.addEventListener("message", (e) => {
    console.log(e.data);
});

// Custom named events
source.addEventListener("status_update", (e) => {
    const data = JSON.parse(e.data);
    console.log(`Online users: ${data.online}`);
});

source.addEventListener("error", (e) => {
    console.log("Connection lost, browser will auto-reconnect");
});
```

## Server side (Python example)

```python
from flask import Flask, Response
import time, json

app = Flask(__name__)

@app.route('/events')
def events():
    def stream():
        while True:
            data = json.dumps({"time": time.time()})
            yield f"data: {data}\n\n"
            time.sleep(1)

    return Response(stream(), content_type='text/event-stream',
                    headers={'Cache-Control': 'no-cache',
                             'X-Accel-Buffering': 'no'})
```

The `X-Accel-Buffering: no` header tells Nginx not to buffer the response, which is important when running behind a reverse proxy.

## SSE vs WebSockets

|                         | SSE                          | WebSockets             |
| ----------------------- | ---------------------------- | ---------------------- |
| Direction               | Server → Client              | Bidirectional          |
| Protocol                | HTTP                         | `ws://` / `wss://`     |
| Reconnection            | Automatic (built-in)         | Manual                 |
| Data format             | Text only                    | Text and binary        |
| Resume support          | Built-in via `Last-Event-ID` | Manual                 |
| Proxy/firewall friendly | Yes (plain HTTP)             | Sometimes needs config |
| Browser support         | All modern browsers          | All modern browsers    |

## Common use cases

- **LLM/AI chat streaming** — streaming token-by-token responses (this is how ChatGPT, Claude, and most LLM APIs stream responses)
- **Live notifications** — new messages, alerts, system events
- **Dashboards** — real-time metrics, stock tickers, scores
- **Progress updates** — file uploads, long-running jobs, build pipelines
- **Live feeds** — news, social media timelines, log tailing

## When to pick SSE over WebSockets

Choose SSE when data only flows server => client. It's simpler to implement, works over standard HTTP infrastructure, handles reconnection and resume automatically, and doesn't require a separate protocol upgrade. Use WebSockets when you need bidirectional communication (e.g., multiplayer games, collaborative editing).
