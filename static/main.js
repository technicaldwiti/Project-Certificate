var s = document.getElementById("search");
s.addEventListener("click",()=>{
    var roll_no = document.getElementById('roll_no').value;
    window.location.href = '/'+roll_no+'/';

    // console.log(roll_no);
});

var ip = document.getElementById("roll_no");
ip.addEventListener("keyup",function(event){
    console.log("Hello");
    if(event.keyCode === 13){
        s.click();
    }
});
