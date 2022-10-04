# Path: app.py
import streamlit as st
import os
import sys
import time
import subprocess
from pyngrok import ngrok

def main():
    public_url = ngrok.connect(port='8501')
    print(public_url)
    os.system("streamlit run Test.py")

if __name__ == "__main__":
    main()