// Add listener to each title element that has clippings attached
document.querySelectorAll('.titles-clip').forEach(item => {
    item.addEventListener('click', event => {
      event.preventDefault();
      openClippings(event.target.getAttribute("data-book-name"));
    })
  })

// Opens modal based on book title
function openClippings(bookName) {
    var modalID = "modal-" + bookName;
    var modal = document.getElementById(modalID);

    // Lock scroll while dialog is open
    document.body.style.overflow = 'hidden';

    modal.showModal();

    // Restore scroll when dialog closes
    modal.addEventListener('close', function onClose() {
        document.body.style.overflow = '';
        modal.removeEventListener('close', onClose);
    });
}