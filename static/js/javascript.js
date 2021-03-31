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