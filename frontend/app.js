// Hämta produkter och visa på index.html
async function loadProducts() {
    const response = await fetch("http://127.0.0.1:8000/all_items");
    const products = await response.json();
    const container = document.getElementById("products");
    if (!container) return; // om vi inte är på index.html
  
    container.innerHTML = "";
    products.forEach(p => {
      const div = document.createElement("div");
      div.className = "product";
      div.innerHTML = `
        <h2>${p.name}</h2>
        <p>${p.price} kr</p>
        <button onclick="addToCart('${p.name}', ${p.price})">Lägg i kundvagn</button>
      `;
      container.appendChild(div);
    });
  }
  
  // Lägg till produkt i kundvagn (localStorage)
  function addToCart(name, price) {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    cart.push({ name, price });
    localStorage.setItem("cart", JSON.stringify(cart));
    alert(`${name} lades till i kundvagnen!`);
  }
  
  // Visa kundvagnen (cart.html)
  function renderCart() {
    const cartList = document.getElementById("cart");
    if (!cartList) return; // om vi inte är på cart.html
  
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    cartList.innerHTML = "";
    cart.forEach(item => {
      const li = document.createElement("li");
      li.textContent = `${item.name} – ${item.price} kr`;
      cartList.appendChild(li);
    });
  }
  
  // Kör när sidan laddas (bara om #products finns)
//   window.onload = loadProducts;