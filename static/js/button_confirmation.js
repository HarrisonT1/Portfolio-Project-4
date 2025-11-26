document.addEventListener("DOMContentLoaded", function() {
    const cancelButtons = document.querySelectorAll(".cancel-btn")

    cancelButtons.forEach(button => {
        button.addEventListener("click", function(event) {
            const confirmation = confirm("Are you sure you want to delete this, this action is irreversible");
            if(!confirmation) {
                event.preventDefault();
            }
        })
    })
})