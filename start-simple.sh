#!/bin/bash
# Simple Jekyll development server using Node.js (no Ruby required)

echo "🚀 Starting simple development server..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js first."
    echo "Download from: https://nodejs.org/"
    exit 1
fi

# Check if we have a simple server installed
if ! command -v npx &> /dev/null; then
    echo "❌ npx not found. Please install Node.js with npm."
    exit 1
fi

echo "✅ Node.js found, starting simple HTTP server..."
echo "📂 Serving files from current directory"
echo "🌐 Open your browser to: http://localhost:3000"
echo "⚠️  Note: This is a simple file server, not full Jekyll processing"
echo "   For full Jekyll features, use Docker or install Ruby/Jekyll"
echo ""
echo "Press Ctrl+C to stop the server"

# Start a simple HTTP server
npx http-server . -p 3000 -o