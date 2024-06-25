# MongoDB installation script with PATH modification

# Specify installation directory
$installDir = "C:\MongoDB"

# Download MongoDB
Invoke-WebRequest -Uri "https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-6.0.15.zip" -OutFile "$installDir\mongodb.zip"

# Extract MongoDB directly into the installation directory
Expand-Archive -Path "$installDir\mongodb.zip" -DestinationPath $installDir


# Create data directory
New-Item -ItemType Directory -Path "$installDir\data"

# Create config file
@"
systemLog:
  destination: file
  path: $installDir\mongod.log
storage:
  dbPath: $installDir\data
"@ | Out-File "$installDir\mongod.cfg"

# Install MongoDB as a service
& "$installDir\bin\mongod.exe" --config "$installDir\mongod.cfg" --install

# Set service to autostart
Set-Service MongoDB -StartupType Automatic

# Start MongoDB service
Start-Service MongoDB

# Verify installation
mongo --eval "db.version()"

# Clean up
Remove-Item "$installDir\mongodb.zip" -Force
