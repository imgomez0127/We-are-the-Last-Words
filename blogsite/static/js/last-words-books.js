window.addEventListener("load",function(){
    var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
    if(w >= 800){
    bookNode = document.getElementsByClassName("book");
    divNode = document.getElementsByClassName("book-wrapper")
    postOverlayNode = document.getElementsByClassName("book-overlay")
    bookNodeLength = bookNode.length;
    for(var i = 0; i < bookNodeLength; i++){
        divNode[i].addEventListener("mouseover", function(e){
            if(e.target.tagName === 'P'){
                e.target.style.opacity = 1
                e.target.style.transition = 'opacity .5s'
            }
        });
        divNode[i].addEventListener("mouseout", function(e){
            if(e.target.tagName === 'P'){
                e.target.style.opacity = 0
                e.target.style.transition = 'opacity .5s'
            }
        });
        }
        }

});