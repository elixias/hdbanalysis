const request = require("superagent");
var cheerio = require("cheerio");
var fs = require("fs");

//var locations = ["Bedok"];
var locations = ["Ang Mo Kio","Bedok","Bishan","Bukit Batok","Bukit Merah","Bukit Panjang","Bukit Timah","Central Area","Choa Chu Kang","Clementi","Geylang","Hougang","Jurong East","Jurong West","Kallang/Whampoa","Marine Parade","Pasir Ris","Punggol","Queenstown","Sembawang","Sengkang","Serangoon","Tampines","Toa Payoh","Woodlands","Yishun"];

async function getData(loc){

	var url = "https://www.squarefoot.com.sg/latest-transactions/sale/hdb/4-room?town="+loc;
	var result = await request.get(url);
	console.log(result.text);
		var td = []
		
		//get table rows:
		var $ = cheerio.load(result.text);
		var r = $('.minimalist.sortable tbody').children();
		
		//extract and insert data
		r.each(function(i,elem){
			td.push(
				{
					date:$("td:nth-child(1)",this).text(),
					town:$("td:nth-child(2)",this).text(),
					projectName:$("td:nth-child(3)",this).text(),
					storey:$("td:nth-child(4)",this).text(),
					propertyType:$("td:nth-child(5)",this).text(),
					model:$("td:nth-child(6)",this).text(),
					tenure:$("td:nth-child(7)",this).text(),
					areasqm:$("td:nth-child(8)",this).text(),
					pricepsf:$("td:nth-child(9)",this).text(),
					price:$("td:nth-child(10)",this).text()
				}
			)
		});
		return td;

}

var extractedData = [];
	
async function start(){
	for(var i = 0;i<locations.length;i++){
	
	//get data
	townData = await getData(locations[i]);
	
	//push townData into extractedData
	extractedData = [...extractedData,...townData];
	
	}
	fs.writeFile("result.txt",JSON.stringify(extractedData),function(err){console.log("Saved.");});
}
start()

//write to file:

