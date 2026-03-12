# Cross Market Analysis Dashboard

## Overview

The **Cross Market Analysis Dashboard** is a data analytics project that compares price movements across different financial markets.
It analyzes relationships between **cryptocurrency, stock indices, and crude oil prices** using a **Streamlit interactive dashboard**.

The project collects market data, stores it in a **MySQL database**, and performs cross-market comparisons to identify trends and correlations.

---

## Features

* 📊 Compare **Bitcoin, Oil, S&P 500, and Nifty 50**
* 📈 Visualize market trends using **interactive charts**
* 📅 Filter analysis using **custom date ranges**
* 🧮 Calculate **average prices between selected dates**
* 🔗 Perform **multi-table joins across markets**
* 📉 Cross-market trend comparison

---

## Tech Stack

| Technology   | Purpose               |
| ------------ | --------------------- |
| Python       | Data processing       |
| Streamlit    | Interactive dashboard |
| MySQL        | Database storage      |
| Pandas       | Data analysis         |
| Git & GitHub | Version control       |

---

## Database Schema

The project uses multiple tables to store market data:

### CRYPTOCURRENCIES

Stores metadata for cryptocurrencies.

### CRYPTO_PRICES

Stores daily cryptocurrency prices.

### STOCK_PRICES

Stores stock market index data including:

* Open
* High
* Low
* Close
* Volume

### OIL_PRICES

Stores crude oil prices by date.
---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/cross-market-analysis.git
```

Navigate to the project directory:

```bash
cd cross-market-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Dashboard

Run the Streamlit application:

```bash
./start_app.sh
```

The dashboard will open in your browser.

---

## Dashboard Capabilities

The Streamlit dashboard allows users to:

* View **market overview metrics**
* Compare **price movements across markets**
* Analyze **historical trends**
* Perform **date-based filtering**

---

## Future Improvements

* Add correlation heatmaps between markets
* Implement predictive analytics
* Add more assets (Gold, NASDAQ, Ethereum)
* Deploy the dashboard online

---

## Author

**Manoj Sivaraj**

---

## License

This project is for educational and analytical purposes.
