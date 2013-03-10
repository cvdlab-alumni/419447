function select (data, key, values) {
	return data.filter(function (item_data) {
		return values.some(function (item_values) {
			return item_data[key] === item_values;
		})
	})
}

var data = [
  {id:'01', name:'duffy'},
  {id:'02', name:'michey'},
  {id:'03', name:'donald'},
  {id:'04', name:'goofy'},
  {id:'05', name:'minnie'},
  {id:'06', name:'scrooge'}
];
var key = 'name';
var values = ['goofy', 'scrooge'];

console.log(select(data, key, values));