import os
import sys
import runpy

# Ensure root directory is in python path
sys.path.insert(0, os.path.abspath("."))

# Run the main Streamlit application
runpy.run_path("controlplane/app/streamlit_app.py", run_name="__main__")
