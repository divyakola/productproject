function getDateTime(){
        var dt=new Date();
        document.getElementById("dt").innerHTML=dt;
     }
setInterval(getDateTime,1000);