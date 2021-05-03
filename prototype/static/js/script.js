const btnHamburger = document.querySelector('#btnHamburger');
const body = document.querySelector('body');
const header = document.querySelector('.header');
const overlay = document.querySelector('.overlay');
const fadeStuffs = document.querySelectorAll('.hasFade');

btnHamburger.addEventListener('click', function(){
    console.log('open hamburger menu');

    //closing
    if(header.classList.contains('open')) {
        body.classList.remove('noscroll');
        header.classList.remove('open');
        fadeStuffs.forEach(function(element){
            element.classList.remove('fadeIn');
            element.classList.add('fadeOut');

        });
    }
    //opening
    else {
        body.classList.add('noscroll');
        header.classList.add('open');
        fadeStuffs.forEach(function(element){
            element.classList.remove('fadeOut');
            element.classList.add('fadeIn');
        });
    }
});
