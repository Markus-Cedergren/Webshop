async function loadProducts() {
    const response = await fetch("/getProducts"); //ask the product-service to return all the products
    const products = await response.json(); //make into json
    const container = document.getElementById("products");
  
    container.innerHTML = "";
    products.forEach(p => {
      const div = document.createElement("div");
      div.className = "product";
      div.innerHTML = `
        <h2>${p.name}</h2>
        <p>${p.price} kr</p>
      `;
      container.appendChild(div);
    });
  }
  
async function login(){
  const usernameTextField = document.getElementById("name");
  const passwordTextField = document.getElementById("password");

  username = usernameTextField.value; 
  password = passwordTextField.value; 

  const response = await fetch("/login", {
    method:"POST",
    headers:{
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      name: username,
      password: password
    })
  });

  const result = await response.json();
  if(result.success){
    alert("Success")
  }else{
    alert("Wrong username or password");
  }

  usernameTextField.value = "";
  passwordTextField.value = "";
}


async function addProduct(){
  const productName = document.getElementById("productName");
  const productPrice = document.getElementById("productPrice");

  Pname = productName.value;
  Pprice = productPrice.value;

  const response = await fetch("/addProduct", {
    method: "POST",
    headers:{
      "Content-Type":"application/json"
    },
    body:JSON.stringify({
      name:Pname,
      price:Pprice
    })
  });
  const result = await response.json();
  if(result.success){
    alert("Sucess")
  }else{
    alert("Failed to add product")
  }

  productName.value = "";
  productPrice.value = "";

}


async function addCustomer(){
  
  const customerName = document.getElementById("newName");
  const customerPassword = document.getElementById("newPassword");

  newName = customerName.value;
  newPassword = customerPassword.value;


  const response = await fetch("/addAccount", {
    method:"POST",
    headers:{"Content-Type": "application/json"
  },
  body:JSON.stringify({
    name:newName,
    password:newPassword
  })
  });

const result = await response.json();
  if(result.success){
    alert("Success")
  }else{
    alert("Failed to add customer")
  }

  customerName.value = "";
  customerPassword.value = "";
}