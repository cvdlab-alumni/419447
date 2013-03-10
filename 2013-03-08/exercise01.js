function pusher(n) {
	var res = [];
	for (i=1; i<=n; i++)
		res.push(i);
	return res;
}

var numbers = pusher(10);

var numbers = numbers.filter(function (item) {
	return (item%2===0);
});

console.log(numbers);

numbers = numbers.map(function (item) {
	return (item*2);
});

console.log(numbers);

numbers = numbers.filter(function (item) {
	return (item%4===0);
});

console.log(numbers);

var result = numbers.reduce(function (prev, cur) {
	return (prev + cur);
});

console.log(result);