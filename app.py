import streamlit as st
import socket
from datetime import datetime

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except socket.error:
        return False


st.set_page_config(page_title="Port Scanner", page_icon="🔍")

st.title("🔍 Port Scanner")
st.write("Scan a target for open ports. Only scan systems you own or have permission to test.")

target = st.text_input("Target IP or hostname", value="127.0.0.1")

col1, col2 = st.columns(2)
with col1:
    start_port = st.number_input("Start port", min_value=1, max_value=65535, value=1)
with col2:
    end_port = st.number_input("End port", min_value=1, max_value=65535, value=1000)

if st.button("Start Scan"):
    if end_port < start_port:
        st.error("End port must be greater than or equal to start port.")
    elif end_port - start_port > 5000:
        st.warning("Please scan a smaller range (max 5000 ports) to keep it fast.")
    else:
        progress_bar = st.progress(0)
        status_text = st.empty()
        open_ports = []

        total_ports = end_port - start_port + 1

        for i, port in enumerate(range(start_port, end_port + 1)):
            if scan_port(target, port):
                open_ports.append(port)
            progress_bar.progress((i + 1) / total_ports)
            status_text.text(f"Scanning port {port}...")

        status_text.empty()
        progress_bar.empty()

        st.subheader("Results")
        if open_ports:
            st.success(f"Found {len(open_ports)} open port(s): {open_ports}")
        else:
            st.info("No open ports found in this range.")