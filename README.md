# Restaurant Order Delivery System

Welcome to the **Restaurant Order Delivery System**! This application leverages the Observer design pattern and RabbitMQ to efficiently handle order deliveries from restaurants to delivery agents.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

In the fast-paced world of food delivery, timely communication between restaurants and delivery agents is crucial. This application uses the Observer pattern, allowing multiple delivery agents to subscribe to order updates, ensuring they receive real-time notifications when a new order is placed.

## Features

- **Real-time Order Notifications**: Delivery agents receive instant updates on new orders.
- **Scalable Architecture**: Easily add more delivery agents or restaurants without significant code changes.
- **Robust Messaging**: Utilizes RabbitMQ for reliable message delivery.
- **User-friendly Interface**: Simple and intuitive UI for both restaurant staff and delivery agents.

## Technologies Used

- **RabbitMQ**: For handling message queuing and delivery.
- **Observer Design Pattern**: To manage the relationship between orders and delivery agents.
- **Python Programming Language**: Python
- **Frameworks Used**: Flask

## Getting Started

To get a local copy up and running, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JavadTorabiKh/RestaurantOrderDeliverySystem.git
   ```

2. **Install dependencies**:

    Navigate to the project directory and install the necessary packages:

    ```bash
    cd restaurant-order-delivery-system
    # Replace with your dependency manager
    pip install -r requirements.txt
    ```

3. **Set up RabbitMQ**:
    Ensure RabbitMQ is installed and running on your machine. [You can follow the official RabbitMQ installation guide](https://www.rabbitmq.com/docs/download).

4. **Run the application**:

    Start the application with the following command:

    ```bash
    python producer.py
    ```

## Usage

1. Place an Order: Use the restaurant interface to place a new order.
2. Notify Delivery Agents: The system will automatically notify all subscribed delivery agents.
3. Track Deliveries: Delivery agents can view and accept orders in real time.


## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repo.
2. Create a new branch (git checkout -b feature/YourFeature).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature/YourFeature).
6. Open a Pull Request.


## License
Distributed under the MIT License. See LICENSE for more information.


### Thank you for checking out the Restaurant Order Delivery System! We hope you find it useful and efficient.