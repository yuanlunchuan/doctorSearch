var searchDoctorObject = {
  onWindowScrolled: function(){
    var self = searchDoctorObject;

    var scrollToTopDistance = $(document).scrollTop();
    if(scrollToTopDistance>0&&$('#navbar').is('.hidden')){
      $('#navbar').removeClass('hidden');
    }
    if(scrollToTopDistance==0&&!$('#navbar').is('.hidden')){
      $('#navbar').addClass('hidden');
    }
  },

  initialize: function(){
    var self = searchDoctorObject;
    $(window).scroll(self.onWindowScrolled);
  }
};

$(document).ready(function(){
  searchDoctorObject.initialize();
});
