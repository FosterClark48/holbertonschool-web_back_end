// Task 12 - In stock?

import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();

// Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

// Data
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

// Set initial stock in Redis
listProducts.forEach(item => {
  client.set(`item.${item.id}`, item.stock);
});

// Functions
function getItemById(id) {
  return listProducts.find(item => item.id === id);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock) : null;
}

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

// Routes
app.get('/list_products', (req, res) => {
  res.json(listProducts.map(item => ({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
  })));
});

app.get('/list_products/:itemId', async (req, res) => {
  const item = getItemById(parseInt(req.params.itemId));
  if (!item) {
    return res.status(404).json({ status: 'Product not found' });
  }
  const currentStock = await getCurrentReservedStockById(item.id) || item.stock;
  res.json({ ...item, currentQuantity: currentStock });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const item = getItemById(parseInt(req.params.itemId));
  if(!item) {
    return res.status(404).json({ status: 'Product not found' });
  }
  const currentStock = await getCurrentReservedStockById(item.id) || item.stock;
  if (currentStock <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: item.id });
  }
  reserveStockById(item.id, currentStock - 1);
  res.json({ status: 'Reservation confirmed', itemId: item.id });
});

// Start server
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
