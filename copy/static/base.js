$(document).ready(function(){
$('.myclass').vTicker({
   speed: 400,
   pause: 3000,
   showItems: 4,
   animation: 'fade',
   mousePause: true,
   height:200,
   direction: 'up'
});


	
	$(".header-items").click(function(){
		 var col=$(this).children("div").css("backgroundColor");
		var position=$(this).position();
		var left=position.left+70;
		 $(".arrow-up").css({'border-bottom-color':col,});
		$(".arrow-up").animate({'left':left,},"slow");
			
		var title=$(this).attr('title');
		if(title=='contactus'){
			$.ajax({
			url:'/contactus/',
				success:function(data){
				$('.container').html(data);
				 var right=$('.container-right');
                        var left=$('.container-center');
                        right.fadeOut(00).animate({'left':'25%'},00).fadeIn(00).animate({'left':'0'},800)
                        left.fadeOut(00).animate({'left':'-75%'},00).fadeIn(00).animate({'left':'0'},800);
                        $(".category").css({'backgroundColor':col,});
                        $(".container-left").css({'backgroundColor':col,});
                        $(".arrow-up").css({'border-bottom-color':col,'left':left,});
	
				}
			});
		}
		else{
		$.ajax(
		{
			url:'/content/'+title,
			data:{},	
			success:function(data){	
			$('.container').html(data);
			var right=$('.container-right');
			var left=$('.container-center');
			right.fadeOut(00).animate({'left':'25%'},00).fadeIn(00).animate({'left':'0'},800)
			left.fadeOut(00).animate({'left':'-75%'},00).fadeIn(00).animate({'left':'0'},800);
			$(".category").css({'backgroundColor':col,});
			$(".container-left").css({'backgroundColor':col,});
			$(".arrow-up").css({'border-bottom-color':col,'left':left,});


			}
			});}
	});
	 $(".category").live('click',function(e){
		var col1=$(this).css("backgroundColor");

		 $('.container-left').show(00).slideUp(700);
		$('.container-center').hide();
			
                var title=$(this).attr('title');
	
                $.ajax(
                {
                        url:'/content/'+title,
                        data:{},
                        success:function(data){
                        $('.container-center').html(data).fadeIn(1200);/*fadeOut(00).animate({'bottom':'100%'},00).fadeIn(00).animate({'bottom':'00%'},1000);;*/
	//		$(".container-left").show();
			$(".arrow-up").css({'border-bottom-color':col1,});
                        }
		                        });

			
        });
	$(".loading").ajaxStart(function(){
        $(this).show();
           }).ajaxStop(function(){
            $(this).hide();
            });
//	$(".header-items div").live('click',function(){
//	 var color=$(this).css("backgroundColor");
	
  //              $(".category").css({'backgroundColor':color,});

//	});
				
	$(".header-items").mouseenter(function(){
		var id=this.id;

	 $("#"+id+" p").fadeIn("slow").css({'z-index':'6','opacity':'1'});

		$("#"+id+" div").css({'opacity':'.1'},1000);
		
	//	$(this).css({'background-color':'white'});
		$(this).children(".head").css({'opacity':'.1'});
		});
	//	$(".header-items").mouseenter(function(){
	//		$(".header-items p").show(20);
	//		});
			$(".header-items").mouseleave(function(){
				var id=this.id;
		$("#"+id+" p").fadeOut(20).css({'z-index':'1',});
			 $(this).children(".head").css({'opacity':'1'});
					 $("#"+id+" div").css({'opacity':'1'});

				$(".header-items div").show("slow");
			//	$(this).css({'background-color':'red'});
		//$(".header-items p").fadeOut(450);
			});
	$(".category").live('dbclick',function(){return false;});

		//$("#header-item_child").children().show(00).animate({"top":"100%" ,"opacity":'6',},1500).css({'height':'150%','width':'150%','z-index':'12'});
	//$("#header-item_child").mouseleave(function(){
	//	$("#header-item_child").children().fadeOut(00);
//	});

	



});
