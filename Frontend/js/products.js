const BASE_URL = "http://localhost:8000";
const productList = document.getElementById("productList");

// Fetch products on page load
async function loadProducts() {
  const res = await fetch(`${BASE_URL}/showproducts`);
  const data = await res.json();

  productList.innerHTML = "";
  data.products.forEach(p => {
    const li = document.createElement("li");
    li.innerHTML = `
      <strong>${p.name}</strong> - $${p.price.toFixed(2)}
      <button onclick="deleteProduct('${p.name}')">Delete</button>
    `;
    productList.appendChild(li);
  });
}

// Add product
document.getElementById("addProductForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const name = document.getElementById("productName").value;
  const price = parseFloat(document.getElementById("productPrice").value);

  const res = await fetch(`${BASE_URL}/add-product`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, price })
  });

  const data = await res.json();
  alert(data.message || data.detail);
  loadProducts();
});

// Delete product
async function deleteProduct(name) {
  const res = await fetch(`${BASE_URL}/delete-product/${name}`, {
    method: "DELETE"
  });

  const data = await res.json();
  alert(data.message || data.detail);
  loadProducts();
}

// Load products on first visit
loadProducts();
