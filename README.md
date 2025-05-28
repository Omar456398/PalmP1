
# Edifice Property Scraper & API

This project helps collect hidden property deals from the Edifice Group’s public listings page, it's made it two parts.

## Part 1. The Python web scraper

### Description
A lightweight scraper that gets title, price, location, and detail link of each listing from:

🔗 https://repossessedhousesforsale.com/properties/

### Setup

```bash
pip install -r requirements.txt
```

### Run

```bash
python scraper.py
```

Output of the scraper is saved to `listings.json`.

---

## Part 2. The Node.js Express API

### Description
A simple REST API that serves data from `listings.json` and allows filtering by:

- `minPrice`
- `maxPrice`
- `location`

### Setup

```bash
npm install
```

### Run

```bash
node server.js
```

### Example Requests

- Get all listings:
  ```
  curl http://localhost:3000/api/listings
  ```

- Filter by price:
  ```
  curl "http://localhost:3000/api/listings?minPrice=100000&maxPrice=300000"
  ```

- Filter by location:
  ```
  curl "http://localhost:3000/api/listings?location=CM1"
  ```

---

## Sample Output (listings.json)

```json
[
  {
    "title": "3 Bedroom House for Sale",
    "price": "175000",
    "location": "CM1",
    "link": "https://repossessedhousesforsale.com/properties/..."
  },
  ...
]
```
