function pusher (n) {
	var numbers = [];
	for (i=0; i<n; i++) {
		numbers.push(Math.floor(Math.random()*100))
	}
	return numbers;
}

numbers = pusher(10);

console.log(numbers);

numbers = numbers.filter(function (item) {
	return (item%2!==0);
})

console.log(numbers);

numbers.sort(function (a,b) {
	return a - b;
});

console.log(numbers);