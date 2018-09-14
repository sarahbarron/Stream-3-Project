/* global $ Stripe*/
// Javascript for STRIPE payments

$(function() {

    // When we submit a payment form 
    $("#payment-form").submit(function() {
        // the current form we are taking information from
        var form = this;
        // credit card details - card number, expiry date, expiry year, security CVV number
        var card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            cvc: $("#id_cvv").val()
        };

        // create a Stripe Token function
        Stripe.createToken(card, function(status, response) {
            //  if it is a status 200 it has been successful
            if (status === 200) {
                // hide any errors
                $("#credit-card-errors").hide();
                // get the stripe id
                $("#id_stripe_id").val(response.id);

                //prevent cr card details from being submitted to our server only to spripes server
                $("#id_credit_card_number").removeAttr('name');
                $("#id_cvv").removeAttr('name');
                $("#id_expiry_month").removeAttr('name');
                $("#id_expiry_year").removeAttr('name');

                // submit the form
                form.submit();
            }
            // otherwise
            else {
                // show any stripe error messages
                $("#stripe-error-message").text(response.error.message);
                // show any credit card error messages
                $("#credit-card-errors").show();
                $("#validate_card_btn").attr("disabled", false);
            }

        });
        // return false
        return false;
    });
});