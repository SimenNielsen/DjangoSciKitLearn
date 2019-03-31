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
                db_request_after();
                if(callback !== undefined) callback(data);
            },
            error: function(data){
                db_request_error();
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
            if(type === "request"){
               db_request_before();
            }
            else if(type === "save"){
                db_save_before();
            }
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
    try{
        let status_elem = document.getElementById('db-status');
        let message =  "Requesting...";
        status_elem.classList.remove("alert-danger");
        status_elem.classList.add("alert-info");
    }
    catch(err){
        console.log(err.message)
    }
}
 function db_after(data){
     try{
        let status_elem = document.getElementById('db-status');
        let message = "Sucessful request.";
        status_elem.classList.remove("alert-info");
        status_elem.classList.add("alert-success");
     }
    catch(err){
        console.log(err.message)
    }
}
 function db_error(data){
     try{
        let status_elem = document.getElementById('db-status');
        let message = "Error";
        status_elem.classList.add("alert-danger");
     }
    catch(err){
        console.log(err.message)
    }
}