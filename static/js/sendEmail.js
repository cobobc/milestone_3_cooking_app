function sendMail(registerEmail) {
    emailjs.send("service_7fq8vte","template_27oewgi", {
        "new_user": registerEmail.username.value,
        "to_email": registerEmail.email.value,
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return;
}