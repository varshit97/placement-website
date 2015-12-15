var imgarr=new Array(5);
imgarr[0]=new Array();
imgarr[0].src="/Placements/static/images/image.jpg";
imgarr[1]=new Array();
imgarr[1].src="/Placements/static/images/image1.jpg";
imgarr[2]=new Array();
imgarr[2].src="/Placements/static/images/image2.png";
imgarr[3]=new Array();
imgarr[3].src="/Placements/static/images/image3.jpg";
imgarr[4]=new Array();
imgarr[4].src="/Placements/static/images/image4.jpg";
var i=0;
function images()
{
    document.getElementById("img").src=imgarr[i].src;
    i=(i+1)%5;
    setInterval(images(),1000);
}
images();
