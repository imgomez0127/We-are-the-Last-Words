function switchImg(n){

    $("#img" + n).delay(4000).fadeOut(1000);
    if(n === 5){
        $("#img1" ).delay(4000).fadeIn(1000);
    }
    else{
        $("#img" + (n+1)).delay(4000).fadeIn(1000);
    }
    setTimeout(function(){
        if(n === 5){
            n = 1;
        }
        else{
            n++
        }
        switchImg(n);
    }, 5000);

}
window.addEventListener("load",function(){
        $("#img1").delay(1000).fadeOut(1000);
        $("#img2").delay(1000).fadeIn(1000);
        setTimeout(function(){
            switchImg(2);
        },2000)

    });
