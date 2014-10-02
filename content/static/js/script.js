$(document).ready(function(){
	$("#zoom_03").elevateZoom({gallery:'gal1', cursor: 'pointer', galleryActiveClass: 'active', imageCrossfade: true, loadingIcon: 'http://www.elevateweb.co.uk/spinner.gif'});

	$("#zoom_03").bind("click", function(e) { 
		var ez = $('#zoom_03').data('elevateZoom');	
		$.fancybox(ez.getGalleryList()); 
		return false; 
	});
});