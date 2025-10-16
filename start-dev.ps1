# PowerShell script to start Docker Desktop and run Jekyll development server

Write-Host "🐳 Starting Docker Desktop..." -ForegroundColor Cyan

# Try to start Docker Desktop
$dockerDesktopPath = "C:\Program Files\Docker\Docker\Docker Desktop.exe"
if (Test-Path $dockerDesktopPath) {
    Start-Process $dockerDesktopPath
    Write-Host "✅ Docker Desktop starting..." -ForegroundColor Green
    Write-Host "⏳ Waiting for Docker to be ready..." -ForegroundColor Yellow
    
    # Wait for Docker to be ready (max 60 seconds)
    $timeout = 60
    $elapsed = 0
    do {
        Start-Sleep -Seconds 2
        $elapsed += 2
        try {
            docker info | Out-Null
            $dockerReady = $true
            break
        } catch {
            $dockerReady = $false
        }
        Write-Host "." -NoNewline -ForegroundColor Yellow
    } while ($elapsed -lt $timeout -and -not $dockerReady)
    
    Write-Host ""
    
    if ($dockerReady) {
        Write-Host "✅ Docker is ready!" -ForegroundColor Green
        Write-Host "🚀 Starting Jekyll development server..." -ForegroundColor Cyan
        Write-Host "🎨 Using development config to fix CSS loading..." -ForegroundColor Yellow
        docker-compose down
        docker-compose up
    } else {
        Write-Host "❌ Docker didn't start in time. Please start Docker Desktop manually and run 'docker-compose up'" -ForegroundColor Red
    }
} else {
    Write-Host "❌ Docker Desktop not found at expected location." -ForegroundColor Red
    Write-Host "Please install Docker Desktop from: https://www.docker.com/products/docker-desktop" -ForegroundColor Yellow
}