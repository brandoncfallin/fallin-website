// Add listener to each title element that has clippings attached
document.querySelectorAll('.titles-clip').forEach(item => {
    item.addEventListener('click', event => {
      //handle click
      openClippings(event.target.getAttribute("data-book-name"));
    })
  })

// Opens modal based on book title
function openClippings(bookName) {
    var modalID = "modal-" + bookName;
    var modal = document.getElementById(modalID);
    modal.showModal();
}