
const buttons = document.querySelectorAll(".object_item_title");

const handleClick = (event) => {
	let el = event.target;
	let el_p = el.parentElement.nextElementSibling.children;
	console.log(el.innerText);
	console.log(el_p);
}

buttons.forEach(button => {
	button.addEventListener('click', handleClick)
})

