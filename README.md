
# Port Scanner
🔗 **Live Demo:** [Try it here](https://port-scanner-nxxtgkpjabzhk6nnzhr4e8.streamlit.app/)

⚠️ **Note:** When using the live demo, scanning `127.0.0.1` will scan Streamlit's own server, not your personal device. For testing your own machine, run the tool locally.

A Python-based TCP port scanner that identifies open ports on a target host.

⚠️ **Disclaimer:** Only use this tool on systems you own or have explicit permission to test. Unauthorized port scanning may be illegal.

## Features
- Scans a customizable port range
- Real-time progress bar
- Identifies open TCP ports on a target IP/hostname

## Tech Stack
Python, Socket programming, Streamlit

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## What I Learned
This project helped me understand how TCP connections work at a low level, and how port scanning is used in both offensive (reconnaissance) and defensive (auditing your own network) security contexts.
