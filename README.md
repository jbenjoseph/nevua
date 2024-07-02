# Nevua

## Overview

**Nevua** is an advanced platform designed for forecasting and monitoring disease outbreaks, with a specific focus on COVID-19. It leverages high-quality, third-party data to provide insights and predict potential hotspots by analyzing growth trends rather than total case counts. This project is a continuation of earlier efforts to track the pandemic, updated to meet the standards required for academic publication.

### Features

- **Interactive Dashboard**: Visualizes growth trends and identifies hotspots in real-time, helping public health officials and researchers prioritize response efforts.
- **Data-Driven Insights**: Utilizes data from the New York Times' COVID-19 reports.
- **Research-Ready**: Aims to provide a robust tool for epidemiological research and public health strategy development.

### Data Sources

- **COVID-19 Data**: Directly integrated with the New York Times COVID-19 dataset for U.S. counties and states.

## Installation

Nevua can be easily installed using Python's pip package manager. This package includes all necessary dependencies to run the application.

```bash
pip install nevua
```

## Usage

To start the Nevua application, use the following command:

```bash
nevua up
```

For production environments, it is recommended to run Nevua on a WSGI server. The application's WSGI entry is configured under the module `nevua.app:SERVER`, and uWSGI is suggested for robust performance.

### Example Command for WSGI Server:

```bash
uwsgi --http :8080 --wsgi-file nevua/app.py
```

## Development

To contribute to Nevua or customize it for specific needs, you can clone the repository and set up a development environment. This is ideal for developers looking to add features or integrate different datasets.

### Setup Development Environment:

```bash
git clone https://github.com/jbenjoseph/nevua.git
cd nevua
poetry install
```

## License and Credits

Nevua is Apache licensed and was initially forked from the `corona-dashboard` project developed by B.Next. It retains the same primary author, JJ Ben-Joseph.

## Additional Information

- **Predictive Model**: Utilizes AutoARIMA for forecasting, configured with custom hyperparameters to optimize performance.
- **Technologies Used**: Python, Dash by Plotly for the frontend, and Pandas for data manipulation.
- **Contribution**: Contributions are welcome! 