# Digizilla Odoo Module

## Description
A custom **Odoo 17** module designed for managing Digizilla records. This module implements a comprehensive management system with specific views, extensive field tracking, and custom reporting capabilities.

### Key Features
*   **Custom Data Management**: Dedicated model (`digizilla.digizilla`) to manage records with Name, Gender, Joining Date, Tags, and more.
*   **Full View Support**: Includes List, Form, and Kanban views for flexible data visualization.
*   **Audit & Tracking**: Inherits from `mail.thread` to provide full chatter support, logging all changes to key fields in the message history.
*   **Custom Reporting**: Built-in PDF report generation (`digizilla_report`) for printing record details.
*   **UI Customizations**: Includes custom JavaScript for specific view-level behavior modifications (e.g., hiding buttons).

---

## Installation Guide

### Prerequisites
*   Odoo 17.0 (Community or Enterprise)
*   Python 3.10+

### 1. Download the Module
Clone this repository into your custom addons folder or a directory of your choice.

**Linux / macOS / Windows Terminal:**
```bash
git clone https://github.com/your-username/digizilla-odoo-module.git
```

### 2. Configure `odoo.conf`
To make Odoo recognize the new module, you must add its parent directory to the `addons_path` in your Odoo configuration file (`odoo.conf` or `.odoorc`).

**A. Locate your config file:**
*   **Linux**: Typically `/etc/odoo/odoo.conf` or `~/.odoorc`.
*   **macOS**: Typically inside your installation folder or `~/.odoorc`.
*   **Windows**: Typically `C:\Program Files\Odoo 17.0\server\odoo.conf`.
*   **Development**: If running manually, it might be in your project root.

**B. Edit the `addons_path`:**
Open the file in a text editor and append the path to the folder **containing** the `Digizilla` folder.

**Example for Linux / macOS:**
```ini
[options]
admin_passwd = your_admin_password
db_host = False
db_port = False
db_user = odoo
db_password = False
; Add your custom path after a comma
addons_path = /usr/lib/python3/dist-packages/odoo/addons,/home/user/custom_addons
```

**Example for Windows:**
```ini
[options]
admin_passwd = your_admin_password
; ...
; Add your custom path after a comma (use absolute paths)
addons_path = C:\Program Files\Odoo 17.0\server\odoo\addons,C:\Users\YourUser\Documents\custom_addons
```
*> **Note:** The path should point to the **parent folder** that contains `Digizilla`, not the `Digizilla` folder itself.*

### 3. Restart Odoo
After saving the configuration file, you must restart the Odoo server for changes to take effect.

*   **Linux**: `sudo service odoo restart`
*   **Windows**: Open "Services" (Win+R > `services.msc`), right-click "Odoo", and select **Restart**.
*   **Manual**: Stop the running process (Ctrl+C) and start it again (e.g., `./odoo-bin -c odoo.conf`).

### 4. Install in Odoo Interface
1.  Log in to your Odoo instance as an Administrator.
2.  Enable **Developer Mode**:
    *   Go to **Settings**.
    *   Scroll to the bottom.
    *   Click **Activate the developer mode**.
3.  Go to the **Apps** menu.
4.  In the top menu bar, click **Update Apps List** and confirm.
5.  Search for **Digizilla** in the search bar.
6.  Click the **Activate** button to install the module.
