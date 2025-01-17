
document.getElementById('collapse-btn').addEventListener('click', function () {
    document.querySelector('.left-menu').classList.toggle('collapsed');
  });

  
function adjustPageSize() {
    const screenWidth = window.innerWidth;
    const body = document.body;
  
    if (screenWidth >= 992 && screenWidth <= 1600) {
      body.style.transform = 'scale(0.9)';
    } else if (screenWidth >= 700 && screenWidth <= 767) {
      body.style.transform = 'scale(0.8)';
    } else if (screenWidth >= 600 && screenWidth <= 700) {
      body.style.transform = 'scale(0.75)';
    } else if (screenWidth <= 600) {
      body.style.transform = 'scale(0.5)';
    } else {
      body.style.transform = 'scale(1)';
    }
  }
  
  window.addEventListener('resize', adjustPageSize);
  adjustPageSize(); 