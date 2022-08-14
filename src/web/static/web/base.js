document.querySelector('#navButton').addEventListener('click', function (e){
	e.preventDefault();
	console.log("clicked");
	let mobileMenu = document.querySelector("#mobileMenu");
	let header = document.querySelector("#header");
	if (!mobileMenu.classList.contains("show")){
		mobileMenu.classList.add("show");
	}
	else {
		mobileMenu.classList.remove("show");
	}
});


function onOpenedMenuWindowScroll() {
	window.scrollTo(0, 0);
}

window.onscroll = function() {myFunction()};

const header = document.querySelector("#header");
const afterLogo = document.querySelector("#afterLogo");
const logoText = document.querySelector("#logoText");

const sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset > 10) {
    let clientWidth = document.body.clientWidth;
    if(clientWidth >= 991){
	    header.classList.add("h-80");
	    if (clientWidth <= 1250) {
		    afterLogo.classList.add("hide");
	    }
    }
  }
  else {
  	let clientWidth = document.body.clientWidth;
  	if(clientWidth >= 991){
	    header.classList.remove("h-80");
	    if (clientWidth <= 1250) {
		    afterLogo.classList.remove("hide");
	    }
    }
  }
}