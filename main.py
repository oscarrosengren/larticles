import streamlit as st
import os
import subprocess
import sys

def get_python_scripts(directory):
    """Returns a list of Python script filenames in the given directory."""
    return [f for f in os.listdir(directory) if f.endswith(".py") and f != os.path.basename(__file__)]

def run_script(script_name):
    """Executes a selected Python script in a new subprocess."""
    python_executable = sys.executable  # Gets the Python environment where Streamlit is running

    try:
        process = subprocess.Popen(
            [python_executable, script_name], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True
        )
        stdout, stderr = process.communicate()

        if stdout:
            st.text_area("Output:", stdout, height=300)
        if stderr:
            st.text_area("Errors:", stderr, height=300, key="stderr")

    except Exception as e:
        st.error(f"Error running script: {e}")

# Streamlit UI
st.title("📜 Script Launcher")

repo_dir = os.path.dirname(os.path.abspath(__file__))
scripts = get_python_scripts(repo_dir)

if not scripts:
    st.warning("No Python scripts found in the repository.")
else:
    selected_script = st.selectbox("Select a script to run:", scripts)
    if st.button("Run Script"):
        run_script(os.path.join(repo_dir, selected_script))
