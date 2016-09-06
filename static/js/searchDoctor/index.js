var searchDoctorObject = {
  initialize: function(){
    console.info('--------------line 3');
  }
};

$(document).ready(function(){
  console.info('----------in ready------');
  searchDoctorObject.initialize();
});
