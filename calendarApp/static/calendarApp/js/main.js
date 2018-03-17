function deleteEvent(event){

    var $event = jQuery(event);
    $event.parent().remove();

    var id = $event.data('id');

    jQuery.ajax({
        url: 'entry/delete/' + id,
        method: 'DELETE',
        beforeSend: function (xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrf_token)
        }
    })
}