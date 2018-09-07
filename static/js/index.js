// NEWS & SPECIAL OFFERS CAROUSEL
$(document).ready(function() {

    // news and special offers carousel on index.html page 
    $('#myCarousel').carousel({
        interval: 10000
    })
});


// TREATMENTS FLIP CARDS
// when the mouse enters the card flip 180degs
$(".flip").mouseenter(function(event) {
    $(this).addClass("mousein");
});

// when the mouse exits the card flip back to 0
$(".flip").mouseleave(function(event) {
    $(this).removeClass("mousein");
});


// CONTACT SECTION GOOGLE MAPS SHOWING GINA'S LOCATION
function initMap() {
    // The location of Ginas Beauty Studio
    var ginas = { lat: 52.162543, lng: -7.152748 };
    // The map, centered at Gina's Beauty Studio
    var map = new google.maps.Map(
        document.getElementById('map'), { zoom: 18, center: ginas });
    // The marker, positioned at Gina's Beauty Studio
    var marker = new google.maps.Marker({ position: ginas, map: map });
}


// CONTACT FORM - SEND AN EMAIL USING EMAIL.JS
function sendMail(contactForm) {
    // send email
    emailjs.send("gmail", "ginas_beauty_studio", {
            "from_name": contactForm.name.value,
            "from_email": contactForm.email.value,
            "telephone": contactForm.telephone.value,
            "comment": contactForm.comment.value
        })
        .then(
            // Successfully sent email
            function(response) {
                console.log("SUCCESS", response.status, response.text);
                contactForm.reset();
                text = 'Your message has been sent I will be in touch with you as soon as possible, Thank You Gina.';
                document.getElementById("after-submit").innerHTML = text;
            },
            // error sending email
            function(error) {
                console.log("FAILED", error);
                text = 'There seems to be a problem sending your email, please try again shortly!'
                document.getElementById("after-submit").innerHTML = text;
            }

        );
    // stop the page reloading
    return false;
}
