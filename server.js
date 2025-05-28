const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;
const DATA_FILE = path.join(__dirname, 'listings.json');

let listings = [];
try {
  listings = JSON.parse(fs.readFileSync(DATA_FILE, 'utf8'));
} catch (err) {
  console.error('Failed to load listings.json:', err);
  process.exit(1);
}

app.get('/api/listings', (req, res) => {
  let results = listings;
  const { minPrice, maxPrice, location } = req.query;

  if (minPrice) {
    const minParsed = parseInt(minPrice);
    results = results.filter(item => parseInt(item.price) >= minParsed);
  }
  if (maxPrice) {
    const maxParsed = parseInt(maxPrice);
    results = results.filter(item => parseInt(item.price) <= maxParsed);
  }
  if (location) {
    const loc = location.toLowerCase();
    results = results.filter(item =>
      item.location && item.location.toLowerCase().includes(loc)
    );
  }

  res.json(results);
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});