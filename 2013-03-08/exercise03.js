function capitalize (word) {
	c = word.charAt(0).toUpperCase();
	return c + word.slice(1);
}

function capitalize_whole (text) {
	var list = text.split(' ').map(capitalize);
	return list.join(' ');
}

var text = capitalize_whole("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
);

console.log(text);