const vh = window.innerHeight / 100;
$(document).ready(function(){
    $(window).scroll(function(){  
        if ($(window).scrollTop() > 50*vh &&  $(window).scrollTop() < (90*vh*3 + 50*vh)){
            $("#board").css("color", "#000");
            $(".pointBtnl").css("background", "#ffffff00");
            $(".pointBtnl").css("border-color", "#000");
            $(".line").css("background", "#000");
        }
        else{
            $("#board").css("color", "#fff");
            $(".pointBtnl").css("background", "#ffffff00");
            $(".pointBtnl").css("border-color", "#fff");
            $(".line").css("background", "#fff");
        }

        if ($(window).scrollTop() >= 60*vh && $(window).scrollTop() < 150*vh){
            $(".pointBtnl").css("background", "#ffffff00");
            $("#pointBtn1").css("background", "#000");
        }
        else if ($(window).scrollTop() >= 150*vh && $(window).scrollTop() < 230*vh){
            $(".pointBtnl").css("background", "#ffffff00");
            $("#pointBtn2").css("background", "#000");
        }
        else if ($(window).scrollTop() >= 230*vh && $(window).scrollTop() < (90*vh*3 + 50*vh)){
            $(".pointBtnl").css("background", "#ffffff00");
            $("#pointBtn3").css("background", "#000");
        }
        else if ($(window).scrollTop() >= 90*vh*3/2 + 50*vh){
            $(".pointBtnl").css("background", "#ffffff00");
            $("#pointBtn4").css("background", "#fff");
        }
        else{
            $(".pointBtnl").css("background", "#ffffff00");
        }

    });
});

// $(document).ready(function(){
//     $(window).scroll(function(){ 
        
//     });
// });
