$(function(){
	var wwth=$(window).width();
	var yyxs=$('#subscribe').css('display');
	var display =$('.wrap').css('display');
	/*获取地址*/
	function GetQueryString(name){
	    var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
	    var r = window.location.search.substr(1).match(reg);
	    if(r!=null)return  unescape(r[2]); return null;
	}
	var login=GetQueryString('login');
	if(login!=null){
		$('.imgeject').hide();
		$('.gray').show();
		$('#reg_box').show();
		$(".gray").unbind();
		
	}
	if(yyxs=='block'){
		if(display=='none'){
			$('#subscribe').hide();
		}
	}
	if(wwth>1920){
		$('body').css({
			'width':'100%',
			'margin-top':'0',
			'margin-left':'auto',
			'margin-bottom':'0',
			'margin-right':'auto',
			'position':'relative'
			
		});
	}
	$('.video_btn').on('click',function(){
		$('.gray').show();
		$('.ej-video').show();
	})
	$('.gray').on('click',function(){
		$(this).hide();
		$('.ej-video').hide();
		$('.i-eject').hide();
		$('.i-eject p').html('');
		$('.logo_main').hide();
		$('.reg_box').hide();
	})
	/*返回按钮*/
    $('#return-top').hide();
    $(window).scroll(function(){
        if($(window).scrollTop()>300){
            $('#return-top').fadeIn(300);
        }else{
        	$('#return-top').fadeOut(200);
        }
    });
    $('#return-top').click(function(){
        $('body,html').animate({scrollTop:0},300);
        return false;
    })
 
	$('.close_v,.close').on('click',function(){
		$('.gray').hide();
		$('.i-eject').hide();
		$('.i-eject p').html('');
		$('.ej-video').hide();
		$('.ej-video p').html('');
		$('.txt,txt1').val('');
	})
   $('#login_box').hide();
   
   $('.yybtn a').on('click',function(){
   	   var name = $.cookie('username');
   	   console.log(name);
   	   if(name==undefined){
	   	   	$('#login_box').show();
	   	    $('.gray').show();
	   	     $('#subscribe').hide();
   	   }else if(name==null||name=='null'){
   	   		$('#login_box').show();
	   	    $('.gray').show();
	   	    $('#subscribe').hide();
   	   }else{
   	   		$('#login_box').hide();
   	   		 $('.gray').show();
   	   		 $('#subscribe').show();
   	   }
   })
	/*音乐*/
	var music=$('#audio1')[0];
	$('#btn-audio').on('click',function(){
		if(music.paused){ 
	        music.play(); 
	        $('.music_box a').removeClass('hover');
	    }else{ 
	        music.pause(); 
	        $('.music_box a').addClass('hover');
	    } 
	})
	function vidtk(){
		var hc=$('.music_box a').hasClass('hover');
		if(hc==true){
			music.pause();
		}else{
			music.pause(); 
			$('.music_box a').addClass('hover');
		}
		$('.gray').fadeIn();
		$('.i-eject').fadeIn();
		 $('.i-eject').css({
		 	'width':'960px',
            'height':'540px',
            'margin-left':'-500px',
            'margin-top':'-270px',
            'background':'#000'
		 })
	}
	$('.video_btn').on('click',function(){
		 vidtk();
		 $('.i-eject p').html('<iframe id="vbox" allowfullscreen="true" marginwidth="0" marginheight="0" scrolling="no" src="dist/20180605gw/v1.html" width="960" height="540" frameborder="no"></iframe>');
	})
	$('.video_close').on('click',function(){
		$('.videomain').html('');
		$('.videomain').hide();
		$('.wrap').show();
		music.play();
	})

	if(navigator.appName == "Microsoft Internet Explorer"&&parseInt(navigator.appVersion.split(";")[1].replace(/[ ]/g, "").replace("MSIE",""))<9){
	   $('.videomain').show();
    }
   /*index文件js*/
    var $li = $(".small_tb ul li");
         var len = $li.length-1;
         var _index = 0;
         var $img = $(".imgbox li");
         //var $btn = $(".b_btn div");
         var timer = null;



         //点击事件
         $li.click(function(){
             _index = $(this).index();
             $li.eq(_index).addClass("hover").siblings().removeClass("hover");
             $img.eq(_index).fadeIn().siblings().fadeOut();
             play();
         });
         //封装函数
         function play(){
             $li.eq(_index).addClass("hover").siblings().removeClass("hover");
             $img.eq(_index).fadeIn().siblings().fadeOut();
         }

         //定时轮播
         function auto(){
             timer = setInterval(function(){
                 _index++;
                 if(_index > len){
                     _index = 0;
                 }
                 play();
             },4000);
         }
         auto();
 
         $(".b_main").hover(function(){
            clearInterval(timer);
         },function(){
             auto();
         });
         $(".b_btn div").hover(function(){
             clearInterval(timer);
         },function(){
             auto();
         });
         function tab_p(n,m){
	  		$(n).on('mouseover',function () {
		         var _index = $(this).index();
		         $(m).eq(_index).show().siblings().hide();
		         $(this).addClass("hover").siblings().removeClass("hover");
		    });
	  	}
         tab_p('.tab_nav li','.img_cont .tab_main');
  		 tab_p('.tab_title li','.listbox .listnews');
  	 
  	  $('.navbtn').on('click',function(){
  	  	var aclass=$('.navbtn a').attr('class');
  	  	if(aclass==undefined||aclass==''){
  	  		$('.nav_head').animate({"height" : "30px"}, 200);
  	  		$('.navbtn a').addClass('hover');
  	  	}else{
  	  		$('.nav_head').animate({"height" : "152px"}, 200);
  	  		$('.navbtn a').removeClass('hover');
  	  	}
  	  })
  	  $(".nav_1 li a").click(function(){
		$("html,body").animate({ scrollTop:$($(this).attr("href")).offset().top + "px"},1000);
		$(this).addClass('hover').parents('li').siblings().children('a').removeClass('hover');
	  });
	   $('.left_nav').hide();
	    $(window).scroll(function(){
	        if($(window).scrollTop()>300){
	            $('.left_nav').fadeIn(300);
	        }else{
	        	$('.left_nav').fadeOut(200);
	        }
	    });
	  $('.topbtn,.backtop').click(function(){
        $('body,html').animate({scrollTop:0},300);
        return false;
    })
	$('#video_btn li a').on('click',function(){
		music.pause(); 
		$('.music_box a').addClass('hover');
		var z1=$(this).parents('li').index();
		$('.gray').fadeIn();
		$('.i-eject').fadeIn();
		 $('.i-eject').css({
		 	'width':'960px',
            'height':'540px',
            'margin-left':'-500px',
            'margin-top':'-270px',
            'background':'#000'
		 })
		 $('.i-eject p').html('<iframe id="vbox" allowfullscreen="true" marginwidth="0" marginheight="0" scrolling="no" src="video/a'+parseInt(z1+1)+'.html" width="960" height="540" frameborder="no"></iframe>')
	})
	$('.imgcont li').hover(function(){
		$(this).children('em').stop().fadeIn();
	},function(){
		$(this).children('em').stop().fadeOut();
	})
	$('.imgcont li em').on('click',function(){
		var ind=$(this).parents('li').index();
		var str=$(this).parents('li').children('img').attr('src');
		var index = str .lastIndexOf("\_"); 
		str= str .substring(0,index);
		$('.gray').fadeIn();
		$('.i-eject').fadeIn();
		$('.i-eject').css({
            'width':'1000px',
            'height':'560px',
            'margin-left':'-510px',
            'margin-top':'-280px',
            'background':'#000'
        })
		$('.i-eject p').html('<img src="'+str+'_0'+parseInt(ind+1)+'.jpg">');
	})
	  if(navigator.appName == "Microsoft Internet Explorer"&&parseInt(navigator.appVersion.split(";")[1].replace(/[ ]/g, "").replace("MSIE",""))<9){
		$('#videoBox').hide();
	}
	$('#loginbtn').on('click',function(){
		$('.gray').show();
		$('#reg_box').show();
	})
	$('#yybtn').on('click',function(){
		$('.gray').show();
		$('#login_box').show();
	})
	
	if(wwth<1000){
		$('.music_box').css({
			'top':'0',
		})
		$('.video_box').html('');
	}
	$('.video_b a').on('click',function(){
		vidtk();
		$('.i-eject p').html('<iframe id="vbox" allowfullscreen="true" marginwidth="0" marginheight="0" scrolling="no" src="dist/20180605gw/v3.html" width="960" height="540" frameborder="no"></iframe>')
	});

});
$(function(){
    $("#Flash").delete();
});