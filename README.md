# Yahoo Finance API

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/vkmguy/yahoo_finance_api.git
    cd yahoo_finance_api
    ```

3. **Build and start the services:**

    ```bash
    docker-compose up --build
    ```

   This command will build the Docker images and start the services.

4. **Access your application:**

    - Web App: [http://localhost:8000](http://localhost:8000)
    - Django Admin: [http://localhost:8000/admin](http://localhost:8000/admin) (username: admin, password: admin)
    - Apache Kafka: Access the Kafka container for further configuration

5. **To stop the services, press `Ctrl + C` in the terminal where `docker-compose` is running.**

## Services

### Django Web App

The Django web app allows you to interact with the Stock Market ML model.
Visit [http://localhost:8000/](http://localhost:8000/api) to access the web app.

- GET request for Historical Data: [http://localhost:8000/api/historical-data/{{marketSymbol}}](http://localhost:8000/api/historical-data/{{marketSymbol}})
- GET request to get date ranged Data: [http://localhost:8000/api/historical-data/{{marketSymbol}}/date-range/{{startDate}}/{{endDate}}](http://localhost:8000/api/historical-data/{{marketSymbol}}/date-range/{{startDate}}/{{endDate}})

## Troubleshooting

- If you encounter issues, check the logs of individual containers for more details.

## License

This project is licensed under the [MIT License](LICENSE).
