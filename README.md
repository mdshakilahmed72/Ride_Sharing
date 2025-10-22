# 🚗 Ride Sharing Management System — Console Based (Python)

## 📖 Overview
A **console-based Ride Sharing Management System** built entirely with **Object-Oriented Programming (OOP) in Python**.  
It simulates real-life ride booking between **Riders** and **Drivers**, featuring **vehicle management**, **fare calculation**, **ride requests**, and **time tracking** — all using core Python classes and objects.

No external libraries required — perfect for learning **OOP concepts**, **class relationships**, and **inheritance** in Python.

---

## 🧠 Features

### 👤 Rider
- Request a ride by specifying destination and vehicle type  
- View assigned driver and ride details  
- Track ride start and end time  
- View total fare after ride completion  

### 🚘 Driver
- Register with vehicle type (Car, Bike, or CNG)  
- Accept ride requests automatically through the system  
- Start and end rides  
- Earn total income based on completed rides  

### 🚗 Vehicle
- Each vehicle has:
  - **Type** (Car / Bike / CNG)  
  - **Base Fare per KM**  
  - **Driver assignment**  

### 📦 Ride Request
- Rider sends a request to the system  
- Ride Matching system searches for the nearest available driver  
- Once matched, a new **Ride** object is created  
- Calculates estimated fare based on:
  - Distance  
  - Vehicle type  

### 🕒 Ride (Trip)
- Records:
  - **Start Location**
  - **End Location**
  - **Start Time**
  - **End Time**
  - **Estimated Fare**
- Fare automatically calculated using per–km rate  
- Shows total duration and cost at the end of the ride  

---

## 💰 Fare Calculation Formula
```python
Fare = Distance (km) × Fare_per_km[vehicle_type]


## 🖥️ How to Run

1. **Clone or Download** the project:
   ```bash
   git clone https://github.com/mdshakilahmed72/restaurant-management.git
   cd Restaurant_Management
   ```
2. **Run the app:**
   ```bash
   python main.py
   ```

   - Username: `Customer` → Place orders
   - Username: `Admin` → Manage food items  

---
