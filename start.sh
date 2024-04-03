#!/bin/bash

# Run your Streamlit app
streamlit run app.py &

# Run your HTTP server
python -m http.server --directory datadrive 3306 &

# Run worker / ai-controller
python worker_stream.py

