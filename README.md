# MongoDB Installation Guide (Windows)

Follow these steps to install MongoDB on your Windows machine using the `mongo_installation_windows.ps1` script provided:

### Step 1: Run the Installation Script

1. **Download the Installation Script:**
   - Download the PowerShell script (`mongo_installation_windows.ps1`) provided in this repository.

2. **Run the Script:**
   - Open PowerShell with administrative privileges.
   - Navigate to the directory where `mongo_installation_windows.ps1` is located.
   - Run the script by executing the following command:
     ```
     .\mongo_installation_windows.ps1
     ```
   - This script will download and install MongoDB on your system.

### Step 2: Add MongoDB Bin Directory to Environmental Variables

1. **Open Environment Variables Settings:**
   - Right-click on **This PC** or **Computer** on your desktop or File Explorer.
   - Click on **Properties**.
   - Click on **Advanced system settings**.
   - In the System Properties window, click on **Environment Variables**.

2. **Modify System Variables:**
   - In the Environment Variables window, under **System variables**, find the variable named **Path** and select it.
   - Click on **Edit**.

3. **Add MongoDB Bin Directory:**
   - Click on **New** and add the following path (adjust based on your MongoDB installation directory):
     ```
     C:\MongoDB\mongodb-win32-x86_64-windows-5.0.27\bin
     ```
   - Click **OK** to save the changes.

4. **Confirm:**
   - Click **OK** in the Environment Variables window to close it.
   - Click **OK** in the System Properties window to close it.

### Step 3: Confirm MongoDB Installation

1. **Open Command Prompt:**
   - Open Command Prompt (cmd.exe).

2. **Check MongoDB Version:**
   - Type the following command to check the installed MongoDB version:
     ```
     mongod --version
     ```
   - Press **Enter**.
   - You should see output similar to:
     ```
     MongoDB server version: 6.0.15
     ```
   - This confirms that MongoDB has been successfully installed and configured on your Windows system.

---


