$(document).ready(function () {
    var stripeFormModule = $(".stripe-payment-form");
    var stripeToken = stripeFormModule.attr("data-token");
    var stripeTokenNextUrl = stripeFormModule.attr("data-next-url");
    var stripeDataBtn = stripeFormModule.attr("data-btn-title");

    var stripeTemplate = $.templates("#stripeTemplate");
    var stripeTemplateDataContext = {
        publish_key: stripeToken,
        next_url: stripeTokenNextUrl,
        label: "Payment Method",
        dataBtn: stripeDataBtn

    };
    var strpeTemplateHtml = stripeTemplate.render(stripeTemplateDataContext);
    stripeFormModule.html(strpeTemplateHtml);


    // Create a Stripe client.
    var pubKey = $("#payment-form").attr('data-token')
    var dataNextUrl = $("#payment-form").attr('data-next-url')

    var stripe = Stripe(pubKey);


    // Create an instance of Elements.
    var elements = stripe.elements();

    // Custom styling can be passed to options when creating an Element.
    // (Note that this demo uses a wider set of styles than the guide below.)
    var style = {
        base: {
            color: '#32325d',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#aab7c4'
            }
        },
        invalid: {
            color: '#fa755a',
            iconColor: '#fa755a'
        }
    };

    // Create an instance of the card Element.
    var card = elements.create('card', {style: style});

    // Add an instance of the card Element into the `card-element` <div>.
    card.mount('#card-element');

    // Handle real-time validation errors from the card Element.
    card.addEventListener('change', function (event) {
        var displayError = document.getElementById('card-errors');
        if (event.error) {
            displayError.textContent = event.error.message;
        } else {
            displayError.textContent = '';
        }
    });

    // Handle form submission.
    var form = document.getElementById('payment-form');
    form.addEventListener('submit', function (event) {
        event.preventDefault();

        stripe.createToken(card).then(function (result) {
            if (result.error) {
                // Inform the user if there was an error.
                var errorElement = document.getElementById('card-errors');
                errorElement.textContent = result.error.message;
            } else {
                // Send the token to your server.
                stripeTokenHandler(dataNextUrl, result.token);
            }
        });
    });

    // redirect to next own build function
    function redirectToNext(nextUrl, timeOut) {
        if (nextUrl) {
            setTimeout(function () {
                window.location.href = dataNextUrl
            }, timeOut)
        }
    }

    // Submit the form with the token ID.
    function stripeTokenHandler(dataNextUrl, token) {
        // Insert the token ID into the form so it gets submitted to the server
        // {#console.log(token.id)#}
        var paymentMethodEndpoint = "/payments/methods/create/"
        var data = {
            'token': token.id
        }
        $.ajax({
            data: data,
            url: paymentMethodEndpoint,
            method: "POST",
            success: function (data) {
                console.log(data);
                var successMsg = data.massege || "Success! your card was added";
                card.clear();
                if (dataNextUrl) {
                    successMsg = successMsg + "<br><i class='fa fa-spin fa-spinner'></i>Redirecting ...."
                }
                if ($.alert) {
                    $.alert(successMsg)
                } else {
                    alert(successMsg)
                }
                redirectToNext(dataNextUrl, 1500);
            },
            error: function (error) {
                console.log(error)
            }
        })

    }
});