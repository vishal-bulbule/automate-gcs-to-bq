function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.id = values[0];
    obj.name = values[1];
    obj.email = values[2];
    obj.age = values[3];
    obj.city = values[4];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }