window.onload=function () {
	var chart=new CanvasJS.Chart("chartContainer",
	{
		title:{
			text:"Branches in IIIT-H"
		},
                animationEnabled:true,
		legend:{
			verticalAlign:"center",
			horizontalAlign:"left",
			fontSize:20,
			fontFamily:"Helvetica"
		},
		theme:"theme2",
		data:[
		{
			type:"pie",
			indexLabelFontFamily:"Garamond",
			indexLabelFontSize:20,
			startAngle:-20,
			showInLegend:true,
			toolTipContent:"{legendText} {y}%",
			dataPoints: [
				{  y: 63.24, legendText:"Computer Science", label: "Computer Science" },
				{  y: 20.16, legendText:"Electronics", label: "Electronics" },
				{  y: 9.67, legendText:"Humanities", label: "Humanities" },
				{  y: 6.67, legendText:"Natural Sciences" , label: "Natural Sciences"},
				{  y: 3.98, legendText:"Linguistics" , label: "Linguistics"}
			]
		}
		]
	});
	chart.render();
}
