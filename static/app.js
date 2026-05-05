async function fetchUser() {
    const username = document.getElementById("username").value;

    const res = await fetch(`/fetch_user/${username}`);
    const data = await res.json();

    const resultDiv = document.getElementById("result");

    if (data.error) {
        resultDiv.innerHTML = `<p style="color:red;">${data.error}</p>`;
        return;
    }

    resultDiv.innerHTML = `
        <div class="user-card">
            <h3>${data.username}</h3>
            <p>Repos: ${data.repos}</p>
            <p>Followers: ${data.followers}</p>
        </div>
    `;
}

async function loadUsers() {
    const res = await fetch("/users");
    const data = await res.json();

    const usersDiv = document.getElementById("users");
    usersDiv.innerHTML = "";

    data.forEach(user => {
        usersDiv.innerHTML += `
            <div class="user-card">
                <h3>${user.username}</h3>
                <p>Repos: ${user.repos}</p>
                <p>Followers: ${user.followers}</p>
            </div>
        `;
    });
}