let popup = document.getElementById("login");
let phone_number = document.getElementById("phone-number")
function signIn(){
    popup.classList.add("show-login");
}
function closeSignIn(){ 
    popup.classList.remove("show-login");
}

function phoneNumberLogin(){
    var phoneNumber = document.getElementById("phone-number").value;
    console.log(phoneNumber);
    var numberLength = phoneNumber.length;
    if(numberLength<10){
        return
    }
    else if(numberLength==10){
        //document.getElementById("continue").style.visibility = "visible"; 
        //document.getElementById("checkbox").checked = true;
        document.getElementById("iagree").style.visibility = "visible";
    }
}
function checkbox(){
    let cb = document.getElementById("checkbox")
    if(cb){
        
    }
}

function generateOtp(){
    var phoneNumber = document.getElementById("phone-number").value;
    console.log(phoneNumber)
    var nos = "0123456789"
    var num = ""
    for(var i = 0; i<6;i++){
        var n = Math.floor(Math.random()*6)
        num = num+nos[n]
    }
    console.log("The numbers are " + num);
    document.getElementById("login").style.display = "none";
    document.getElementById("otp-login").style.visibility = "visible";
}








// phone_number.addEventListener("click", continuee)
// function continuee(){
//     let xhr = new XMLHttpRequest();
//     xhr.open("GET", "bookmyshow.json" , true);
//     xhr.send()
//     xhr.onload = function(){
//         let result = xhr.responseText
//         result = JSON.parse(result)
//         console.log(result)
      
//     }
// }
