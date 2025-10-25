"""
Setup script for Temporal workflow system
This script helps set up the Temporal server and worker
"""

import subprocess
import sys
import os
import time

def install_temporal_cli():
    """Install Temporal CLI if not present"""
    try:
        result = subprocess.run(['temporal', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Temporal CLI already installed")
            return True
    except FileNotFoundError:
        pass
    
    print("📦 Installing Temporal CLI...")
    
    # Install based on OS
    if sys.platform == "darwin":  # macOS
        subprocess.run(['brew', 'install', 'temporalio/tap/temporal'], check=True)
    elif sys.platform == "linux":
        subprocess.run(['curl', '-sSf', 'https://temporal.download/cli.sh', '|', 'sh'], shell=True, check=True)
    else:
        print("❌ Please install Temporal CLI manually for your OS")
        return False
    
    print("✅ Temporal CLI installed successfully")
    return True

def start_temporal_server():
    """Start Temporal server in development mode"""
    print("🚀 Starting Temporal server...")
    
    try:
        # Start Temporal server
        process = subprocess.Popen(['temporal', 'server', 'start-dev'], 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE)
        
        # Wait a moment for server to start
        time.sleep(5)
        
        print("✅ Temporal server started on localhost:7233")
        return process
        
    except Exception as e:
        print(f"❌ Failed to start Temporal server: {e}")
        return None

def setup_worker():
    """Set up the Temporal worker"""
    print("👷 Setting up Temporal worker...")
    
    try:
        # Install Python dependencies
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
        print("✅ Dependencies installed")
        
        # Start worker in background
        worker_process = subprocess.Popen([sys.executable, 'temporal_worker.py'],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
        
        print("✅ Temporal worker started")
        return worker_process
        
    except Exception as e:
        print(f"❌ Failed to set up worker: {e}")
        return None

def main():
    """Main setup function"""
    print("🎯 Setting up Temporal workflow system for button analytics...")
    
    # Step 1: Install Temporal CLI
    if not install_temporal_cli():
        print("❌ Failed to install Temporal CLI")
        return
    
    # Step 2: Start Temporal server
    server_process = start_temporal_server()
    if not server_process:
        print("❌ Failed to start Temporal server")
        return
    
    # Step 3: Set up worker
    worker_process = setup_worker()
    if not worker_process:
        print("❌ Failed to set up worker")
        return
    
    print("\n🎉 Temporal workflow system is ready!")
    print("\n📋 Next steps:")
    print("1. Your Flask app is running on http://localhost:5001")
    print("2. Visit http://localhost:5001/analytics to access the dashboard")
    print("3. Click 'Run Button Analysis' to start the workflow")
    print("4. Temporal UI is available at http://localhost:8080")
    
    print("\n🔄 Workflow Process:")
    print("1. Fetch GA4 data → 2. Process metrics → 3. Generate insights → 4. Save & notify")
    
    try:
        # Keep processes running
        print("\n⏳ Press Ctrl+C to stop all services...")
        server_process.wait()
        worker_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Stopping services...")
        server_process.terminate()
        worker_process.terminate()
        print("✅ Services stopped")

if __name__ == "__main__":
    main()
