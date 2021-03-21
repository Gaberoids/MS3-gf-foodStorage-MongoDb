// login js template taken from https://bootsnipp.com/snippets/92gmX 

$(document).ready(function () {
    $('.login-info-box').fadeOut();
    $('.login-show').addClass('show-log-panel');
});


$('.login-reg-panel input[type="radio"]').on('change', function () {
    if ($('#log-login-show').is(':checked')) {
        $('.register-info-box').fadeOut();
        $('.login-info-box').fadeIn();

        $('.white-panel').addClass('right-log');
        $('.register-show').addClass('show-log-panel');
        $('.login-show').removeClass('show-log-panel');

    }
    else if ($('#log-reg-show').is(':checked')) {
        $('.register-info-box').fadeIn();
        $('.login-info-box').fadeOut();

        $('.white-panel').removeClass('right-log');

        $('.login-show').addClass('show-log-panel');
        $('.register-show').removeClass('show-log-panel');
    }
});

// Textarea max and alert from https://salesforce.stackexchange.com/questions/122481/how-to-show-error-message-when-maximum-limit-exceed-in-text-area-field

$(document).ready(function () {
    var maxLen = 400;

    $('#item_details').keypress(function (event) {
        var Length = $("#item_details").val().length;
        var AmountLeft = maxLen - Length;
        $('#txt-length-left').text('Number of characters left: ' + AmountLeft);
        if (Length >= maxLen) {
            if (event.which != 8) {
                $('#errMsg').text('... Textbox will not allow 400 or more characters.');
                return false;
            }
        }
    });

});