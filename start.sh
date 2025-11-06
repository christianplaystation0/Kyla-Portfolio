#!/bin/bash
# Start script for Kyla Mates Portfolio

echo "🎨 Starting Kyla Mates Portfolio Server..."
echo "📁 Working directory: $(pwd)"

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    echo "🐍 Using Python 3"
    python3 server.py
elif command -v python &> /dev/null; then
    echo "🐍 Using Python"
    python server.py
else
    echo "❌ Python not found. Please install Python 3"
    echo "💡 You can also open index.html directly in your browser"
    exit 1
fi
