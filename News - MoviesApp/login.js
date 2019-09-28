$(document).ready(function(){

    sessionStorage.setItem("username", "user");
    sessionStorage.setItem("passwords", "user"); //or 'uaspti'

    $('.btnSubmit').click(function(){
        if ($("#inputUsername").val() == '' && $("#inputPassword").val() == '')
        {
            alert("Wrong combination of Username and/or Password");
        }
        else if($("#inputUsername").val() == sessionStorage.getItem("username") && $("#inputPassword").val() == sessionStorage.getItem("passwords"))
        {
            alert("Welcome back");
            sessionStorage.clear("username");
            sessionStorage.clear("passwords");
            //direct ke halaman utama disini
        }
        else if ($("#inputUsername").val() != sessionStorage.getItem("username") || $("#inputPassword").val() != sessionStorage.getItem("passwords"))
        {
            alert("Wrong combination of Username and/or Password");
        }
    })
});