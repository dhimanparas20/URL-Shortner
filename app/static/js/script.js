// Function to get CSRF token from the cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const baseUrl = window.location.origin + '/';
const csrftoken = getCookie('csrftoken');
$('#url-form').on('submit', function(e) {
    e.preventDefault();
    const long_url = $('#long_url').val();
    $.ajax({
        url: '/api/urls/',
        type: 'POST',
        data: JSON.stringify({ long_url: long_url }),
        contentType: 'application/json',
        headers: { 'X-CSRFToken': csrftoken }, // Include CSRF token in the request
        success: function(response) {
            $('#shortened-url').html(`KEY: <a href="/${response.short_url}" target="_blank">${response.short_url}</a>`);
            $('#full_short-url').html(`Complete URL: <a href="${baseUrl}${response.short_url}" target="_blank">${baseUrl}${response.short_url}</a>`);
        },
        error: function(xhr, status, error) {
            // Display the error message to the user
            const errorMessage = xhr.responseJSON?.detail || "Invalid URL. Please check the URL and try again";
            $('#shortened-url').html(`<div class="alert alert-danger" role="alert">${errorMessage}</div>`);
            $('#full_short-url').empty();
        }
    });
});

// Clear the output fields on reset
$('#url-form').on('reset', function() {
    $('#shortened-url').empty();
    $('#full_short-url').empty();
});