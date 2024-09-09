console.log('Hello')
const currentlocation = location.href;
const menuItem = document.querySelectorAll('a');
const menuLength = menuItem.length

console.log('done')
for(let i = 0; i < menuLength; i++){
    console.log(menuItem[i].href)
    console.log('empty')
    if(menuItem[i].href === currentlocation){
        menuItem[i].classList.add("active")
    }
}




/*
const navBarEls = document.querySelectorAll('.nav-link');
navBarEls.forEach(navBarEl => {
    navBarEl.addEventListener('click', () => {
        document.querySelector('.active')?.classList.remove('active');
        navBarEl.classList.add('active')
        
    });
});
*/
