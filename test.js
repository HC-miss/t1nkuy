function Unicode2Native() {
    var a = '&#243;';
	var code = a.match(/&#(\d+);/g); //&#243;
	for (var i=0; i<code.length; i++)  //[ '&#243;' ]
		$("#a_source").val($("#a_source").val() + String.fromCharCode(code[i].replace(/[&#;]/g, '')));
}