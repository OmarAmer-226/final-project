
document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get username and password values
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Here you can perform validation or send the data to the server for authentication
    // For simplicity, let's just log the values to the console
    console.log('Username:', username);
    console.log('Password:', password);
});
