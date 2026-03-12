#!/bin/bash
echo "Stopping old processes..."
pkill -f streamlit
pkill -f cloudflared
echo "Starting Streamlit..."
streamlit run ./src/dashboard.py --server.address 0.0.0.0 &
sleep 5
echo "Starting Cloudflare Tunnel..."
cloudflared tunnel --url http://localhost:8501