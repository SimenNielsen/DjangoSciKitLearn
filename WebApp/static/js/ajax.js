class Data_Provider{
    constructor(pathname){
        this.url = pathname;
    }
    
    ajax_request(args, callback){
        this.ajax_setup();
        
        $.ajax({
            url: this.url,
            type: "POST",
            data: args,
            dataType: 'json',
            success: function(data){
                db_after();
                if(callback !== undefined) callback(data);
            },
            error: function(data){
                db_error();
            },
        });
    }
    ajax_setup(type, enable_async=true){
        enable_async = (enable_async === undefined) ? true : enable_async;
        $.ajaxSetup({
        async: enable_async,
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
            db_before();
        }
        });
    }
}

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
// these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function db_before(data){
    console.log('Requesting...')
}
 function db_after(data){
     console.log('Requesting successful')
}
 function db_error(data){
     console.log('Requesting error')
}