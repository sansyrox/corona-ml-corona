var word=$('.quote span');var container=$('#preloader');function completeLoading(){word.each(function(index){var y=Math.floor(Math.random()*200)-100;$(this).css('transform','translateY('+y+'px)')})}
function displayMap(){$('#map').css('display','block');$('.tab').css('display','block');var dv=document.createElement("div");dv.id="map"
document.body.appendChild(dv);mapboxgl.accessToken='pk.eyJ1Ijoic2Fuc3lyb3giLCJhIjoiY2s3dnZrbmFvMWRhdTNmc2ZvcmdoN2ZzcSJ9.6QHhyKVX3aybyR0AgKmjyQ';var map=new mapboxgl.Map({container:'map',style:'mapbox://styles/mapbox/dark-v10',center:[0,0.404374],zoom:1});map.on('load',function(){map.addSource('trees',{type:'geojson',data:'./data.geojson'});map.addLayer({id:'trees-heat',type:'heatmap',source:'trees',maxzoom:15,paint:{'heatmap-weight':{property:'dbh',type:'exponential',stops:[[1,0],[62,1]]},'heatmap-intensity':{stops:[[11,1],[15,3]]},'heatmap-color':['interpolate',['linear'],['heatmap-density'],0,'rgba(236,222,239,0)',0.2,'rgb(208,209,230)',0.4,'rgb(166,189,219)',0.6,'rgb(103,169,207)',0.8,'rgb(28,144,153)'],'heatmap-radius':{stops:[[11,15],[15,20]]},'heatmap-opacity':{default:1,stops:[[14,1],[15,0]]},}},'waterway-label')})}
setTimeout(function(){container.fadeOut().delay(3000);displayMap()},3000);const second=1000,minute=second*60,hour=minute*60,day=hour*24;let countDown=new Date('Jul 21, 2020 00:00:00').getTime(),x=setInterval(function(){let now=new Date().getTime(),distance=countDown-now;document.getElementById('days').innerText=Math.floor(distance/(day)),document.getElementById('hours').innerText=Math.floor((distance%(day))/(hour)),document.getElementById('minutes').innerText=Math.floor((distance%(hour))/(minute)),document.getElementById('seconds').innerText=Math.floor((distance%(minute))/second)},second)
