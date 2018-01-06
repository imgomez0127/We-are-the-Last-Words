console.log("hello")
window.addEventListener("load",function(){
var read_more = document.getElementsByClassName("button-read-more");
var read_more_len = read_more.length;
console.log(read_more)
console.log(read_more_len)
    for(var i = 0; i < read_more_len; i++)
    {

        read_more[i].addEventListener("click", function(e){
            console.log(e.target.value);
        })
    }

})
