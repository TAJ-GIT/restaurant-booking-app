# 🍽️ Restaurant Table Booking – 3-Tier Web App on AWS

This project is a scalable 3-tier web application hosted on AWS to manage restaurant table bookings.

## 🧱 Architecture

- **Frontend EC2** – Static HTML form hosted with Apache
- **Backend EC2** – Python Flask API to handle booking logic
- **Amazon RDS (MySQL)** – Stores booking data
- **Application Load Balancer (ALB)** – Routes traffic
- **Route 53** – Domain name for frontend

## 📁 Project Structure

restaurant-booking-app/
├── frontend/ # HTML form
├── backend/ # Flask app.py
├── infrastructure/ # Optional setup scripts or diagrams
├── README.md # Project documentation


## ✅ How to Use

1. Launch EC2 for frontend and backend
2. Deploy Flask app with connection to RDS
3. Point HTML form to backend via ALB
4. Access via Route 53 custom domain

## 🛠️ MySQL Workbench Usage

Before integrating with Amazon RDS, I used **MySQL Workbench** locally to test and manage the booking database.

### ✅ What I Did with MySQL Workbench:

- Designed the **initial schema** for the `restaurant` database.
- Created the `bookings` table:
  ```sql
  CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    date DATE
  );


