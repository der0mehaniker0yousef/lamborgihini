
const baropen = document.getElementById('bar');
const navopen = document.getElementById('navbar');
const closenav = document.getElementById('close-nav');

baropen.addEventListener("click" , () => {
  navopen.classList.toggle("open")
})

if(closenav){
  closenav.addEventListener("click" , () => {
    navopen.classList.remove("open")
})}

/*
// slider Images
 const slider = document.querySelector('.landing-page');
 const arrowLeft = document.querySelector('.arrow-left')
 const arrowRight = document.querySelector('.arrow-right')
 const headingDes = document.querySelector('.heading-des')
 const headingP = document.querySelector('.heading-p')


const images = [
  "background1.jpg"  , "background2.jpg" , "background3.jpg" , "background4.jpg"
]

const detilesImages = [
  "HURÁCANSTO" , "Terzo Millennio" , "URAS S"
];

const descriptions = [
  "BASED ON A TRUE STORY",
  "CONCEPT CAR",
  "FOR BAR RAISERS ONLY",
]

// SLIDER ID
let id = 0;

// THE SLIDER FUNCTION
function slide(id) {
  slider.style.backgroundImage = `url(img/${images[id]})`

  slider.classList.add('image-fade');

  setTimeout(() => {
  slider.classList.remove('image-fade');
  }, 550);

  // CHANGE h2 DESCRIPTIONS
headingDes.innerText = detilesImages[id]
// CHANGE p DESCRIPTIONS
headingP.innerText = descriptions[id];

}

arrowLeft.addEventListener("click", () => {
  id--;

  if(id < 0) {
    id = images.length -1;
  }
  slide(id)
});

arrowRight.addEventListener("click" , () => {
  id++;

  if(id > images.length -1 ){
id = 0;
  }
  slide(id)
})
*/



const slider = document.querySelector('.landing-page');
 const arrowLeft = document.querySelector('.arrow-left');
 const arrowRight = document.querySelector('.arrow-right');
 const headingDes = document.querySelector('.heading-des');
 const description = document.querySelector('.heading-p');


const images = [
  "background1.jpg"  , "background2.jpg" , "background3.jpg" , "background4.jpg"
]

const headDescription = [
  "HURÁCANSTO" , "Terzo Millennio" , "URAS S" , "Terzo Millennio"
];

const descriptions = [
  "BASED ON A TRUE STORY",
  "CONCEPT CAR",
  "FOR BAR RAISERS ONLY",
  "CONCEPT CAR"
]

let id = 0;

function slide(id) {
  slider.style.backgroundImage = `url(img/${images[id]})`;
  slider.classList.add("image-fade");
  setTimeout(() => {
  slider.classList.remove("image-fade");
  }, 550);
  
  headingDes.innerText = headDescription[id]
// CHANGE p DESCRIPTIONS
description.innerText = descriptions[id];
}

arrowLeft.addEventListener("click" , () => {
  id--;
  if(id < 0){
   id = images.length - 1
  }
  slide(id)
})

arrowRight.addEventListener("click" , () => {
  id++;
  if(id > images.length -1){
id = 0;
  }
  slide(id)
})

const iconMsg = document.querySelector(".massage");
const popup = document.querySelector(".popup-massaeg");
const closeMsg = document.querySelector("#close-msg");


iconMsg.addEventListener("click" , () => {
  popup.classList.toggle("openmsg")
})

if(closeMsg){
  closeMsg.addEventListener("click" , () => {
    popup.classList.remove("openmsg")
  })}

  const closeSearch = document.querySelector("#close-search");
  const SearchIcon = document.querySelector(".search-icon");
  const searchArea = document.querySelector(".search-area");

  SearchIcon.addEventListener("click" , () => {
    searchArea.classList.toggle("open-search")
  })
  
  if(closeSearch){
    closeSearch.addEventListener("click" , () => {
      searchArea.classList.remove("open-search")
    })}


