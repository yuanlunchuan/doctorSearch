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
  onIconAreaClicked: function(event){
    var self = searchDoctorObject;
    if($('.float-layer').is('.hidden')){
      $('.float-layer').removeClass('hidden');
    }else{
      $('.float-layer').addClass('hidden');
    }
  },
  onFloatLayerClicked: function(event){
    var self = searchDoctorObject;
    $('.float-layer').addClass('hidden');
  },
  onClosedIconClicked: function(event){
    var self = searchDoctorObject;
    $('.float-layer').addClass('hidden');
  },
  onInputBoxClicked: function(event){
    var self = searchDoctorObject;
    event.stopPropagation();
  },
  initialize: function(){
    var self = searchDoctorObject;
    $(window).scroll(self.onWindowScrolled);
    $('.icon-area').on('click', self.onIconAreaClicked);
    $('.float-layer').on('click', self.onFloatLayerClicked);
    $('.close-icon').on('click', self.onClosedIconClicked);
    $('.input-box').on('click', self.onInputBoxClicked)
  }
};

$(document).ready(function(){
  searchDoctorObject.initialize();
});
