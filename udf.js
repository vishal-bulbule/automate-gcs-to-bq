function transform(line) {
    var values = line.split(',');

    // Check if the line is the header by checking the first value
    if (values[0].toLowerCase() === 'id') {
        return null; // Ignore the header row
    }

    var obj = new Object();
    obj.id = values[0];
    obj.name = values[1];
    obj.email = values[2];
    obj.age = values[3];
    obj.city = values[4];
    var jsonString = JSON.stringify(obj);
    return jsonString;
}
