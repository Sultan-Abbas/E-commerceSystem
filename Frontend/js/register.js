document.body.getElementById('registerForm').addEventlistener('submit',async (e) => { 
    e.defaultPrevent()
    const name = document.body.getElementById("username").value
    const password = document.body.getElementById("password").value
    const post_function= await fetch('http://127.0.0.1:8000/register',{
        method:"POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({name,password}),
    });
    const result = await post_function.json
    document.getElementById('message').innerText(result.message || result.detail)
 });
