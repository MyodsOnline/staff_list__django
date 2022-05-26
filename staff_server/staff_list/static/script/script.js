
const buttons = document.querySelectorAll(".checker");
const staffs = document.querySelectorAll("input");


const handleClickTitle = (event) => {
	let el = event.target;
	el.classList.toggle('fa-angle-down')
	el.classList.toggle('fa-angle-up')
	let el_li = el.parentElement.parentElement.nextElementSibling.children;
    for (let el_li_item of el_li) {
		if (el_li_item.classList.contains('checked')) {
			
		} else {
			el_li_item.classList.toggle('ok');
		}
	}
	// console.log(el.innerText);
}

const handleClickStaff = (event) => {
	let staff_el = event.target;
	// console.log(staff_el)
	let staff_el_li = staff_el.parentElement.parentElement;
	// console.log(staff_el_li)
	let staff_el_ul = staff_el_li.parentElement.children;
	// console.log(staff_el_ul);
	staff_el_li.classList.toggle('checked')
}

buttons.forEach(button => {
	button.addEventListener('click', handleClickTitle)
})

staffs.forEach(staff => {
	staff.addEventListener('click', handleClickStaff)
})

