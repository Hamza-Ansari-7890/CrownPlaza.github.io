$(document).ready(function(){
    var trnum = 0;
    var maxRows = 7;
    var totalRows = $('table tbody tr').length;
    $('table tr:gt(0)').each(function(){
          trnum++
          if(trnum > maxRows){
                $(this).hide()
          }
          else if(trnum <= maxRows){
                $(this).show()
          }
    });
    if(totalRows > maxRows){
    var pagenum = Math.ceil(totalRows/maxRows)
    for(i = 1; i<=pagenum;i++)
    {
         $('.pagination').append('<li class = "page-item" ><span class="page-link">'+ i +'</span></li>').show()
    }
 }

 $('.pagination li:first-of-type').addClass('active')

 $('.pagination li').on('click',function(){
 $('.pagination li').removeClass('active')
 $(this).addClass('active')
 });

 $('.pagination li span').on('click',function(){
 var pagenum = $(this).html()
 var trindex= 0;
         $('table tr:gt(0)').each(function(){
         trindex++
         if(trindex > (maxRows*pagenum) || trindex <= ((maxRows*pagenum)-maxRows))
         {
             $(this).hide()
         }
         else{
              $(this).show()
         }
      });
   });
   $('.btn-click').click(function(){
if($('.d2').val() == "")
 {
 alert("please enter the check-out date")
 }
 else
 {
 var d1 = $('.d1').val();
 var d2 = $('.d2').val();
 var dateOne = new Date(d1);
 var dateTwo = new Date(d2);
 var days = (dateTwo.getTime()-dateOne.getTime()) / (1000 * 3600 * 24);
 $('.append1').append('<div class="form-floating mb-3">'+
     '<input type="text" class="form-control Days" id="floatingInput" placeholder="No. of Days" name="days"'+
         'value='+days+' required>'+
     '<label for="floatingInput">No. of Days</label></div>')
 var Type = $('.type').val()
 alert(Type)
 if(Type == 'Standard Deluxe AC')
 {
 total = ((550 + 250)*days)
 $('.append2').append('<div class="form-floating mb-3">'+
     '<input type="text" class="form-control price" id="floatingInput" placeholder="Total amount" name="price"'+
             'value='+total+' required>'+
     '<label for="floatingInput">Total amount</label></div>')
 }
 else if(Type == "Luxury AC")
 {
 total = ((550 + 450)*days)
 $('.append2').append('<div class="form-floating mb-3">'+
     '<input type="text" class="form-control price" id="floatingInput" placeholder="Total amount" name="price"'+
             'value='+total+' required>'+
     '<label for="floatingInput">Total amount</label></div>')
  }
 else if (Type == 'Suite AC')
 {
 total = ((550 + 750)*days)
 $('.append2').append('<div class="form-floating mb-3">'+
     '<input type="text" class="form-control price" id="floatingInput" placeholder="Total amount" name="price"'+
             'value='+total+' required>'+
     '<label for="floatingInput">Total amount</label></div>')
 }
 else
 {
 total = 550 * days
 $('.append2').append('<div class="form-floating mb-3">'+
     '<input type="text" class="form-control price" id="floatingInput" placeholder="Total amount" name="price"'+
             'value='+total+' required>'+
     '<label for="floatingInput">Total amount</label></div>')
 }
 $('.btn-click').attr("aria-disabled",true)
 }
 })
 let images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg']
    setInterval(function(){
     let random = Math.floor(Math.random() * 5);
     $('.rounded').attr("src",`/static/image/${images[random]}`)
    }, 2200);
})











//
//else if (Type == 'Suite')
//{
//total = ((550 + 750)*days)
//$('.append2').append('<div class="form-floating mb-3">'+
//    '<input type="text" class="form-control price" id="floatingInput" placeholder="Total amount" name="price"'+
//            'value='+total+' required>'+
//    '<label for="floatingInput">Total amount</label></div>')
//}
//else
//{
//total = 550 * days
//$('.append2').append('<div class="form-floating mb-3">'+
//    '<input type="text" class="form-control price" id="floatingInput" placeholder="Total amount" name="price"'+
//            'value='+total+' required>'+
//    '<label for="floatingInput">Total amount</label></div>')
//}
//$('.btn-click').attr("aria-disabled",true)
//}
//});
//let images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg']
//setInterval(function(){
// let random = Math.floor(Math.random() * 4);
// $('.rounded').attr("src","\static\image"images[random])
//}, 800);
////$('#floatingSelect').on('change',function(){
////  value = $(this).val();
////
////  $('#Filter').filter(function(){
////   $(this).toggle($(this).text().toLowerCase().indexOf(value)>-1);
//=======







//  })

 //$('#floatingSelect').on('change',function(){
 //  value = $(this).val();
 //
 //  $('#Filter').filter(function(){
 //   $(this).toggle($(this).text().toLowerCase().indexOf(value)>-1);
 //  })