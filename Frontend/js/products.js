try {
    document.getElementById('addProductForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const name = document.getElementById("productName").value;
        const price = document.getElementById("productprice").value;

        const post_function = await fetch('http://127.0.0.1:8000/addproduct', {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, price }),
        });

        const result = await post_function.json();
        document.getElementById('addmsg').innerText = result.message || result.detail;
    });
} catch (error) {
    console.error("Failed to add products:", error);
}


try {
    document.getElementById('GetProductForm').addEventListener('submit', async (e) => {
        e.preventDefault();

        const response = await fetch('http://127.0.0.1:8000/showproduct');
        const data = await response.json();

        const list = document.getElementById('productlist');
        list.innerHTML = '';

        // Assuming data.product is an array
        (data.product || []).forEach(product => {
            const item = document.createElement('li');
            item.textContent = `${product.name} - Rs.${product.price}`;
            list.appendChild(item);
        });
    });
} catch (error) {
    console.error('Failed to load Products:', error);
}


try {
    document.getElementById('UpdateProductForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const name = document.getElementById("productName").value;
        const price = document.getElementById("productprice").value;

        const post_function = await fetch('http://127.0.0.1:8000/updateproduct', {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, price }),
        });

        const result = await post_function.json();
        document.getElementById('updatemsg').innerText = result.message || result.detail;
    });
} catch (error) {
    console.error('Failed to Update Products:', error);
}


try {
    document.getElementById('RemoveProductForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const name = document.getElementById("productName").value;
        const price = document.getElementById("productprice").value;

        const post_function = await fetch('http://127.0.0.1:8000/deleteproduct', {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, price }),
        });

        const result = await post_function.json();
        document.getElementById('removemsg').innerText = result.message || result.detail;
    });
} catch (error) {
    console.error('Failed to Remove Products:', error);
}
