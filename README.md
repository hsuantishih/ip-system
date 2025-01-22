# IP Management System  

This repository contains an IP Management System designed to efficiently organize and manage IP addresses. The system supports two types of user roles: administrators and regular users, each with tailored functionalities.

## General Features  

### Login and Logout Functionality  
The system ensures secure login and logout processes, validated through the school database and robust authentication mechanisms. Access is restricted to current school faculty, staff, and students. User permissions are role-specific, ensuring appropriate access control.

<img src="https://github.com/user-attachments/assets/0c5d6992-bf26-42da-9082-da86e509a0ba" width="300" height="200">

### Search and Filter  
Users can search and filter IP addresses based on various criteria such as IP address, device name, and user name. This functionality enables quick identification of specific IP addresses and devices. 

<img src="https://github.com/user-attachments/assets/154913bc-3b40-4a01-8386-d17392b17cb4" width="500" height="100">

### Pop-up Notifications  
The system includes real-time pop-up notifications to inform users about important events, such as successful IP address assignments, requests, or system updates. This feature enhances user experience by providing instant feedback and alerts.

<img src="https://github.com/user-attachments/assets/d46562fe-7e02-40c8-8331-83b2fc6a6513" width="200" height="80">

### Interactive Dashboard  
The interactive dashboard leverages mouse hover and click events, allowing users to view detailed information such as IP address allocation, device types, and user information. This feature provides an intuitive understanding of IP address distribution and system data. 

<img src="https://github.com/user-attachments/assets/255a1e54-d11b-4117-85e5-1c1071b7216e" width="300" height="280">

## Administrator Features  

### IP Address Calculation  
Administrators can calculate IP addresses based on subnet masks, determining the number of available IP addresses within a subnet and allocating them efficiently. Occupied IP addresses are identified, and the system displays the number of available IP addresses to facilitate effective management.  

<table>
<tr>
<td> <img src="https://github.com/user-attachments/assets/39c0887c-cb68-4879-b234-1ff2355ac983" width="300" height="100"> </td>
<td> <img src="https://github.com/user-attachments/assets/79ca9893-6791-4f03-aacf-845f57e89315" width="380" height="100"> </td>
</tr>
</table>

### Assign IP Addresses  
Administrators can assign IP addresses to multiple users simultaneously. Allocation can be based on IP address ranges, user roles, and departments.

<img src="https://github.com/user-attachments/assets/7fa14dff-9504-4e83-bd9e-59de2027e5cf" width="500" height="100">

### Staff Query and Assignment  
Administrators can search for staff members and assign IP addresses accordingly. This feature ensures quick and accurate IP address allocation based on roles and departmental needs.  

<img src="https://github.com/user-attachments/assets/72f66a80-bc34-491c-b970-7078a69bbd74" width="700" height="100">

### Tracking and Management  
The system tracks and manages all allocated IP addresses and their associated devices. Records include MAC addresses, user names, comments, and device types, ensuring comprehensive management.  

<img src="https://github.com/user-attachments/assets/7c619dee-327f-4499-8109-beb910ec4bff" width="500" height="100">

### IP Address Pool Management  
Administrators can manage a pool of available IP addresses, enabling efficient organization and allocation of IP address ranges.  

<img src="https://github.com/user-attachments/assets/3dffae39-a679-4279-9cfb-6f43994900ed" width="500" height="100">

## User Features  

### IP Address Request  
Users can submit requests for IP address assignments. This feature ensures that users can request IP addresses based on their specific needs.  

<img src="https://github.com/user-attachments/assets/b093b08d-22b5-483a-b596-86b491e1b19e" width="600" height="100">

### CSV Import and Export  
Users can import and export data using CSV files for detailed IP address management. This functionality supports streamlined data handling for administrators.  

<img src="https://github.com/user-attachments/assets/77e64b6e-6302-47be-ab6b-a3d0af5468df" width="500" height="220">

## System Architecture  

### Flask Blueprints  
The application is modularized using Flask blueprints, facilitating organized development and maintenance of different components.  

<img src="https://github.com/user-attachments/assets/1e84ee04-9b19-40ec-bacc-8e47e2eb3b66" width="260" height="140">

### SOAP API Integration  
SOAP APIs are integrated to retrieve and update data from external sources. This enables seamless communication with external databases and services for data retrieval and updates.  

### MySQL Database  
The system uses MySQL for scalability and future expansion. The database is managed via SQLAlchemy ORM for efficient operations.  

<img src="https://github.com/user-attachments/assets/9c504d3b-43fa-4dba-9c92-d71e4fcd283a" width="300" height="180">

### Apache and mod_wsgi Deployment  
The application is deployed using Apache and mod_wsgi, ensuring stability and security.  

### Low Coupling Design  
A low-coupling design approach enhances code readability and maintainability, making the system easier to extend and debug.

<img src="https://github.com/user-attachments/assets/3de0fb5d-cf2d-4205-bd6a-956001a67f99" width="300" height="180">

### Unit Testing  
The system employs `pytest` for unit testing, utilizing a dedicated test database to prevent interference with the primary database.  


### Technologies Used  

- Python Flask  
- SOAP API  
- SQLAlchemy - MySQL  
- JavaScript  
- HTML/CSS  
- Apache - mod_wsgi  
