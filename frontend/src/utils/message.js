import Toastify from 'toastify-js'
import "toastify-js/src/toastify.css"

export default function showMessage(message, state='error', callback_func) {
    let background_color;
    if (state == 'error') {
        background_color = 'linear-gradient(to right, #ff5f6d, #ffc371)'
    } else {
        background_color = 'linear-gradient(to right, #00b09b, #96c93d)'
    }

    Toastify({
        text: message,
        duration: 2000,
        close: true,
        gravity: "top", // `top` or `bottom`
        position: "center", // `left`, `center` or `right`
        stopOnFocus: true, // Prevents dismissing of toast on hover
        style: {
            background: background_color,
        },
        callback: function(){
            if (!callback_func) return ;
            if (callback_func) {
                callback_func()
            }
        },
        onClick: function(){
            alert('debug onclick')
        } // Callback after click
        }).showToast();
}