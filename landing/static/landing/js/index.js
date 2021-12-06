const vh = window.innerHeight / 100;
$(document).ready(function(){
    $(window).scroll(function(){  
        if ($(window).scrollTop() > 50*vh &&  $(window).scrollTop() < (90*vh*3 + 50*vh)){
            $("#board").css("color", "#000");
            $(".pointBtn").css("background", "#ffffff00");
            $(".pointBtn").css("border-color", "#000");
            $(".line").css("background", "#000");
        }
        else{
            $("#board").css("color", "#fff");
            $(".pointBtn").css("background", "#ffffff00");
            $(".pointBtn").css("border-color", "#fff");
            $(".line").css("background", "#fff");
        }

        if ($(window).scrollTop() >= 60*vh && $(window).scrollTop() < 150*vh){
            $(".pointBtn").css("background", "#ffffff00");
            $("#pointBtn1").css("background", "#000");
        }
        else if ($(window).scrollTop() >= 150*vh && $(window).scrollTop() < 230*vh){
            $(".pointBtn").css("background", "#ffffff00");
            $("#pointBtn2").css("background", "#000");
        }
        else if ($(window).scrollTop() >= 230*vh && $(window).scrollTop() < (90*vh*3 + 50*vh)){
            $(".pointBtn").css("background", "#ffffff00");
            $("#pointBtn3").css("background", "#000");
        }
        else if ($(window).scrollTop() >= 90*vh*3/2 + 50*vh){
            $(".pointBtn").css("background", "#ffffff00");
            $("#pointBtn4").css("background", "#fff");
        }
        else{
            $(".pointBtn").css("background", "#ffffff00");
        }

    });
});

// $(document).ready(function(){
//     $(window).scroll(function(){ 
        
//     });
// });
