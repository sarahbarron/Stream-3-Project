// Email.js contact form on index.html page 
function sendMail(contactForm) {
    emailjs.send("gmail", "ginas_beauty_studio", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "telephone": contactForm.telephone.value,
        "comment": contactForm.comment.value
    })
    .then(
        function(response) {
            console.log("SUCCESS",response.status, response.text);
            contactForm.reset();
             alert('Your mail is sent!');
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}