const btnHamburger = document.querySelector('#btnHamburger');
const header = document.querySelector('.header');
const overlay = document.querySelector('.overlay');
const fadeStuffs = document.querySelectorAll('.hasFade');

btnHamburger.addEventListener('click', function(){
    console.log('open hamburger menu');

    //closing
    if(header.classList.contains('open')) {
        header.classList.remove('open');
        overlay.classList.remove('fadeIn');
        overlay.classList.add('fadeOut');
    }
    //opening
    else {
        header.classList.add('open');
        fadeStuffs.forEach(function(element){
            element.classList.remove('fadeOut');
            element.classList.add('fadeIn');
        });
    }
});
