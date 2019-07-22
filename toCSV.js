var fs = require("fs");

file = fs.readFile('hdbData_22072019.txt', (err, data) => {
	if(err) throw err;
	
	var res = JSON.parse(data);//.slice(0,3);
	
	res = res.map((x)=>{
		return Object.values(x).join("\t");
	});
	res = res.join("\n");
	console.log(res);
	
	fs.writeFile("hdbData_22072019.tsv",res,function(err){console.log("Saved.");});
});