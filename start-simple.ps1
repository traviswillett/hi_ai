# Simple HTTP server using Node.js (alternative to Docker)

Write-Host "🚀 Starting simple development server..." -ForegroundColor Cyan

# Check if Node.js is installed
try {
    $nodeVersion = node --version
    Write-Host "✅ Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Node.js not found. Please install Node.js first." -ForegroundColor Red
    Write-Host "Download from: https://nodejs.org/" -ForegroundColor Yellow
    exit 1
}

Write-Host "📂 Serving files from current directory" -ForegroundColor Blue
Write-Host "🌐 Open your browser to: http://localhost:3000" -ForegroundColor Green
Write-Host "⚠️  Note: This is a simple file server, not full Jekyll processing" -ForegroundColor Yellow
Write-Host "   For full Jekyll features, use Docker or install Ruby/Jekyll" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Cyan

# Start a simple HTTP server
npx http-server . -p 3000 -o