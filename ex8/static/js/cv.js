// wellcome haeder//

const d = new Date();
console.log(d);
var h = d.getHours();

if(h<12){
    greeting = "good morning";
}else if(h<17){
    greeting = "good afternoon";
} else{
    greeting = "good evening";
}; console.log(greeting);

function greet(){
    document.getElementById("P").innerHTML=greeting;
};

// img cat//
function catpic(){    
    document.getElementById("item3").style.backgroundImage = "url('pics/EX2_pic.jpg')";
    document.getElementById("buttoncat").style.display = "none"
};


// -----------api iq---------//
function myFunction() {
    const inpObj = document.getElementById("iq");
    if (inpObj.value != 20) {
         document.getElementById("demo").innerHTML = "wrong input   ";
    } else {
        document.getElementById("demo").innerHTML = "Input OK";
    }
}
