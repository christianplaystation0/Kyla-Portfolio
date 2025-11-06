#!/usr/bin/env python3
"""
Simple HTTP server for Kyla Mates Portfolio
Run this script to serve the website on localhost
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

# Configuration
PORT = 8001
HOST = 'localhost'

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers for development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def start_server():
    """Start the local development server"""
    # Change to the directory containing the HTML file
    os.chdir(Path(__file__).parent)
    
    # Check if index.html exists
    if not os.path.exists('index.html'):
        print("❌ Error: index.html not found in the current directory")
        print("Make sure you're running this script from the portfolio directory")
        sys.exit(1)
    
    try:
        with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
            print("🚀 Kyla Mates Portfolio Server Starting...")
            print(f"📱 Local URL: http://{HOST}:{PORT}")
            print(f"🌐 Network URL: http://0.0.0.0:{PORT}")
            print("📁 Serving files from:", os.getcwd())
            print("\n✨ Your portfolio is now running!")
            print("💡 Press Ctrl+C to stop the server")
            print("-" * 50)
            
            # Open browser automatically
            webbrowser.open(f'http://{HOST}:{PORT}')
            
            # Start serving
            httpd.serve_forever()
            
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Error: Port {PORT} is already in use")
            print(f"💡 Try a different port or stop the process using port {PORT}")
        else:
            print(f"❌ Error starting server: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
        print("👋 Thanks for using Kyla Mates Portfolio!")

if __name__ == "__main__":
    start_server()
